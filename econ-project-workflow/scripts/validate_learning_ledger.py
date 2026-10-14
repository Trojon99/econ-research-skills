"""Validate local ledger declarations, not source truth or publication permission."""


import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

SOURCE_TYPES = ("article", "book", "chapter", "paper", "documentation", "lecture")
COVERAGE = ("unread", "partial", "complete")
CHECK_KINDS = ("primary_source", "documentation", "calculation", "code_execution")
CHECK_STATUSES = ("not_attempted", "partial", "complete", "blocked")
LESSON_STATUSES = ("candidate", "integrated", "needs_recheck", "superseded", "rejected")
VALIDATION_LEVELS = ("reading_only", "primary_checked", "numerically_checked", "executed")


def _object(value, path, required, optional, errors):
    if not isinstance(value, dict):
        errors.append(f"{path}: expected object")
        return False
    for field in required:
        if field not in value:
            errors.append(f"{path}.{field}: required")
    for field in value:
        if field not in required and field not in optional:
            errors.append(f"{path}.{field}: unknown field")
    return True


def _text(value, path, errors):
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{path}: expected nonempty string")


def _enum(value, choices, path, errors):
    if not isinstance(value, str) or value not in choices:
        errors.append(f"{path}: expected one of {', '.join(choices)}")


def _strings(value, path, errors):
    if not isinstance(value, list):
        errors.append(f"{path}: expected string array")
        return
    for i, item in enumerate(value):
        _text(item, f"{path}[{i}]", errors)


