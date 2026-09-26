import importlib.util
import json
import pathlib
import re
import shutil
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "deterministic" / "validate_foundation.py")


class FoundationTreeContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = importlib.util.module_from_spec(SPEC)
        SPEC.loader.exec_module(cls.module)
        cls.module.reset_full_tree_scan_count()

    def tree(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        root = pathlib.Path(temporary.name) / "foundation"
        shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__", "artifacts/tmp"))
        subprocess.run(["git", "-C", str(root), "init", "-q"], check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.email", "test@example.invalid"], check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.name", "Test"], check=True)
        subprocess.run(["git", "-C", str(root), "add", "."], check=True)
        subprocess.run(["git", "-C", str(root), "commit", "-qm", "C0 bootstrap fixture"], check=True)
        return root

    def scan(self, root):
        errors = self.module.validate(root)
        self.assertLessEqual(self.module.FULL_TREE_SCAN_COUNT, 3)
        return errors

    def complete_c1(self, root):
        active = "todos/active/process/TODO-uninotas-canonical-foundation-transition.md"
        completed = "todos/completed/process/TODO-uninotas-canonical-foundation-transition.md"
        c0 = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], text=True, capture_output=True, check=True).stdout.strip()
        source, destination = root / active, root / completed
        destination.parent.mkdir(parents=True, exist_ok=True)
        text = source.read_text(encoding="utf-8").replace(
            "**C0 active implementation/genesis commit:** `pending delivery — persisted in C1 after observation`",
            f"**C0 active implementation/genesis commit:** `{c0}`",
        )
        source.unlink(); destination.write_text(text, encoding="utf-8")
        for relative in (
            "artifacts/publication-manifest.txt",
            "artifacts/feature-briefs/uninotas-smart-notas-central.md",
            "todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md",
        ):
            path = root / relative
            path.write_text(path.read_text(encoding="utf-8").replace(active, completed), encoding="utf-8")
        subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(root), "commit", "-qm", "C1 completed fixture"], check=True)
        c1 = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], text=True, capture_output=True, check=True).stdout.strip()
        return c0, c1, destination

    def publication_tree(self, root):
        entries = self.module.repository_entries(root)
        return {path.relative_to(root).as_posix(): path for path in entries if path.is_file() and not path.is_symlink()}

    @staticmethod
    def valid_cnpj():
        digits = [1, 1, 4, 4, 4, 7, 7, 7, 0, 0, 0, 1]
        for weights in ((5,4,3,2,9,8,7,6,5,4,3,2), (6,5,4,3,2,9,8,7,6,5,4,3,2)):
            remainder = sum(value * weight for value, weight in zip(digits, weights)) % 11
            digits.append(0 if remainder < 2 else 11 - remainder)
        return "".join(map(str, digits))

    def test_manifest_matches_published_tree(self):
        root = self.tree(); self.complete_c1(root); (root / "unmanifested.md").write_text("publication probe\n", encoding="utf-8")
        errors=self.scan(root)
        self.assertIn("publication manifest must uniquely and exactly match publication tree", errors)  # GUARD-PUB-01
        self.assertNotIn("recorded LEDGER_GENESIS differs from earliest first-parent ledger introduction commit", errors)
        self.assertNotIn("ledger genesis must be recorded after the clean C0 bootstrap commit", errors)

    def test_c1_ledger_genesis_binding_rejects_lifecycle_mutations(self):
        pending="pending delivery — persisted in C1 after observation"
        cases=(
            ("descendant",lambda text,c0,c1:text.replace(f"`{c0}`",f"`{c1}`",1),"recorded LEDGER_GENESIS differs from earliest first-parent ledger introduction commit"),
            ("pending",lambda text,c0,c1:text.replace(f"`{c0}`",f"`{pending}`",1),"ledger genesis must be recorded after the clean C0 bootstrap commit"),
            ("missing",lambda text,c0,c1:re.sub(r"^- \*\*C0 active implementation/genesis commit:\*\*.*\n","",text,count=1,flags=re.M),"canonical LEDGER_GENESIS field must occur exactly once"),
            ("malformed",lambda text,c0,c1:text.replace(f"`{c0}`","`not-an-oid`",1),"canonical LEDGER_GENESIS must be pending bootstrap or lowercase 40-hex OID"),
            ("duplicate",lambda text,c0,c1:text.replace(f"- **C0 active implementation/genesis commit:** `{c0}`",f"- **C0 active implementation/genesis commit:** `{c0}`\n- **C0 active implementation/genesis commit:** `{c1}`",1),"canonical LEDGER_GENESIS field must occur exactly once"),
        )
        for name,mutate,diagnostic in cases:
            with self.subTest(case=name):
                root=self.tree(); c0,c1,todo=self.complete_c1(root); todo.write_text(mutate(todo.read_text(encoding="utf-8"),c0,c1),encoding="utf-8")
                tree=self.publication_tree(root); identities=json.loads((root/"deterministic/capability_identity_ledger.json").read_text(encoding="utf-8"))["identities"]
                self.assertIn(diagnostic,self.module.repository_ledger_history_errors(root,tree,"todos/completed/process/TODO-uninotas-canonical-foundation-transition.md",identities))
        root=self.tree(); _c0,_c1,completed=self.complete_c1(root); active=root/"todos/active/process/TODO-uninotas-canonical-foundation-transition.md"; active.parent.mkdir(parents=True,exist_ok=True); active.write_text(completed.read_text(encoding="utf-8"),encoding="utf-8")
        binding,errors=self.module.lifecycle_genesis_binding(self.publication_tree(root),"todos/completed/process/TODO-uninotas-canonical-foundation-transition.md")
        self.assertIsNone(binding); self.assertIn("exactly one canonical lifecycle TODO path may publish LEDGER_GENESIS",errors)

    def test_symlink_and_legacy_contracts(self):
        root = self.tree(); (root / "linked.md").symlink_to("README.md")
        (root / "README.md").write_text("# Wrong Foundation\nLead" + "sHug\n", encoding="utf-8")
        policy = root / "policies/scope_subscope_governance.md"
        policy.write_text(policy.read_text(encoding="utf-8").replace('"business_tenancy":false', '"business_tenancy":true', 1), encoding="utf-8")
        errors = self.scan(root)
        self.assertIn("symlink forbidden in publication tree: linked.md", errors)  # GUARD-SYMLINK-01
        self.assertIn("legacy authority/reference in README.md", errors)  # GUARD-LEGACY-01
        self.assertIn("canonical identity heading mismatch: README.md", errors)  # GUARD-ID-01
        self.assertIn("scope policy mismatch", errors)  # GUARD-TENANCY-01

    def test_registry_composes_with_module_files(self):
        root = self.tree(); target = root / "modules/fiscal-notes-and-documents.md"
        policy_path = root / "policies/scope_subscope_governance.md"
        policy = json.loads(re.search(r"```json\s*(\{.*?\})\s*```", policy_path.read_text(encoding="utf-8"), re.S).group(1))
        ledger = json.loads((root / "deterministic/capability_identity_ledger.json").read_text(encoding="utf-8"))
        self.assertEqual([], self.module.policy_registry_errors(policy, ledger, {"modules/" + path.name for path in (root / "modules").glob("*.md") if path.name != "README.md"}))
        evolved=json.loads(json.dumps(policy)); evolved["subscopes"].append("future-module"); evolved["subscopes"].sort(); evolved["modules"].append({"module_id":"future-module","path":"modules/future-module.md","runtime_authority_state":"target_planned","owned_capabilities":[],"planned_capabilities":["future_module_read"]}); evolved["module_catalog"].append({"module_id":"future-module","path":"modules/future-module.md","catalog_state":"active"}); evolved["capability_transitions"].append({"transition_id":"future-module-read-001","capability_id":"future_module_read","sequence":1,"origin":"new","transition_state":"planned","predecessor":None,"successor":"future-module"})
        dynamic=root/"dynamic-policy.md"; dynamic.write_text("```json\n"+json.dumps(evolved,separators=(",",":"))+"\n```\n",encoding="utf-8"); dynamic_errors=[]; self.assertEqual(evolved,self.module.scope_policy({"policies/scope_subscope_governance.md":dynamic},dynamic_errors)); self.assertEqual([],dynamic_errors); dynamic.unlink()
        fiscal=next(row for row in policy["modules"] if row["module_id"]=="fiscal-notes-and-documents"); fiscal["planned_capabilities"].append("future_read")
        policy["capability_transitions"].append({"transition_id":"future-read-001","capability_id":"future_read","sequence":1,"origin":"new","transition_state":"planned","predecessor":None,"successor":"fiscal-notes-and-documents"})
        ledger["identities"].append({"capability_id":"future_read","origin":"new","origin_transition_id":"future-read-001"})
        policy_text=policy_path.read_text(encoding="utf-8"); policy_path.write_text(re.sub(r"```json\s*\{.*?\}\s*```","```json\n"+json.dumps(policy,separators=(",",":"))+"\n```",policy_text,count=1,flags=re.S),encoding="utf-8")
        ledger_path = root / "deterministic/capability_identity_ledger.json"; ledger_path.write_text(json.dumps(ledger),encoding="utf-8")
        self.assertEqual([], self.module.policy_registry_errors(policy,ledger,{"modules/" + path.name for path in (root / "modules").glob("*.md") if path.name != "README.md"}))
        operational=next(row for row in policy["modules"] if row["module_id"]=="operational-cases"); operational["planned_capabilities"].remove("operational_workflow")
        policy_text=policy_path.read_text(encoding="utf-8"); policy_path.write_text(re.sub(r"```json\s*\{.*?\}\s*```","```json\n"+json.dumps(policy,separators=(",",":"))+"\n```",policy_text,count=1,flags=re.S),encoding="utf-8")
        target.write_text(target.read_text(encoding="utf-8").replace("`fiscal_document_read`", "`wrong_capability`", 1), encoding="utf-8")
        policy_path.write_text(policy_path.read_text(encoding="utf-8").replace('"runtime_authority_state":"target_planned"', '"runtime_authority_state":"current_runtime"', 1), encoding="utf-8")
        policy_path.write_text(policy_path.read_text(encoding="utf-8").replace('"catalog_state":"active"', '"catalog_state":"unknown"', 1).replace('"transition_state":"planned"', '"transition_state":"unknown"', 1), encoding="utf-8")
        policy_path.write_text(policy_path.read_text(encoding="utf-8").replace("Unifast and Prosperar are `FiscalIssuerContext` values, not tenants.", "Unifast and Prosperar are tenants.", 1), encoding="utf-8")
        constitution = root / "project_constitution.md"
        constitution.write_text(constitution.read_text(encoding="utf-8").replace("Namespaces: nestjs, react, vite, postgresql, prisma, docker, railway", "Namespaces: nestjs, react, postgresql, prisma, docker, railway", 1).replace("Smart Notas is the target-planned source of truth for fiscal notes and documents.", "PostgreSQL is the source of truth for fiscal notes and documents.", 1), encoding="utf-8")
        domain = root / "domain_entities.md"; domain.write_text(domain.read_text(encoding="utf-8")+"\nRouterfy remains owner of persisted source rows.\n",encoding="utf-8")
        privacy = root / "artifacts/README.md"
        placeholder = "smart_notas_unifast_token: <redacted>\nprovider_id: https://example.invalid/safe\ndocument_url: https://example.invalid/document\n"
        self.assertIsNone(self.module.private_context_diagnostic(placeholder))
        privacy.write_text(privacy.read_text(encoding="utf-8") + "\n" + placeholder + f"smart_notas_unifast_cnpj: {self.valid_cnpj()}\nprovider_id: synthetic-provider-901\ndocument_url: https://documents.invalid/danfe/901\nsmart_notas_unifast_token: synthetic-token-901\n", encoding="utf-8")
        nested_tmp=root/"artifacts/analysis/tmp/leak.md"; nested_tmp.parent.mkdir(parents=True,exist_ok=True); nested_tmp.write_text("authorization: bearer "+"nested-secret-value-901\n",encoding="utf-8")
        tracked_tmp=root/"artifacts/tmp/forced.md"; tracked_tmp.parent.mkdir(parents=True,exist_ok=True); tracked_tmp.write_text("forced tracked transient\n",encoding="utf-8"); subprocess.run(["git","-C",str(root),"add","-f",str(tracked_tmp.relative_to(root))],check=True)
        privacy_probe_paths=("deterministic/validate_foundation.py","deterministic/tests/test_privacy_predicate.py","deterministic/tests/test_closeout_handoff.py")
        for relative in privacy_probe_paths:
            probe_target=root/relative; probe_target.write_text(probe_target.read_text(encoding="utf-8")+"\n# injected probe\n"+"authorization: bearer "+"fixture-secret-value-901\n",encoding="utf-8")
        bytecode=root/"deterministic/__pycache__/probe.pyc"; bytecode.parent.mkdir(); bytecode.write_bytes(b"synthetic bytecode")
        todo = root / "todos/active/process/TODO-uninotas-canonical-foundation-transition.md"
        todo.write_text(todo.read_text(encoding="utf-8") + "\n- **C0 active implementation/genesis commit:** `pending delivery — persisted in C1 after observation`\n", encoding="utf-8")
        errors = self.scan(root)
        self.assertIn("module metadata does not match scope registry: fiscal-notes-and-documents.md", errors)
        self.assertIn("current_runtime module must own at least one capability", errors)
        self.assertIn("module catalog state is invalid", errors)
        self.assertIn("capability transition state is invalid", errors)
        self.assertIn("canonical identity mismatch: project_constitution.md", errors)
        self.assertIn("canonical ownership mismatch: project_constitution.md", errors)
        self.assertIn("canonical fiscal context mismatch: policies/scope_subscope_governance.md", errors)
        self.assertIn("canonical target owner mismatch: operational-cases", errors)
        self.assertIn("retired Routerfy log ownership claim in domain_entities.md", errors)
        self.assertNotIn("capability identity seed projection mismatch", errors)
        self.assertNotIn("origin new transition requires exactly one identity ledger record", errors)
        self.assertIn("privacy pattern in artifacts/README.md: valid CNPJ value", errors)
        self.assertIn("privacy pattern in artifacts/README.md: concrete provider identifier context", errors)
        self.assertIn("privacy pattern in artifacts/README.md: captured document URL context", errors)
        self.assertIn("privacy pattern in artifacts/README.md: token credential", errors)
        self.assertIn("privacy pattern in artifacts/analysis/tmp/leak.md",errors)
        self.assertIn("tracked file forbidden under artifacts/tmp",errors)
        for relative in privacy_probe_paths:
            self.assertTrue(any(error.startswith(f"privacy pattern in {relative}") for error in errors),relative)
        self.assertIn("publication manifest must uniquely and exactly match publication tree",errors)
        self.assertIn("canonical LEDGER_GENESIS field must occur exactly once", errors)
        decisions = (root / "decisions/uninotas-foundation-decisions.md").read_text(encoding="utf-8")
        self.assertIn("D-07", decisions)
        result = subprocess.run(["python3", "-B", str(ROOT / "deterministic" / "validate_foundation.py"), "--root", str(ROOT)], text=True, capture_output=True)
        self.assertEqual(0, result.returncode, result.stderr)
