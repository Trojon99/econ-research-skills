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
