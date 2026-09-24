import importlib.util
import json
import pathlib
import shutil
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "deterministic" / "validate_foundation.py")

class ValidateFoundationTests(unittest.TestCase):
    def setUp(self): self.module = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(self.module)
    def tree(self):
        temp = tempfile.TemporaryDirectory(); root = pathlib.Path(temp.name) / "tree"
        shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__")); self.addCleanup(temp.cleanup); return root
    def errors(self, mutate):
        root = self.tree(); mutate(root); return self.module.validate(root)
    def manifest(self, root): return root / "artifacts/publication-manifest.txt"
    def add_manifest(self, root, path): self.manifest(root).write_text(self.manifest(root).read_text() + "\n" + path + "\n")
    def test_valid_active_tree(self): self.assertEqual([], self.module.validate(ROOT))
    def test_lifecycle_exactly_one_and_completed_simulation(self):
        self.assertTrue(any("exactly one" in x for x in self.errors(lambda r: shutil.copy2(r / self.module.ACTIVE_TODO, r / self.module.COMPLETED_TODO))))
        self.assertTrue(any("exactly one" in x for x in self.errors(lambda r: ((r / self.module.ACTIVE_TODO).unlink(), self.manifest(r).write_text(self.manifest(r).read_text().replace(self.module.ACTIVE_TODO, ""))))))
        root = self.tree(); completed = root / self.module.COMPLETED_TODO; completed.parent.mkdir(parents=True, exist_ok=True); shutil.move(root / self.module.ACTIVE_TODO, completed)
        ledger = root / "deterministic/legacy_reference_exceptions.json"; data = json.loads(ledger.read_text())
        for row in data: row["path"], row["lifecycle"] = self.module.COMPLETED_TODO, "historical"
        ledger.write_text(json.dumps(data)); self.manifest(root).write_text(self.manifest(root).read_text().replace(self.module.ACTIVE_TODO, self.module.COMPLETED_TODO)); self.assertEqual([], self.module.validate(root))
    def test_ledger_section_lifecycle_and_required_fields(self):
        for key, value in (("section", "wrong"), ("lifecycle", "historical"), ("owner", ""), ("reason", "")):
            def mutate(r, k=key, v=value):
                p=r/"deterministic/legacy_reference_exceptions.json"; data=json.loads(p.read_text()); data[0][k]=v; p.write_text(json.dumps(data))
            self.assertTrue(any("ledger" in x for x in self.errors(mutate)))
        def unused(r):
            p=r/"deterministic/legacy_reference_exceptions.json"; data=json.loads(p.read_text()); data.append({**data[0], "section":"Unused"}); p.write_text(json.dumps(data))
        self.assertTrue(any("ledger" in x for x in self.errors(unused)))
        self.assertTrue(any("legacy" in x for x in self.errors(lambda r: (r / "README.md").write_text("lead" + "shug"))))
        self.assertTrue(any("legacy" in x for x in self.errors(lambda r: (r / "project_mandate.md").write_text("evol" + "ution"))))
        self.assertTrue(any("ledger" in x for x in self.errors(lambda r: (r / self.module.ACTIVE_TODO).write_text((r / self.module.ACTIVE_TODO).read_text() + "\n## Unlisted historical statement\nLead" + "sHug\n"))))
        self.assertTrue(any("ledger" in x for x in self.errors(lambda r: (r / self.module.ACTIVE_TODO).write_text((r / self.module.ACTIVE_TODO).read_text().replace("Baileys.\n", "Baileys.\nLead" + "sHug is the current authority.\n", 1)))))
    def test_delete_paths_are_exact_and_independent_of_manifest(self):
        root, original_manifest = self.tree(), None
        original_manifest = self.manifest(root).read_text()
        for relative in self.module.DELETE_PATHS:
            target=root/relative; target.parent.mkdir(parents=True, exist_ok=True); target.write_text("safe"); self.add_manifest(root,relative)
            self.assertTrue(any("forbidden deleted path" in x for x in self.module.validate(root)), relative)
            target.unlink(); self.manifest(root).write_text(original_manifest)
    def test_identity_scope_and_module_contracts(self):
        root = self.tree()
        for owner, tokens in self.module.IDENTITY.items():
            if not (ROOT / owner).is_file(): continue
            for token in tokens:
                path=root/owner; original=path.read_text(); path.write_text(original.replace(token,"")); self.assertTrue(any("identity" in x for x in self.module.validate(root)), (owner, token)); path.write_text(original)
        def scope_mutation(old, new):
            return lambda r: (r / "policies/scope_subscope_governance.md").write_text((r / "policies/scope_subscope_governance.md").read_text().replace(old, new, 1))
        self.assertTrue(any("scope policy" in x for x in self.errors(scope_mutation('"subscopes":[', '"subscopes":["extra",'))))
        self.assertTrue(any("scope policy" in x for x in self.errors(scope_mutation('"runtime-and-deployment",', ''))))
        self.assertTrue(any("scope policy" in x for x in self.errors(scope_mutation("monitor-de-notas", "other-scope"))))
        self.assertTrue(any("scope policy" in x for x in self.errors(scope_mutation("paced_technical_adapter", "business_adapter"))))
        self.assertTrue(any("scope policy" in x for x in self.errors(scope_mutation("false}", "true}"))))
        self.assertTrue(any("scope/subscope" in x for x in self.errors(lambda r: (r / "modules/events-and-classification.md").write_text((r / "modules/events-and-classification.md").read_text().replace("`events-and-classification`", "`other`")))))
        for name, sections in self.module.REQUIRED_CONTRACT_SECTIONS.items():
            for section in sections:
                self.assertTrue(any("contract section" in x for x in self.errors(lambda r,n=name,s=section: (r / "modules" / n).write_text((r / "modules" / n).read_text().replace("## " + s, "## Missing")))) , (name, section))
        self.assertTrue(any("identity anchor" in x for x in self.errors(lambda r: (r / "README.md").write_text((r / "README.md").read_text().replace("# Monitor de Notas Foundation", "# Other Foundation", 1)))))
        owner = "modules/events-and-classification.md"; assertion = self.module.CANONICAL_ASSERTIONS[owner]
        self.assertTrue(any("ownership" in x for x in self.errors(lambda r: (r / owner).write_text((r / owner).read_text().replace(assertion, "Monitor de Notas writes `logs`; Routerfy reads `logs` only.")))))
    def test_privacy_scans_every_persisted_surface(self):
        fragments=("eyJ"+"hbGciOiJIUzI1NiJ9"+".eyJzdWIiOiIxIn0"+".signature", "-----"+"BEGIN PRIVATE "+"KEY-----", "api"+"_key='abcdefghijk'", "API"+"_KEY=abcdefghijk", "api"+"-key: abcdefghijk", "{\"api"+"_key\":\"abcdefghijk\"}", "a"+"lice"+"@example.com")
        root = self.tree()
        for relative in ("deterministic/validate_foundation.py", "deterministic/legacy_reference_exceptions.json", "deterministic/tests/test_validate_foundation.py", "deterministic/tests/fixtures/valid-tree/README.md"):
            for content in fragments:
                path=root/relative; original=path.read_text(); path.write_text(original+"\n"+content); self.assertTrue(any("privacy" in x for x in self.module.validate(root)), (relative, content)); path.write_text(original)
    def test_legacy_destination_is_not_stripped(self):
        url = "https://example.invalid/lead" + "shug"
        markdown = chr(91) + "x" + chr(93) + chr(40) + url + chr(41)
        self.assertTrue(any("legacy" in x for x in self.errors(lambda r: (r / "README.md").write_text((r / "README.md").read_text() + "\n" + markdown + "\n"))))
