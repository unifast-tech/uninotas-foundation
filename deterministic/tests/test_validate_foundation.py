import importlib.util
import json
import pathlib
import shutil
import os
import re
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "deterministic" / "validate_foundation.py")
EXPECTED_DELETE_PATHS = frozenset({
    "artifacts/analysis/leadshug-architecture-truth-and-legacy-boundaries-20260915.md", "artifacts/analysis/leadshug-executive-system-dossier-20260915.md", "artifacts/analysis/leadshug-system-analysis-20260915.md", "artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md", "artifacts/migration/claude-legacy-reconciliation-review.json", "artifacts/migration/claude-legacy-reconciliation-review.prompt.txt", "artifacts/migration/legacy-reconciliation-20260915.md", "artifacts/workspace-link-stabilization-20260915.md", "decisions/ST-01-foundation-lifecycle-decisions.md", "deterministic/.gitkeep", "modules/audit-and-history.md", "modules/identity-and-tenancy.md", "modules/inbox-and-conversations.md", "modules/integrations-and-channels.md", "policies/central_whatsapp_independent_legacy_policy.md", "policies/web_to_app_promotion_policy.md", "todos/active/features/TODO-leadshug-mode-specific-primary-and-secondary-color.md", "todos/active/features/TODO-leadshug-typebot-automation-integration.md", "todos/active/process/TODO-foundation-lifecycle-structural-validator.md", "todos/completed/features/TODO-delphi-shell-line-endings-and-cross-platform-validation.md", "todos/completed/features/TODO-leadshug-foundation-and-delphi-migration.md", "todos/completed/features/TODO-leadshug-identity-visual-screen-tests.md", "todos/completed/features/TODO-leadshug-initial-branding-and-unofficial-connection.md", "todos/completed/features/TODO-leadshug-post-onboarding-brand-settings.md", "todos/completed/features/TODO-leadshug-secondary-color-background-contract.md", "todos/completed/process/TODO-central-whatsapp-independent-legacy-policy.md", "todos/completed/process/TODO-ci-contract-and-migration-test-gates.md", "todos/completed/process/TODO-leadshug-architecture-truth-and-legacy-boundaries.md", "todos/completed/process/TODO-leadshug-authority-and-technology-documentation-rebase.md", "todos/completed/process/TODO-leadshug-executive-system-dossier.md", "todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md", "todos/completed/process/TODO-leadshug-legacy-authority-migration-and-retirement.md", "todos/completed/process/TODO-leadshug-system-analysis-and-modernization-plan.md", "todos/completed/process/TODO-leadshug-workspace-link-stabilization.md",
})

