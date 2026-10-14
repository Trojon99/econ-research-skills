"""Check this repository's packaging (not economic or citation correctness)."""
import argparse
import re
from pathlib import Path


def _without_fences(text):
    """Skip backtick/tilde illustrations, including longer indented fences."""
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
        elif match:
            fence = match[1]
        else:
            lines.append(line)
    return "".join(lines)


def validate(root):
    errors = []
    try:
        version = (root / "VERSION").read_text(encoding="utf-8").strip()
        readme = (root / "README.md").read_text(encoding="utf-8")
        changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
    except OSError as exc:
        return [str(exc)]
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("Invalid VERSION format")
    readme_version = re.search(r"\*\*Current version:\*\* `v([^`]+)`", readme)
    changelog_version = re.search(r"^## \[([^\]]+)\]", changelog, re.MULTILINE)
    if not readme_version or readme_version.group(1) != version:
        errors.append("README version differs from VERSION")
    if not changelog_version or changelog_version.group(1) != version:
        errors.append("Latest CHANGELOG version differs from VERSION")
    names = set()
    skills = sorted(root.glob("*/SKILL.md"))
    if not skills:
        errors.append("No skill entrypoints found")
    for entry in skills:
        relative = entry.relative_to(root)
        text = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.DOTALL)
        if not match:
            errors.append(f"{relative}: missing frontmatter")
            continue
        header, body = match.groups()
        name = re.search(r"^name:[ \t]*([^\n]+)$", header, re.MULTILINE)
        description = re.search(r"^description:[ \t]*([^\n]+)$", header, re.MULTILINE)
        if not name or not description or not description.group(1).strip("\"' "):
            errors.append(f"{relative}: missing name or description")
        if name:
            slug = name.group(1).strip().strip("\"'")
            if slug != entry.parent.name:
                errors.append(f"{relative}: name differs from directory slug")
            if slug in names:
                errors.append(f"{relative}: duplicate skill name")
            names.add(slug)
        if not body.strip():
            errors.append(f"{relative}: empty body")
    catalog = set(re.findall(r"\]\(([^)]+/SKILL\.md)\)", readme))
    expected = {entry.relative_to(root).as_posix() for entry in skills}
    if catalog != expected:
        errors.append(f"README skill catalog mismatch: missing={sorted(expected - catalog)}, extra={sorted(catalog - expected)}")
    for document in sorted(root.rglob("*.md")):
        if ".git" in document.relative_to(root).parts:
            continue
        text = document.read_text(encoding="utf-8")
        # Code examples are not actual links or bundle-file declarations.
        text = _without_fences(text)
        bundle = root / document.relative_to(root).parts[0]
        for target in re.findall(r"`([^`\n]+)`", text):
            if not re.fullmatch(r"(?:[a-z0-9-]+/)?(?:references|assets|templates|scripts)/[A-Za-z0-9_./-]+\.[A-Za-z0-9]+", target):
                continue  # Directory descriptors, commands, globs, and placeholders are not file declarations.
            first = target.split("/", 1)[0]
            base = bundle if first in ("references", "assets", "templates", "scripts") and (bundle / "SKILL.md").is_file() else root
            exists = (base / target).is_file()
            if not exists and document.parent == root and first in ("references", "assets", "templates", "scripts"):
                # Older root changelogs may name an unqualified moved bundle file.
                # Accept only a unique existing match, never a blanket exemption.
                exists = sum((entry.parent / target).is_file() for entry in skills) == 1
            if not exists:
                errors.append(f"{document.relative_to(root)}: broken backtick file {target}")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            target = target.strip().strip("<>")
            if target.startswith(("#", "//")) or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
                continue
            local = target.split("#", 1)[0].split("?", 1)[0]
            if local and not (document.parent / local).exists():
                errors.append(f"{document.relative_to(root)}: broken local link {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    for error in errors:
        print("ERROR:", error)
    if not errors:
        print("PASS: repository packaging checks")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