def validate(data, root=None):
    """Return declaration errors without writing, fetching, or executing anything."""
    errors = []
    if not _object(data, "ledger", ("schema_version", "sources", "lessons"), (), errors):
        return errors
    if type(data.get("schema_version")) is not int or data.get("schema_version") != 1:
        errors.append("ledger.schema_version: expected integer 1")
    for name in ("sources", "lessons"):
        if not isinstance(data.get(name), list):
            errors.append(f"ledger.{name}: expected array")
    if errors:
        return errors
    for i, source in enumerate(data["sources"]):
        path = f"sources[{i}]"
        if not _object(source, path, ("source_id", "source_type", "title", "version", "read_at", "coverage"),
                       ("url", "authors", "edition", "checks"), errors):
            continue
        for field in ("source_id", "title", "version"):
            _text(source.get(field), f"{path}.{field}", errors)
        _enum(source.get("source_type"), SOURCE_TYPES, f"{path}.source_type", errors)
        for field in ("url", "edition"):
            if field in source:
                _text(source[field], f"{path}.{field}", errors)
        if "authors" in source:
            _strings(source["authors"], f"{path}.authors", errors)
        read_at = source.get("read_at")
        try:
            if not isinstance(read_at, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", read_at):
                raise ValueError
            date.fromisoformat(read_at)
        except ValueError:
            errors.append(f"{path}.read_at: expected ISO date YYYY-MM-DD")
        coverage = source.get("coverage")
        if _object(coverage, f"{path}.coverage", ("text", "images", "scope"), (), errors):
            _enum(coverage.get("text"), COVERAGE, f"{path}.coverage.text", errors)
            _enum(coverage.get("images"), COVERAGE + ("not_applicable",), f"{path}.coverage.images", errors)
            _text(coverage.get("scope"), f"{path}.coverage.scope", errors)
        checks = source.get("checks", [])
        if not isinstance(checks, list):
            errors.append(f"{path}.checks: expected array")
        else:
            for j, check in enumerate(checks):
                cp = f"{path}.checks[{j}]"
                if _object(check, cp, ("kind", "locator", "scope", "status", "version"), (), errors):
                    _enum(check.get("kind"), CHECK_KINDS, f"{cp}.kind", errors)
                    _enum(check.get("status"), CHECK_STATUSES, f"{cp}.status", errors)
                    for field in ("locator", "scope", "version"):
                        _text(check.get(field), f"{cp}.{field}", errors)
    for i, lesson in enumerate(data["lessons"]):
        path = f"lessons[{i}]"
        if not _object(lesson, path, ("lesson_id", "statement", "status", "source_ids", "evidence",
                       "assumptions", "limitations", "target", "supersedes", "validation", "conflict_note"), (), errors):
            continue
        for field in ("lesson_id", "statement"):
            _text(lesson.get(field), f"{path}.{field}", errors)
        _enum(lesson.get("status"), LESSON_STATUSES, f"{path}.status", errors)
        for field in ("source_ids", "assumptions", "limitations", "supersedes"):
            _strings(lesson.get(field), f"{path}.{field}", errors)
        if not isinstance(lesson.get("conflict_note"), str):
            errors.append(f"{path}.conflict_note: expected string (may be empty)")
        if lesson.get("target") is not None:
            _text(lesson["target"], f"{path}.target", errors)
        evidence = lesson.get("evidence")
        if not isinstance(evidence, list):
            errors.append(f"{path}.evidence: expected array")
        else:
            for j, item in enumerate(evidence):
                ep = f"{path}.evidence[{j}]"
                if _object(item, ep, ("source_id", "locator", "scope", "relation"), (), errors):
                    for field in ("source_id", "locator", "scope"):
                        _text(item.get(field), f"{ep}.{field}", errors)
                    _enum(item.get("relation"), ("supports", "contradicts", "context"), f"{ep}.relation", errors)
        validation = lesson.get("validation")
        if _object(validation, f"{path}.validation", ("level", "record"), ("code_version", "software_version"), errors):
            _enum(validation.get("level"), VALIDATION_LEVELS, f"{path}.validation.level", errors)
            _text(validation.get("record"), f"{path}.validation.record", errors)
            for field in ("code_version", "software_version"):
                if field in validation:
                    _text(validation[field], f"{path}.validation.{field}", errors)
    if errors:
        return errors  # Cross-reference checks only run on structurally valid data.
    sources = {source["source_id"]: source for source in data["sources"]}
    lessons = {lesson["lesson_id"]: lesson for lesson in data["lessons"]}
    if len(sources) != len(data["sources"]):
        errors.append("sources: duplicate source_id")
    if len(lessons) != len(data["lessons"]):
        errors.append("lessons: duplicate lesson_id")
    resolved_root = None
    if root is not None:
        try:
            resolved_root = Path(root).resolve(strict=True)
            if not resolved_root.is_dir():
                raise ValueError("root must be a directory")
        except (OSError, RuntimeError, ValueError, TypeError) as exc:
            errors.append(f"root: {exc}")
    for lesson in data["lessons"]:
        lid = lesson["lesson_id"]
        target = lesson["target"]
        if target is not None:
            parts = target.split("/")
            safe = (all(re.fullmatch(r"[A-Za-z0-9_.-]+", part) and part not in (".", "..") for part in parts)
                    and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", parts[0])
                    and ((len(parts) == 2 and parts[1] == "SKILL.md")
                         or (len(parts) >= 3 and parts[1] in ("references", "scripts", "templates"))))
            if not safe:
                errors.append(f"{lid}.target: expected safe repo-relative skill entrypoint/references/scripts/templates file")
            elif resolved_root is not None:
                try:
                    resolved = (resolved_root / target).resolve(strict=True)
                    if not resolved.is_relative_to(resolved_root) or not resolved.is_file():
                        raise ValueError("target must be a file contained inside root (including symlinks)")
                except (OSError, RuntimeError, ValueError) as exc:
                    errors.append(f"{lid}.target: {exc}")
        for field, available in (("source_ids", sources), ("supersedes", lessons)):
            ids = lesson[field]
            if len(set(ids)) != len(ids):
                errors.append(f"{lid}.{field}: duplicate reference")
            for reference in ids:
                if reference not in available:
                    errors.append(f"{lid}.{field}: missing ID {reference}")
        if lid in lesson["supersedes"]:
            errors.append(f"{lid}.supersedes: self reference")
        if lesson["status"] == "integrated":
            if target is None:
                errors.append(f"{lid}.target: integrated requires a named target")
            if (lesson["supersedes"] or any(item["relation"] == "contradicts" for item in lesson["evidence"])) and not lesson["conflict_note"].strip():
                errors.append(f"{lid}: integrated replacement or contradiction requires conflict_note")
            for predecessor in lesson["supersedes"]:
                if predecessor in lessons and lessons[predecessor]["status"] != "superseded":
                    errors.append(f"{lid}: predecessor {predecessor} must be superseded, not active")
        for item in lesson["evidence"]:
            if item["source_id"] not in sources or item["source_id"] not in lesson["source_ids"]:
                errors.append(f"{lid}.evidence: source_id must exist and be in source_ids")
        support = [item for item in lesson["evidence"]
                   if item["relation"] == "supports" and item["source_id"] in sources
                   and sources[item["source_id"]]["coverage"]["text"] != "unread"
                   and _body_locator(item["locator"], sources[item["source_id"]]["title"])]
        if lesson["status"] == "integrated" and not support:
            errors.append(f"{lid}: integrated requires declared read support with a body locator and scope, not title metadata")
        level = lesson["validation"]["level"]
        kinds = {"primary_checked": ("primary_source", "documentation"),
                 "numerically_checked": ("calculation",), "executed": ("code_execution",)}
        if level in kinds:
            matching = any(check["kind"] in kinds[level] and check["status"] == "complete"
                           and check["scope"] == item["scope"]
                           and _body_locator(check["locator"], sources[item["source_id"]]["title"])
                           for item in support for check in sources[item["source_id"]].get("checks", []))
            if not matching:
                errors.append(f"{lid}: {level} requires completed source check matching a read support scope exactly")
        if level == "executed":
            for field in ("code_version", "software_version"):
                if field not in lesson["validation"]:
                    errors.append(f"{lid}.validation.{field}: executed requires recorded version")
    # Kahn's algorithm avoids recursion limits for long replacement histories.
    incoming = dict.fromkeys(lessons, 0)
    for lesson in lessons.values():
        for predecessor in lesson["supersedes"]:
            if predecessor in incoming:
                incoming[predecessor] += 1
    queue = [lid for lid, count in incoming.items() if count == 0]
    visited = 0
    while queue:
        lid = queue.pop()
        visited += 1
        for predecessor in lessons[lid]["supersedes"]:
            if predecessor in incoming:
                incoming[predecessor] -= 1
                if incoming[predecessor] == 0:
                    queue.append(predecessor)
    if visited != len(lessons):
        errors.append("lessons.supersedes: cycle")
    for source in data["sources"]:
        coverage = source["coverage"]
        if (source["source_type"] == "book" and coverage["text"] == "complete"
                and re.search(r"\b(selected|excerpt)\b|\b(chapter|page|section)s?\b.*\bonly\b|\bonly\b.*\b(chapter|page|section)s?\b", coverage["scope"], re.I)):
            errors.append(f"{source['source_id']}: selected book scope must not declare complete book text")
    return errors


def summary(data):
    """Count a validated ledger's declarations only, never inferred reading/checks.

    body_complete is the declared text status for the recorded source scope,
    not a claim that the entire parent book or every image has been read.
    Call validate first; this function expects its valid input shape.
    """
    result = {"declarations_only": True, "source_count": len(data["sources"]),
              "lesson_count": len(data["lessons"])}
    for state in COVERAGE:
        result[f"body_{state}"] = sum(source["coverage"]["text"] == state for source in data["sources"])
    result["image_coverage"] = {state: sum(source["coverage"]["images"] == state for source in data["sources"])
                                for state in COVERAGE + ("not_applicable",)}
    result["check_statuses"] = {
        kind: {status: sum(check["kind"] == kind and check["status"] == status
                           for source in data["sources"] for check in source.get("checks", []))
               for status in CHECK_STATUSES} for kind in CHECK_KINDS}
    result["validation_levels"] = {level: sum(lesson["validation"]["level"] == level for lesson in data["lessons"])
                                   for level in VALIDATION_LEVELS}
    result["lesson_statuses"] = {status: sum(lesson["status"] == status for lesson in data["lessons"])
                                 for status in LESSON_STATUSES}
    return result


def _body_locator(locator, title):
    """Reject obvious metadata-only declarations; cannot verify a locator's truth."""
    value = locator.strip()
    return (value.casefold() != title.strip().casefold()
            and not re.match(r"(?i)^(title|author|doi|isbn|url|metadata|citation)\b|https?://", value))


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__ + " Pure read: no mutation, commands, or network. Counts are declarations only.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python3 econ-project-workflow/scripts/validate_learning_ledger.py /tmp/private-ledger.json
  python3 econ-project-workflow/scripts/validate_learning_ledger.py /tmp/private-ledger.json --root .

Keep filled ledgers private, outside this repository. --root checks target file
existence and symlink containment; it never restricts the input ledger location.
This validates structure/declarations, not truth, copyright, or publication permission.
""")
    parser.add_argument("ledger", type=Path, help="local JSON ledger anywhere you choose")
    parser.add_argument("--root", type=Path, help="optional repository root for target existence checks")
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.ledger.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
    except (OSError, ValueError, UnicodeError, RecursionError) as exc:
        print(f"ERROR: cannot read JSON ledger: {exc}", file=sys.stderr)
        return 1
    errors = validate(data, root=args.root)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print(json.dumps(summary(data), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