class ValidateFoundationTests(unittest.TestCase):
    def setUp(self): self.module = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(self.module)
    def tree(self):
        temp = tempfile.TemporaryDirectory(); root = pathlib.Path(temp.name) / "tree"
        shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__")); self.addCleanup(temp.cleanup); return root
    def errors(self, mutate):
        root = self.tree(); mutate(root); return self.module.validate(root)
    def manifest(self, root): return root / "artifacts/publication-manifest.txt"
    def add_manifest(self, root, path): self.manifest(root).write_text(self.manifest(root).read_text() + "\n" + path + "\n")
    def copy_manifest(self, source_root, destination_root):
        manifest = [line for line in (source_root / "artifacts/publication-manifest.txt").read_text().splitlines() if line and not line.startswith("#")]
        for relative in manifest:
            source, destination = source_root / relative, destination_root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination, follow_symlinks=False)
    def test_valid_active_tree(self): self.assertEqual([], self.module.validate(ROOT))
    def test_lifecycle_exactly_one_and_completed_simulation(self):
        self.assertTrue(any("exactly one" in x for x in self.errors(lambda r: ((r / self.module.COMPLETED_TODO).parent.mkdir(parents=True, exist_ok=True), shutil.copy2(r / self.module.ACTIVE_TODO, r / self.module.COMPLETED_TODO)))))
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
        def ledgered_active_claim(r, line):
            todo = r / self.module.ACTIVE_TODO
            todo.write_text(todo.read_text() + "\n## Active claim probe\n" + line + "\n")
            ledger = r / "deterministic/legacy_reference_exceptions.json"; rows = json.loads(ledger.read_text())
            rows.append({"path":self.module.ACTIVE_TODO,"term":"lead"+"shug","context_kind":"historical_migration_record","section":"Active claim probe","reason":"probe","owner":"test","lifecycle":"active_until_closeout_move","line_hashes":[self.module.normalized_line_hash(line)]})
            ledger.write_text(json.dumps(rows))
        probes = ("Lead"+"sHug is the current authority.", "Lead"+"sHug is the canonical architecture.", "Lead"+"sHug remains the source of truth.", "Lead"+"sHug é a autoridade atual.")
        for line in probes:
            errors = self.errors(lambda r, value=line: ledgered_active_claim(r, value))
            self.assertTrue(any("active legacy authority" in x for x in errors), line)
        self.assertFalse(self.module.term_occurs("evol"+"ution", "evol"+"ution_lifecycle.md"))
        self.assertTrue(self.module.term_occurs("evol"+"ution", "historical Evol"+"ution integration"))
        for suffix in ("-connector", ".backup", "/connector", "_connector"):
            self.assertTrue(self.module.term_occurs("evol"+"ution", "evol"+"ution_lifecycle" + suffix), suffix)
        for compound in ("Lead"+"shugFoundation is the current product.", "Lead"+"shug_Foundation is the current authority.", "Lead"+"shugFundação é o produto atual."):
            self.assertTrue(any("legacy" in x for x in self.errors(lambda r, value=compound: (r / "README.md").write_text(value))), compound)
        self.assertTrue(any("ledger" in x for x in self.errors(lambda r: (r / self.module.ACTIVE_TODO).write_text((r / self.module.ACTIVE_TODO).read_text().replace("LeadsHug", "LEADSHUG", 1)))))
    def test_delete_paths_are_exact_and_independent_of_manifest(self):
        self.assertEqual(EXPECTED_DELETE_PATHS, self.module.DELETE_PATHS)
        root, original_manifest = self.tree(), None
        original_manifest = self.manifest(root).read_text()
        for relative in self.module.DELETE_PATHS:
            target=root/relative; target.parent.mkdir(parents=True, exist_ok=True); target.write_text("safe"); self.add_manifest(root,relative)
            self.assertTrue(any("forbidden deleted path" in x for x in self.module.validate(root)), relative)
            target.unlink(); self.manifest(root).write_text(original_manifest)
    def test_publication_manifest_freezes_lifecycle_tree_and_order(self):
        def remove_keep_with_row(r, relative):
            (r / relative).unlink()
            lines = self.manifest(r).read_text().splitlines()
            self.manifest(r).write_text("\n".join(line for line in lines if line != relative) + "\n")
        for relative in (".gitattributes", "deterministic/tests/fixtures/valid-tree/README.md"):
            self.assertTrue(any("frozen lifecycle tree" in x for x in self.errors(lambda r, value=relative: remove_keep_with_row(r, value))), relative)
        self.assertTrue(any("uniquely" in x for x in self.errors(lambda r: self.manifest(r).write_text(self.manifest(r).read_text() + ".gitattributes\n"))))
    def test_external_symlink_is_rejected_before_and_after_manifest_copy(self):
        source = self.tree()
        external = pathlib.Path(tempfile.mkdtemp()) / "README.md"
        self.addCleanup(lambda: shutil.rmtree(external.parent, ignore_errors=True))
        external.write_bytes((source / "README.md").read_bytes())
        (source / "README.md").unlink()
        (source / "README.md").symlink_to(external)
        self.assertTrue(any("symlink forbidden" in error for error in self.module.validate(source)))
        destination_temp = tempfile.TemporaryDirectory(); self.addCleanup(destination_temp.cleanup)
        destination = pathlib.Path(destination_temp.name) / "archive"; destination.mkdir()
        self.copy_manifest(source, destination)
        self.assertTrue((destination / "README.md").is_symlink())
        self.assertTrue(any("symlink forbidden" in error for error in self.module.validate(destination)))
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
            for token in self.module.REQUIRED_CONTRACT_TOKENS.get(name, ()):
                self.assertTrue(any("contract semantic" in x for x in self.errors(lambda r,n=name,t=token: (r / "modules" / n).write_text((r / "modules" / n).read_text().replace(t, "removed-contract-semantic")))), (name, token))
                def move_outside_contract(r, n=name, t=token):
                    path = r / "modules" / n; text = path.read_text()
                    for section in self.module.REQUIRED_CONTRACT_SECTIONS[n]:
                        pattern = rf"(^## {re.escape(section)}\s*\n)(.*?)(?=^## |\Z)"
                        text = re.sub(pattern, lambda match: match.group(1) + match.group(2).replace(t, "moved-contract-semantic"), text, flags=re.M | re.S)
                    path.write_text(text + "\n## Regression Sink\n" + t + "\n")
                self.assertTrue(any("contract semantic" in x for x in self.errors(move_outside_contract)), (name, token, "outside"))
        def remove_route(r):
            path = r / "modules/events-and-classification.md"; text = path.read_text()
            path.write_text(re.sub(r"^\| `GET /eventos/resumo`.*\n", "", text, count=1, flags=re.M))
        self.assertTrue(any("route contract mismatch" in x for x in self.errors(remove_route)))
        def swap_route_statuses(r):
            path = r / "modules/identity-and-team.md"; lines = path.read_text().splitlines()
            for index, line in enumerate(lines):
                if line.startswith("| `POST /auth/login`"): lines[index] = line.replace("HTTP 200", "HTTP 201")
                if line.startswith("| `POST /usuarios`"): lines[index] = line.replace("HTTP 201", "HTTP 200")
            path.write_text("\n".join(lines) + "\n")
        self.assertTrue(any("route contract mismatch" in x for x in self.errors(swap_route_statuses)))
        def swap_route_columns(r):
            path = r / "modules/identity-and-team.md"; lines = path.read_text().splitlines()
            for index, line in enumerate(lines):
                if line.startswith("| `POST /auth/login`"):
                    cells = self.module.markdown_table_cells(line); cells[1], cells[2] = cells[2], cells[1]
                    lines[index] = "| " + " | ".join(cells) + " |"
            path.write_text("\n".join(lines) + "\n")
        self.assertTrue(any("route contract mismatch" in x for x in self.errors(swap_route_columns)))
        self.assertTrue(any("identity anchor" in x for x in self.errors(lambda r: (r / "README.md").write_text((r / "README.md").read_text().replace("# Monitor de Notas Foundation", "# Other Foundation", 1)))))
        self.assertTrue(any("identity heading" in x for x in self.errors(lambda r: (r / "README.md").write_text((r / "README.md").read_text() + "\n# Other Product Foundation\n"))))
        self.assertTrue(any("canonical identity claim" in x for x in self.errors(lambda r: (r / "decisions/monitor-de-notas-foundation-decisions.md").write_text((r / "decisions/monitor-de-notas-foundation-decisions.md").read_text() + "\nThe canonical product is Other Product.\n"))))
        owner = "project_constitution.md"; assertion = self.module.CANONICAL_ASSERTIONS[owner]
        self.assertTrue(any("ownership" in x for x in self.errors(lambda r: (r / owner).write_text((r / owner).read_text().replace(assertion, "Monitor de Notas writes `logs`; Routerfy reads `logs` only.")))))
        self.assertTrue(any("contradictory" in x for x in self.errors(lambda r: (r / "modules/events-and-classification.md").write_text((r / "modules/events-and-classification.md").read_text() + "\nMonitor de Notas owns logs.\n"))))
        self.assertTrue(any("contradictory" in x for x in self.errors(lambda r: (r / "modules/events-and-classification.md").write_text((r / "modules/events-and-classification.md").read_text() + "\nMonitor   de   Notas can write logs.\n"))))
        decision = "decisions/monitor-de-notas-foundation-decisions.md"
        self.assertTrue(any("decision table" in x for x in self.errors(lambda r: (r / decision).write_text((r / decision).read_text() + "\n| D-01 | conflicting | x |\n"))))
        self.assertTrue(any("decision table" in x for x in self.errors(lambda r: (r / decision).write_text((r / decision).read_text() + "\n| D-04 | conflicting | x |\n"))))
        self.assertTrue(any("decision table" in x for x in self.errors(lambda r: (r / decision).write_text((r / decision).read_text() + "\n|D-01|conflicting|x|\n"))))
        self.assertTrue(any("decision table" in x for x in self.errors(lambda r: (r / decision).write_text((r / decision).read_text() + "\n| D-04|Monitor de Notas owns logs.|x|\n"))))
        self.assertTrue(any("decision table" in x for x in self.errors(lambda r: (r / decision).write_text((r / decision).read_text().replace("Routerfy owns and writes the authoritative production `logs`; Monitor de Notas reads that external table only and writes only its application tables.", "Monitor de Notas owns `logs`.")))))
    def test_privacy_scans_every_persisted_surface(self):
        fragments=("eyJ"+"hbGciOiJIUzI1NiJ9"+".eyJzdWIiOiIxIn0"+".signature", "-----"+"BEGIN PRIVATE "+"KEY-----", "api"+"_key='abcdefghijk'", "API"+"_KEY=abcdefghijk", "api"+"-key: abcdefghijk", "- api"+"_key: abcdefghijk", "{\"api"+"_key\":\"abcdefghijk\"}", "{\"kind\":\"config\",\"api"+"_key\":\"abcdefghijk\"}", "[{\"api"+"_key\":\"abcdefghijk\"}]", "https://x.invalid/?to"+"ken=abcdefghijk", "Authorization: Bea"+"rer abcdefghijk", "DATABASE"+"_URL=postgres"+"ql://db_admin:"+"Sup3rValue@127.0.0.1/prod", "AK"+"IAIOSFODNN7EXAMPLE", "gh"+"p_"+("A"*36), "github"+"_pat_"+("A"*24), "sk"+"-proj-"+("A"*24), "AI"+"za"+("A"*35), "529"+".982.247-25", "111"+"444"+"777"+"35", "+55"+" 11 "+"99999"+"-9999", "+55"+" 11 "+"3333"+"-4444", "{\n  \"no"+"me\": \"Pessoa\",\n  \"documento\": \"redacted\",\n  \"telefone\": \"redacted\"\n}", "a"+"lice"+"@example.com")
        root = self.tree()
        for relative in ("README.md", "modules/events-and-classification.md", "policies/engineering_guardrails.md", "artifacts/README.md", self.module.ACTIVE_TODO, "local_packages.yaml", "artifacts/publication-manifest.txt", "deterministic/validate_foundation.py", "deterministic/legacy_reference_exceptions.json", "deterministic/tests/test_validate_foundation.py", "deterministic/tests/fixtures/valid-tree/README.md"):
            for content in fragments:
                path=root/relative; original=path.read_text(); path.write_text(original+"\n"+content); self.assertTrue(any("privacy" in x for x in self.module.validate(root)), (relative, content)); path.write_text(original)
    def test_legacy_destination_is_not_stripped(self):
        url = "https://example.invalid/lead" + "shug"
        markdown = chr(91) + "x" + chr(93) + chr(40) + url + chr(41)
        self.assertTrue(any("legacy" in x for x in self.errors(lambda r: (r / "README.md").write_text((r / "README.md").read_text() + "\n" + markdown + "\n"))))
    def test_clean_copy_commands_leave_no_bytecode(self):
        temp = tempfile.TemporaryDirectory(); self.addCleanup(temp.cleanup); root = pathlib.Path(temp.name) / "archive"; root.mkdir()
        self.copy_manifest(ROOT, root)
        env = {**os.environ, "FOUNDATION_CLEAN_COPY_CHILD":"1"}
        child_tests = [f"deterministic.tests.test_validate_foundation.ValidateFoundationTests.{name}" for name in dir(type(self)) if name.startswith("test_") and name != "test_clean_copy_commands_leave_no_bytecode"]
        suite = ["python3", "-B", "-m", "unittest", "-v", *child_tests]
        suite_result = subprocess.run(suite, cwd=root, env=env, capture_output=True, text=True)
        self.assertEqual(0, suite_result.returncode, suite_result.stdout + suite_result.stderr)
        validator_result = subprocess.run(["python3", "-B", "deterministic/validate_foundation.py", "--root", "."], cwd=root, env=env, capture_output=True, text=True)
        self.assertEqual(0, validator_result.returncode, validator_result.stdout + validator_result.stderr)
        self.assertFalse(list(root.rglob("__pycache__")))
