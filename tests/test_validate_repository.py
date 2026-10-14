"""Packaging regression tests with isolated, explicitly synthetic fixtures."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_repository.py"


class RepositoryValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "VERSION").write_text("0.1.0\n", encoding="utf-8")
        (self.root / "README.md").write_text(
            "**Current version:** `v0.1.0`\n[test-skill](test-skill/SKILL.md)\n",
            encoding="utf-8",
        )
        (self.root / "CHANGELOG.md").write_text("## [0.1.0] - 2026-01-01\n", encoding="utf-8")
        bundle = self.root / "test-skill"
        bundle.mkdir()
        (bundle / "SKILL.md").write_text(
            "---\nname: test-skill\ndescription: Synthetic test fixture.\n---\n# Test\n",
            encoding="utf-8",
        )

    def run_validator(self):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.root)],
            text=True, capture_output=True, check=False,
        )

    def test_backtick_bundle_files_must_exist(self):
        entry = self.root / "test-skill/SKILL.md"
        original = entry.read_text(encoding="utf-8")
        for folder, filename in [("references", "guide.md"), ("assets", "image.svg"), ("templates", "ledger.json"), ("scripts", "check.py")]:
            with self.subTest(folder=folder):
                relative = f"{folder}/{filename}"
                entry.write_text(original + f"Read `{relative}`.\n", encoding="utf-8")
                result = self.run_validator()
                self.assertNotEqual(result.returncode, 0, "missing backtick file must fail")
                self.assertIn(relative, result.stdout)
                file = self.root / "test-skill" / relative
                file.parent.mkdir(exist_ok=True)
                file.write_text("Synthetic fixture", encoding="utf-8")
                self.assertEqual(self.run_validator().returncode, 0)
                nested = self.root / "test-skill/references/nested.md"
                nested.parent.mkdir(exist_ok=True)
                nested.write_text(f"Load `{relative}` from the bundle.\n", encoding="utf-8")
                self.assertEqual(self.run_validator().returncode, 0)
        entry.write_text(original + "Use `test-skill/templates/ledger.json`.\n", encoding="utf-8")
        self.assertEqual(self.run_validator().returncode, 0)

    def test_root_historical_unqualified_reference_requires_unique_bundle_file(self):
        guide = self.root / "test-skill/references/guide.md"
        guide.parent.mkdir()
        guide.write_text("Synthetic fixture", encoding="utf-8")
        readme = self.root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "History: moved `references/guide.md` into a skill.\n", encoding="utf-8")
        self.assertEqual(self.run_validator().returncode, 0)
        readme.write_text(readme.read_text(encoding="utf-8") + "Missing `references/absent.md`.\n", encoding="utf-8")
        self.assertNotEqual(self.run_validator().returncode, 0)

    def test_fenced_illustrations_and_broad_descriptors_are_not_file_references(self):
        entry = self.root / "test-skill/SKILL.md"
        original = entry.read_text(encoding="utf-8")
        for fence in ("~~~", "   ````"):
            with self.subTest(fence=fence):
                entry.write_text(original + f"\n{fence}text\n`references/missing.md`\n[Example](templates/missing.json)\n{fence}\n" +
                                 "Broad legacy descriptors: `references/`, `assets/*.svg`, `templates/<name>.json`.\n", encoding="utf-8")
                result = self.run_validator()
                self.assertEqual(result.returncode, 0, result.stdout)
                with entry.open("a", encoding="utf-8") as handle:
                    handle.write("Actual `scripts/missing.py`.\n")
                self.assertNotEqual(self.run_validator().returncode, 0)

    def test_ci_is_read_only_pinned_and_runs_package_checks(self):
        workflow = SCRIPT.parents[1] / ".github/workflows/validate.yml"
        self.assertTrue(workflow.is_file(), "CI workflow missing")
        text = workflow.read_text(encoding="utf-8")
        self.assertIn("contents: read", text)
        self.assertIn("persist-credentials: false", text)
        self.assertIn("actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683", text)
        self.assertIn("actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065", text)
        self.assertIn('python-version: ["3.11", "3.13"]', text)
        for command in ("python -m unittest discover -s tests -v", "python scripts/validate_repository.py",
                        "python econ-project-workflow/scripts/validate_learning_ledger.py econ-project-workflow/templates/learning-ledger.json"):
            self.assertIn(command, text)
        self.assertNotIn("secrets.", text)
        self.assertNotIn("upload-artifact", text)
        self.assertNotIn("pull_request_target", text)

    def test_accepts_consistent_packaging(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


    def test_rejects_version_mismatch(self):
        (self.root / "VERSION").write_text("0.2.0\n", encoding="utf-8")
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("version", result.stdout.lower())


    def test_rejects_invalid_skill_packaging(self):
        entry = self.root / "test-skill" / "SKILL.md"
        valid = entry.read_text(encoding="utf-8")
        cases = {
            "missing description": "---\nname: test-skill\n---\n# Test\n",
            "empty description before metadata": "---\nname: test-skill\ndescription:\nversion: 0.1.0\n---\n# Test\n",
            "empty name before metadata": "---\nname:\ndescription: Fixture.\n---\n# Test\n",
            "wrong slug": valid.replace("name: test-skill", "name: different-slug"),
            "empty body": "---\nname: test-skill\ndescription: Fixture.\n---\n",
            "missing frontmatter": "# Test\n",
        }
        for label, text in cases.items():
            with self.subTest(label=label):
                entry.write_text(text, encoding="utf-8")
                result = self.run_validator()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("test-skill", result.stdout)
        entry.write_text(valid, encoding="utf-8")


    def test_rejects_broken_local_link(self):
        with (self.root / "test-skill" / "SKILL.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[Missing](references/missing.md)\n")
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("references/missing.md", result.stdout)


    def test_rejects_uncatalogued_skill(self):
        (self.root / "README.md").write_text("**Current version:** `v0.1.0`\n", encoding="utf-8")
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("catalog", result.stdout.lower())


if __name__ == "__main__":
    unittest.main()
