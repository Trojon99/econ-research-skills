"""Synthetic ledger fixtures only; not research findings or completed reading."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "econ-project-workflow/scripts/validate_learning_ledger.py"
TEMPLATE = ROOT / "econ-project-workflow/templates/learning-ledger.json"
SCHEMA = ROOT / "econ-project-workflow/templates/learning-ledger.schema.json"


def load_validator():
    spec = importlib.util.spec_from_file_location("learning_ledger", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def synthetic_source():
    return {
        "source_id": "s1", "source_type": "chapter", "title": "Synthetic chapter",
        "version": "fixture-v1", "read_at": "2026-01-01",
        "coverage": {"text": "partial", "images": "not_applicable", "scope": "Chapter 2, pp. 10-12 only"},
        "checks": [],
    }


def synthetic_lesson():
    return {
        "lesson_id": "l1", "statement": "Synthetic scoped claim, not a finding.",
        "status": "candidate", "source_ids": ["s1"],
        "evidence": [{"source_id": "s1", "locator": "p. 11, equation 2", "scope": "Chapter 2 only", "relation": "supports"}],
        "assumptions": [], "limitations": ["Synthetic fixture"], "target": None,
        "supersedes": [], "validation": {"level": "reading_only", "record": "Synthetic reading declaration"},
        "conflict_note": "",
    }


def synthetic_ledger():
    return {"schema_version": 1, "sources": [synthetic_source()], "lessons": []}


class LearningLedgerTests(unittest.TestCase):
    def test_cli_rejects_ambiguous_or_excessively_nested_json_cleanly(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "synthetic-invalid.json"
            for text in ('{"schema_version":2,"schema_version":1,"sources":[],"lessons":[]}', '[' * 2000 + '0' + ']' * 2000):
                with self.subTest(text_kind="duplicate" if text.startswith("{") else "deep"):
                    path.write_text(text, encoding="utf-8")
                    result = subprocess.run([sys.executable, str(SCRIPT), str(path)], text=True, capture_output=True, check=False)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn("ERROR:", result.stderr)
                    self.assertNotIn("Traceback", result.stderr)

    def test_complete_book_scope_is_not_rejected_for_text_only_descriptor(self):
        data = synthetic_ledger()
        source = data["sources"][0]
        source["source_type"] = "book"
        source["coverage"].update(text="complete", scope="Whole book, text only; images not applicable")
        self.assertEqual(load_validator().validate(data), [])

    def test_documentary_schema_matches_common_actual_instances(self):
        self.assertTrue(SCHEMA.is_file(), "documentary schema missing")
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["schema_version"]["const"], 1)
        validator = load_validator()
        definitions = schema["$defs"]
        self.assertEqual(definitions["source"]["properties"]["source_type"]["enum"], list(validator.SOURCE_TYPES))
        self.assertEqual(definitions["lesson"]["properties"]["status"]["enum"], list(validator.LESSON_STATUSES))
        self.assertEqual(definitions["validation"]["properties"]["level"]["enum"], list(validator.VALIDATION_LEVELS))
        for kind in validator.SOURCE_TYPES:
            data = synthetic_ledger()
            data["sources"][0]["source_type"] = kind
            data["sources"][0].update(url="https://example.org/home/fixture", authors=["Synthetic author"], edition="Fixture edition")
            data["lessons"] = [synthetic_lesson()]
            self.assertEqual(validator.validate(data), [])
            for name, instance in [("source", data["sources"][0]), ("lesson", data["lessons"][0])]:
                self.assertTrue(set(definitions[name]["required"]).issubset(instance))
                self.assertTrue(set(instance).issubset(definitions[name]["properties"]))
                self.assertFalse(definitions[name]["additionalProperties"])

    def test_cli_private_paths_help_and_clean_errors(self):
        def run(*args):
            return subprocess.run([sys.executable, str(SCRIPT), *args], text=True, capture_output=True, check=False)
        help_result = run("--help")
        self.assertEqual(help_result.returncode, 0)
        self.assertIn("Examples:", help_result.stdout)
        self.assertIn("declarations", help_result.stdout)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "private ledger.json"
            path.write_text(json.dumps(synthetic_ledger()), encoding="utf-8")
            before = path.read_bytes()
            result = run(str(path), "--root", str(ROOT))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(json.loads(result.stdout)["declarations_only"])
            self.assertEqual(path.read_bytes(), before)
            for text in ("{broken", '{"schema_version":1,"sources":[null],"lessons":[]}', '[]'):
                path.write_text(text, encoding="utf-8")
                result = run(str(path))
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("ERROR:", result.stderr)
                self.assertNotIn("Traceback", result.stdout + result.stderr)
            result = run(str(Path(directory) / "missing.json"))
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn("Traceback", result.stdout + result.stderr)

    def test_summary_counts_only_explicit_declarations_without_mutation(self):
        validator = load_validator()
        self.assertTrue(callable(getattr(validator, "summary", None)), "summary API missing")
        data = synthetic_ledger()
        for i, coverage in enumerate(("complete", "unread"), start=2):
            source = synthetic_source()
            source["source_id"] = f"s{i}"
            source["coverage"]["text"] = coverage
            data["sources"].append(source)
        data["sources"][0]["checks"] = [{"kind": "primary_source", "locator": "p. 11", "scope": "Chapter 2 only", "status": "blocked", "version": "fixture-v1"}]
        for i, status in enumerate(("candidate", "integrated", "needs_recheck", "superseded", "rejected")):
            lesson = synthetic_lesson()
            lesson.update(lesson_id=f"l{i}", status=status)
            if status == "integrated":
                lesson["target"] = "test-skill/references/test.md"
            data["lessons"].append(lesson)
        before = copy.deepcopy(data)
        result = validator.summary(data)
        self.assertTrue(result["declarations_only"])
        self.assertEqual((result["source_count"], result["lesson_count"]), (3, 5))
        self.assertEqual([result[f"body_{state}"] for state in ("complete", "partial", "unread")], [1, 1, 1])
        self.assertEqual(result["check_statuses"]["primary_source"]["blocked"], 1)
        self.assertEqual(result["validation_levels"]["reading_only"], 5)
        self.assertEqual(result["lesson_statuses"], dict.fromkeys(("candidate", "integrated", "needs_recheck", "superseded", "rejected"), 1))
        self.assertEqual(result["image_coverage"]["not_applicable"], 3)
        self.assertEqual(data, before)

    def test_integrated_rejects_null_target_with_and_without_root(self):
        validator = load_validator()
        data = synthetic_ledger()
        lesson = synthetic_lesson()
        lesson["status"] = "integrated"
        data["lessons"] = [lesson]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "synthetic-ledger.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            for optional_root in (None, root):
                with self.subTest(root=optional_root, interface="API"):
                    self.assertIn("l1.target: integrated requires a named target",
                                  validator.validate(data, root=optional_root))
                with self.subTest(root=optional_root, interface="CLI"):
                    args = [sys.executable, str(SCRIPT), str(path)]
                    if optional_root is not None:
                        args.extend(["--root", str(optional_root)])
                    result = subprocess.run(args, text=True, capture_output=True, check=False)
                    self.assertEqual(result.returncode, 1)
                    self.assertIn("ERROR: l1.target: integrated requires a named target", result.stderr)
                    self.assertNotIn("Traceback", result.stderr)

    def test_nullable_nonintegrated_targets_and_optional_integrated_existence(self):
        validator = load_validator()
        data = synthetic_ledger()
        lesson = synthetic_lesson()
        data["lessons"] = [lesson]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for status in ("candidate", "needs_recheck", "superseded", "rejected"):
                lesson["status"] = status
                for optional_root in (None, root):
                    with self.subTest(status=status, root=optional_root):
                        self.assertEqual(validator.validate(data, root=optional_root), [])
            lesson.update(status="integrated", target="test-skill/references/test.md")
            self.assertEqual(validator.validate(data), [])
            self.assertTrue(validator.validate(data, root=root))
            target = root / lesson["target"]
            target.parent.mkdir(parents=True)
            target.write_text("Synthetic fixture", encoding="utf-8")
            self.assertEqual(validator.validate(data, root=root), [])

    def test_documentary_schema_requires_nonnull_target_only_when_integrated(self):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        lesson = schema["$defs"]["lesson"]
        self.assertEqual(lesson.get("allOf"), [{
            "if": {"properties": {"status": {"const": "integrated"}}, "required": ["status"]},
            "then": {"properties": {"target": {"type": "string"}}},
        }])
        self.assertEqual(lesson["properties"]["target"], {"$ref": "#/$defs/target"})
        self.assertIn({"type": "null"}, schema["$defs"]["target"]["oneOf"])

    def test_targets_are_safe_and_optional_root_checks_symlink_containment(self):
        validator = load_validator()
        data = synthetic_ledger()
        lesson = synthetic_lesson()
        data["lessons"] = [lesson]
        for target in ["../other.md", "/tmp/file", "C:\\temp\\file", "skill\\references\\file.md",
                       "skill/references/../file.md", "skill/references//file.md", "skill/./SKILL.md",
                       "skill/unknown/file.md", "skill/references/", "https://example.org/home/guide"]:
            lesson["target"] = target
            with self.subTest(target=target):
                self.assertTrue(validator.validate(data))
        for target in ["test-skill/SKILL.md", "test-skill/references/test.md", "test-skill/scripts/test.py", "test-skill/templates/test.json"]:
            lesson["target"] = target
            self.assertEqual(validator.validate(data), [])
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            root = Path(directory)
            lesson["target"] = "test-skill/references/test.md"
            self.assertTrue(validator.validate(data, root=root))
            file = root / lesson["target"]
            file.parent.mkdir(parents=True)
            file.write_text("Synthetic fixture", encoding="utf-8")
            self.assertEqual(validator.validate(data, root=root), [])
            link = root / "test-skill/references/outside.md"
            outside_file = Path(outside) / "outside.md"
            outside_file.write_text("Synthetic external fixture", encoding="utf-8")
            link.symlink_to(outside_file)
            lesson["target"] = "test-skill/references/outside.md"
            self.assertTrue(validator.validate(data, root=root))
            self.assertTrue(validator.validate(data, root=root / "absent"))
        data["sources"][0]["url"] = "https://example.org/home/article"
        lesson["target"] = None
        self.assertEqual(validator.validate(data), [])

    def test_supersession_cycles_and_active_replacement_conflicts(self):
        validator = load_validator()
        data = synthetic_ledger()
        first, second = synthetic_lesson(), synthetic_lesson()
        second["lesson_id"] = "l2"
        first["supersedes"] = ["l1"]
        data["lessons"] = [first]
        self.assertTrue(validator.validate(data), "self supersession must fail")
        first["supersedes"] = ["l2"]
        second["supersedes"] = ["l1"]
        data["lessons"] = [first, second]
        self.assertTrue(validator.validate(data), "cycle must fail")
        second["supersedes"] = []
        first["status"] = "integrated"
        second["status"] = "integrated"
        first["target"] = "test-skill/references/test.md"
        second["target"] = "test-skill/references/test.md"
        first["conflict_note"] = "Synthetic resolution"
        self.assertTrue(validator.validate(data), "predecessor cannot remain active")
        second["status"] = "superseded"
        self.assertEqual(validator.validate(data), [])
        first["conflict_note"] = ""
        self.assertTrue(validator.validate(data), "replacement needs resolution note")
        first["supersedes"] = []
        first["evidence"].append(dict(first["evidence"][0], relation="contradicts"))
        self.assertTrue(validator.validate(data), "integrated conflicting evidence needs note")
        first["conflict_note"] = "Synthetic conditional distinction"
        self.assertEqual(validator.validate(data), [])

    def test_upgraded_levels_require_matching_completed_source_checks(self):
        validator = load_validator()
        for level, kind in [("primary_checked", "primary_source"), ("primary_checked", "documentation"),
                            ("numerically_checked", "calculation"), ("executed", "code_execution")]:
            data = synthetic_ledger()
            lesson = synthetic_lesson()
            lesson["validation"].update(level=level, code_version="fixture-code-v1", software_version="Python fixture-v1")
            data["lessons"] = [lesson]
            with self.subTest(level=level, kind=kind):
                self.assertTrue(validator.validate(data), "level cannot be upgraded without check")
                check = {"kind": kind, "locator": "p. 11, equation 2", "scope": "Chapter 2 only", "status": "complete", "version": "fixture-v1"}
                data["sources"][0]["checks"] = [check]
                self.assertEqual(validator.validate(data), [])
                for status in ("not_attempted", "partial", "blocked"):
                    check["status"] = status
                    self.assertTrue(validator.validate(data))
                check["status"] = "complete"
                check["scope"] = "Unrelated appendix"
                self.assertTrue(validator.validate(data))
                check["scope"] = "Chapter 2 only"
                data["sources"][0]["coverage"]["text"] = "unread"
                self.assertTrue(validator.validate(data), "candidate unread cannot claim upgraded check")
                data["sources"][0]["coverage"]["text"] = "partial"
                if level == "executed":
                    for field in ("code_version", "software_version"):
                        item = copy.deepcopy(data)
                        del item["lessons"][0]["validation"][field]
                        self.assertTrue(validator.validate(item))

    def test_integrated_requires_scoped_read_support_not_metadata(self):
        validator = load_validator()
        base = synthetic_ledger()
        lesson = synthetic_lesson()
        lesson["status"] = "integrated"
        lesson["target"] = "test-skill/references/test.md"
        base["lessons"] = [lesson]
        self.assertEqual(validator.validate(base), [])  # Partial reading can support a scoped lesson.
        changes = [("unread", "p. 11", "supports"), ("partial", "Synthetic chapter", "supports"),
                   ("partial", "title: Synthetic chapter", "supports"), ("partial", "DOI: 10.fake/id", "supports"),
                   ("partial", "p. 11", "context"), ("partial", "p. 11", "contradicts")]
        for coverage, locator, relation in changes:
            data = copy.deepcopy(base)
            data["sources"][0]["coverage"]["text"] = coverage
            data["lessons"][0]["evidence"][0].update(locator=locator, relation=relation)
            with self.subTest(coverage=coverage, locator=locator, relation=relation):
                self.assertTrue(validator.validate(data))
        data = copy.deepcopy(base)
        data["lessons"][0]["evidence"] = []
        self.assertTrue(validator.validate(data))
        data = copy.deepcopy(base)
        data["sources"][0]["coverage"]["text"] = "unread"
        data["lessons"][0]["status"] = "candidate"
        self.assertEqual(validator.validate(data), [])
        data = copy.deepcopy(base)
        data["sources"][0]["source_type"] = "book"
        data["sources"][0]["coverage"]["text"] = "complete"
        self.assertTrue(validator.validate(data), "selected chapter is not a complete book")

    def test_duplicate_and_missing_cross_references_are_rejected(self):
        validator = load_validator()
        base = synthetic_ledger()
        base["lessons"] = [synthetic_lesson()]
        cases = []
        data = copy.deepcopy(base)
        data["sources"].append(synthetic_source())
        cases.append(data)
        data = copy.deepcopy(base)
        data["lessons"].append(synthetic_lesson())
        cases.append(data)
        for field in ("source_ids", "supersedes"):
            for ids in (["missing"], ["s1", "s1"] if field == "source_ids" else ["l2", "l2"]):
                data = copy.deepcopy(base)
                data["lessons"][0][field] = ids
                cases.append(data)
        data = copy.deepcopy(base)
        data["lessons"][0]["evidence"][0]["source_id"] = "missing"
        cases.append(data)
        data = copy.deepcopy(base)
        extra = synthetic_source()
        extra["source_id"] = "s2"
        data["sources"].append(extra)
        data["lessons"][0]["evidence"][0]["source_id"] = "s2"
        cases.append(data)
        for data in cases:
            with self.subTest(data=data):
                self.assertTrue(validator.validate(data))

    def test_lesson_and_check_structure_rejects_malformed_fields(self):
        validator = load_validator()
        data = synthetic_ledger()
        data["lessons"] = [synthetic_lesson()]
        self.assertEqual(validator.validate(data), [])
        for field, value in [("lesson_id", []), ("statement", ""), ("status", "approved"),
                             ("source_ids", "s1"), ("assumptions", [None]), ("limitations", {}),
                             ("evidence", [None]), ("supersedes", 3), ("validation", []),
                             ("target", 3), ("conflict_note", None), ("unexpected", "x")]:
            item = copy.deepcopy(data)
            item["lessons"][0][field] = value
            with self.subTest(field=field):
                self.assertTrue(validator.validate(item))
        for field, value in [("source_id", 1), ("locator", ""), ("scope", ""), ("relation", "proves")]:
            item = copy.deepcopy(data)
            item["lessons"][0]["evidence"][0][field] = value
            with self.subTest(evidence=field):
                self.assertTrue(validator.validate(item))
        for field, value in [("level", "verified"), ("record", ""), ("code_version", None), ("software_version", "")]:
            item = copy.deepcopy(data)
            item["lessons"][0]["validation"][field] = value
            with self.subTest(validation=field):
                self.assertTrue(validator.validate(item))
        for value in [None, {}, {"kind": "magic", "locator": "p. 1", "scope": "test", "status": "complete", "version": "v1"},
                      {"kind": "calculation", "locator": "", "scope": 1, "status": "done", "version": None}]:
            item = copy.deepcopy(data)
            item["sources"][0]["checks"] = [value]
            with self.subTest(check=value):
                self.assertTrue(validator.validate(item))
        item = copy.deepcopy(data)
        item["lessons"] = [None]
        self.assertTrue(validator.validate(item))

    def test_source_structure_is_strict_and_safe_on_malformed_values(self):
        validator = load_validator()
        self.assertEqual(validator.validate(synthetic_ledger()), [])
        invalid = [None, [], {}, {"schema_version": True, "sources": [], "lessons": []}]
        for field, value in [("source_id", ""), ("source_type", "video"), ("title", 4),
                             ("version", None), ("read_at", "2026-02-30"),
                             ("read_at", "20260101"), ("coverage", []), ("checks", {}),
                             ("authors", "Not a list"), ("url", 5), ("edition", 1)]:
            item = synthetic_ledger()
            item["sources"][0][field] = value
            invalid.append(item)
        for value in [None, 42, "s1", []]:
            item = synthetic_ledger()
            item["sources"] = [value]
            invalid.append(item)
        for field, value in [("text", "skimmed"), ("images", "none"), ("scope", "")]:
            item = synthetic_ledger()
            item["sources"][0]["coverage"][field] = value
            invalid.append(item)
        for item in invalid:
            with self.subTest(item=item):
                self.assertTrue(validator.validate(item), repr(item))
        item = synthetic_ledger()
        item["sources"][0]["unexpected"] = True
        self.assertTrue(validator.validate(item))
        item = synthetic_ledger()
        del item["sources"][0]["read_at"]
        self.assertTrue(validator.validate(item))

    def test_empty_template_is_version_one_and_valid(self):
        self.assertTrue(SCRIPT.is_file(), "ledger validator is missing")
        data = json.loads(TEMPLATE.read_text(encoding="utf-8"))
        self.assertEqual(data, {"schema_version": 1, "sources": [], "lessons": []})
        self.assertEqual(load_validator().validate(data), [])


if __name__ == "__main__":
    unittest.main()
