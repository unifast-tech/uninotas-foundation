import json
import pathlib
import re
import subprocess
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "validate_closeout_diff.py"
FOUNDATION = pathlib.Path(__file__).resolve().parents[2]
ACTIVE = "todos/active/process/TODO-uninotas-canonical-foundation-transition.md"
COMPLETED = "todos/completed/process/TODO-uninotas-canonical-foundation-transition.md"
STATIC = ("artifacts/publication-manifest.txt", "artifacts/feature-briefs/uninotas-smart-notas-central.md", "todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md")

class CloseoutDiffTests(unittest.TestCase):
    def git(self, repo, *args): return subprocess.run(["git", "-C", str(repo), *args], text=True, capture_output=True, check=True)
    def repo(self):
        temp=tempfile.TemporaryDirectory(); self.addCleanup(temp.cleanup); repo=pathlib.Path(temp.name); self.git(repo,"init","-q"); self.git(repo,"config","user.email","test@example.invalid"); self.git(repo,"config","user.name","Test")
        todo=(FOUNDATION / ACTIVE).read_text(encoding="utf-8")
        # C0 is delivery-ready in this fixture: production validation must not
        # exempt the two real delivery-review criteria from its prerequisite.
        todo=todo.replace("- [ ] `VAL-04`", "- [x] `VAL-04`").replace("- [ ] `VAL-05`", "- [x] `VAL-05`")
        todo=re.sub(r"(\| `VAL-04` \|.*?\| local \| )completed( \|)", r"\1passed\2", todo)
        todo=re.sub(r"(\| `VAL-05` \|.*?\| local \| )planned( \|)", r"\1passed\2", todo)
        path=repo/ACTIVE; path.parent.mkdir(parents=True); path.write_text(todo)
        for relative in STATIC:
            path=repo/relative; path.parent.mkdir(parents=True,exist_ok=True); path.write_text(f"link {ACTIVE}\n")
        self.git(repo,"add","."); self.git(repo,"commit","-qm","c0"); return repo
    def candidate(self, repo, mutate=None, recovery=False):
        base_oid=self.git(repo,"rev-parse","HEAD").stdout.strip()
        source,destination=(COMPLETED,ACTIVE) if recovery else (ACTIVE,COMPLETED)
        original=repo/source; target=repo/destination; target.parent.mkdir(parents=True,exist_ok=True); text=original.read_text()
        if recovery:
            text=text.replace("**Lifecycle state:** `Completed — conditional Production-Ready candidate`", "**Lifecycle state:** `Active — blocked recovery`").replace("**Current delivery stage:** `Production-Ready`", "**Current delivery stage:** `Local-Implemented`").replace("**Qualifiers:** `Provisional`", "**Qualifiers:** `Blocked — external closeout verification failed`").replace("**Next exact step:** external C1 remote verification + semantic active scan handoff", "**Next exact step:** reconcile observed C1 failure and rerun atomic closeout").replace("**Work state:** `review`", "**Work state:** `blocked`").replace("**Why this state now:** implementation and primary validation complete; independent delivery audits and C0 publication remain.", "**Why this state now:** published C1 failed external activation").replace("**Exit condition:** all delivery reviews and guards green; C0 published and verified before atomic C1 formation.", "**Exit condition:** failure reconciled and exact closeout protocol green").replace("C1 conditional; external activation pending", "C1 external activation failed; C1R recovery in progress").replace("**Disposition:** `move-completed`", "**Disposition:** `blocked`").replace("**Disposition reason:** candidate C1 guards green; Production-Ready remains conditional on external handoff", "**Disposition reason:** published C1 failed external activation").replace("**Post-commit/push status:** `C0 verified; C1 external verification pending`", "**Post-commit/push status:** `FAILED_C1 observed; C1R recovery pending`").replace("**Next path/status action:** external C1 verification + active scan handoff", "**Next path/status action:** publish/verify C1R then reconcile blocker")
        else:
            text=text.replace("**Lifecycle state:** `Active — planning`", "**Lifecycle state:** `Completed — conditional Production-Ready candidate`").replace("**Current delivery stage:** `Local-Implemented`", "**Current delivery stage:** `Production-Ready`").replace("**Qualifiers:** `none`", "**Qualifiers:** `Provisional`").replace("**Next exact step:** validate final independent reviews, then promote C0 to main by CAS", "**Next exact step:** external C1 remote verification + semantic active scan handoff").replace("**Disposition:** `keep-active`", "**Disposition:** `move-completed`").replace("**Disposition reason:** implementation locally complete; independent delivery gates and C0 publication remain.", "**Disposition reason:** candidate C1 guards green; Production-Ready remains conditional on external handoff").replace("**Post-commit/push status:** `pending`", "**Post-commit/push status:** `C0 verified; C1 external verification pending`").replace("**Next path/status action:** finish independent reviews, publish/verify C0, then form atomic C1", "**Next path/status action:** external C1 verification + active scan handoff").replace("| Foundation UniNotas cutover | `main@1b8a5e9` | `n/a — main-only authority` | `n/a` | `origin/main@1b8a5e9` | R8V material review-baseline evidence only; not delivery promotion |", f"| Foundation UniNotas cutover | `main@{base_oid}` | `n/a — main-only authority` | `n/a` | `origin/main@{base_oid}` | C1 conditional; external activation pending |").replace("**C0 active implementation/genesis commit:** `pending delivery — persisted in C1 after observation`", f"**C0 active implementation/genesis commit:** `{base_oid}`").replace("**C0 remote verification:** `pending delivery — typed C0 promotion + C0_POST clean validator/active-path/exact-two-active evidence persisted externally and C0 facts persisted in C1`", f"**C0 remote verification:** `fresh remote/origin/main/base HEAD all observed as {base_oid}`")
        text=re.sub(r"^- \*\*Qualifiers:\*\*.*$","- **Qualifiers:** `Blocked`" if recovery else "- **Qualifiers:** `Provisional`",text,count=1,flags=re.M)
        if recovery: text += f"Failure-Tuple: failure_id=failure-001; failed_c1_oid={base_oid}; predicate=actual_remote_mismatch; observed=remote-tip-mismatch; recorded_at_utc=2026-09-26T00:00:00Z\nObserved-Failure: external_verification_failed\n"
        original.unlink(); target.write_text(text)
        for relative in STATIC:
            path=repo/relative; path.write_text(path.read_text().replace(source,destination))
        if mutate: mutate(repo,target)
        self.git(repo,"add","-A"); return self.git(repo,"write-tree").stdout.strip()
    def validate_candidate(self, repo, base, tree, mode="closeout", focused_reviewer=None):
        todo=COMPLETED if mode=="closeout" else ACTIVE
        base_oid=self.git(repo,"rev-parse",base).stdout.strip(); base_tree=self.git(repo,"rev-parse",base+"^{tree}").stdout.strip()
        implementation_tree=base_tree
        if mode=="recovery":
            text=self.git(repo,"show",f"{base_oid}:{COMPLETED}").stdout; c0=re.search(r"\*\*C0 active implementation/genesis commit:\*\* `([0-9a-f]{40})`",text).group(1); implementation_tree=self.git(repo,"rev-parse",c0+"^{tree}").stdout.strip()
        review_ids=("privacy-review-c0","architecture-adherence-c0","security-review-c0","test-quality-c0","final-review-c0","verification-debt-c0","triple-performance-c0","triple-test-quality-c0","triple-cutover-integrity-c0","performance-concurrency-c0")
        implementation=[{"consumer_id":identifier,"phase":"C0","candidate_tree_oid":implementation_tree,"exact_path_set":["implementation-content"],"reviewer_or_session":f"test-session-{identifier}","outcome":"no_material_findings","scope":"implementation_content"} for identifier in review_ids]
        phase="C1" if mode=="closeout" else "C1R"; focused_id="closeout-integrity-review-c1" if mode=="closeout" else "recovery-integrity-review-c1r"; delta=self.git(repo,"diff","--no-renames","--name-only",base_oid,tree).stdout.splitlines(); focused={"consumer_id":focused_id,"phase":phase,"candidate_tree_oid":tree,"exact_path_set":delta,"reviewer_or_session":focused_reviewer if focused_reviewer is not None else f"test-session-{focused_id}","outcome":"no_material_findings"}
        reviews=repo.parent/"implementation-reviews.json"; focus=repo.parent/"focused-review.json"; reviews.write_text(json.dumps(implementation)); focus.write_text(json.dumps(focused))
        return subprocess.run(["python3",str(SCRIPT),"--mode",mode,"--repo",str(repo),"--base",base,"--candidate-tree",tree,"--todo",todo,"--implementation-reviews",str(reviews),"--focused-review",str(focus)],text=True,capture_output=True)
    def test_closeout_pos_01_atomic_move_and_allowed_cells(self):
        repo=self.repo(); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo); result=self.validate_candidate(repo,base,tree)
        self.assertEqual(0,result.returncode,result.stderr); proof=json.loads(result.stdout); self.assertEqual("go",proof["outcome"]); self.assertEqual(sorted((*STATIC,ACTIVE,COMPLETED)),proof["exact_delta"])
    def test_closeout_rejects_non_visible_focused_reviewer_session(self):
        for reviewer in ("\u200b","\u034f","reviewer\nforged","a"*129):
            with self.subTest(reviewer=repr(reviewer)):
                repo=self.repo(); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo); result=self.validate_candidate(repo,base,tree,focused_reviewer=reviewer)
                self.assertEqual(2,result.returncode); self.assertIn("focused C1 review",result.stderr)

    def test_closeout_cli_rejects_duplicate_review_attestation_members(self):
        repo=self.repo(); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo); self.validate_candidate(repo,base,tree)
        reviews=repo.parent/"implementation-reviews.json"; focus=repo.parent/"focused-review.json"; reviews.write_text(reviews.read_text().replace('"phase": "C0"','"phase":"C0","phase":"C0"',1))
        result=subprocess.run(["python3",str(SCRIPT),"--repo",str(repo),"--base",base,"--candidate-tree",tree,"--todo",COMPLETED,"--implementation-reviews",str(reviews),"--focused-review",str(focus)],text=True,capture_output=True)
        self.assertEqual(2,result.returncode); self.assertIn("review attestation input is invalid",result.stderr)
    def test_closeout_neg_01_incomplete_todo(self):
        repo=self.repo(); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); (repo/ACTIVE).write_text((repo/ACTIVE).read_text().replace("- [x] `DOD-01`","- [ ] `DOD-01`",1)); self.git(repo,"add",ACTIVE); self.git(repo,"commit","-qm","incomplete"); tree=self.candidate(repo); result=self.validate_candidate(repo,"HEAD",tree); self.assertIn("completed path requires all repository-verifiable criteria complete",result.stderr)
    def test_closeout_neg_02_unexpected_sixth_path(self):
        repo=self.repo(); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo,lambda root,target:(root/"extra").write_text("x")); result=self.validate_candidate(repo,base,tree); self.assertIn("non-allowlisted",result.stderr)
    def test_closeout_neg_03_frozen_todo_change(self):
        repo=self.repo(); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo,lambda root,target:target.write_text(target.read_text().replace("MonitorDeNotas","Changed Foundation",1))); result=self.validate_candidate(repo,base,tree); self.assertIn("frozen contract content",result.stderr)
    def test_closeout_and_recovery_reject_standalone_state_literals_outside_typed_fields(self):
        cases=((False,"Completed — conditional Production-Ready candidate","frozen contract content"),(True,"Active — blocked recovery","closeout recovery may only restore lifecycle truth"))
        for recovery,literal,diagnostic in cases:
            with self.subTest(recovery=recovery):
                repo=self.repo(); base=self.git(repo,"rev-parse","HEAD").stdout.strip()
                if recovery: self.candidate(repo); self.git(repo,"commit","-qm","c1"); base=self.git(repo,"rev-parse","HEAD").stdout.strip()
                tree=self.candidate(repo,lambda root,target:target.write_text(target.read_text()+f"\n{literal}\n"),recovery)
                result=self.validate_candidate(repo,base,tree,"recovery" if recovery else "closeout"); self.assertEqual(2,result.returncode); self.assertIn(diagnostic,result.stderr)
    def test_closeout_neg_04_static_cell_change(self):
        repo=self.repo(); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo,lambda root,target:(root/STATIC[0]).write_text("other")); result=self.validate_candidate(repo,base,tree); self.assertIn("frozen promotion scope or threshold cell",result.stderr)
    def test_closeout_neg_05_prospective_oid(self):
        repo=self.repo(); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo,lambda root,target:target.write_text(target.read_text().replace("**Current delivery stage:** `Production-Ready`", "**Current delivery stage:** `Production-Ready` "+"a"*40, 1))); result=self.validate_candidate(repo,base,tree); self.assertIn("uncreated C1 OID",result.stderr)
    def test_closeout_neg_06_invalid_state_machine_value(self):
        repo=self.repo(); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo,lambda root,target:target.write_text(target.read_text().replace("**Current delivery stage:** `Production-Ready`","**Current delivery stage:** `invalid`",1))); result=self.validate_candidate(repo,base,tree); self.assertIn("non-contract stage",result.stderr)
    def test_closeout_neg_16_17_success_rejects_recovery_only_markers(self):
        markers=(
            "Failure-Tuple: failure_id=failure-001; failed_c1_oid="+("a"*40)+"; predicate=actual_remote_mismatch; observed=remote-tip-mismatch; recorded_at_utc=2026-09-26T00:00:00Z\n",
            "Observed-Failure: external_verification_failed\n",
        )
        for suffix in (markers[0],markers[1],"".join(markers)):
            with self.subTest(markers=suffix.count("\n")):
                repo=self.repo(); base=self.git(repo,"rev-parse","HEAD").stdout.strip()
                tree=self.candidate(repo,lambda _root,target:target.write_text(target.read_text()+"\n"+suffix))
                result=self.validate_candidate(repo,base,tree)
                self.assertEqual(2,result.returncode)
                self.assertIn("successful closeout cannot contain recovery-only failure markers",result.stderr)
    def test_closeout_neg_c0_source_state_rejects_stale_stage_or_next_action(self):
        mutations=(("**Current delivery stage:** `Local-Implemented`","**Current delivery stage:** `Pending`"),("**Next exact step:** validate final independent reviews, then promote C0 to main by CAS","**Next exact step:** executar implementação"))
        for old,new in mutations:
            with self.subTest(field=old):
                repo=self.repo(); path=repo/ACTIVE; path.write_text(path.read_text().replace(old,new,1)); self.git(repo,"add",ACTIVE); self.git(repo,"commit","-qm","stale C0 state"); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo); result=self.validate_candidate(repo,base,tree); self.assertEqual(2,result.returncode); self.assertIn("C0 source state is not delivery-ready",result.stderr)
    def test_closeout_neg_08_self_guard_dependency(self):
        repo=self.repo(); (repo/ACTIVE).write_text((repo/ACTIVE).read_text()+"Criterion: validate_closeout_diff\n"); self.git(repo,"add",ACTIVE); self.git(repo,"commit","-qm","self"); tree=self.candidate(repo); result=self.validate_candidate(repo,"HEAD",tree); self.assertIn("cannot require its own",result.stderr)
    def test_closeout_pos_04_failed_c1_recovery_to_active(self):
        repo=self.repo(); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); c1=self.candidate(repo); self.git(repo,"commit","-m","c1"); c1=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo,recovery=True); result=self.validate_candidate(repo,c1,tree,"recovery"); self.assertEqual(0,result.returncode,result.stderr); self.assertEqual("go",json.loads(result.stdout)["outcome"])
    def test_closeout_neg_09_failed_external_verification_requires_recovery(self):
        repo=self.repo(); self.candidate(repo); self.git(repo,"commit","-qm","c1"); c1=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo,lambda root,target:target.write_text(target.read_text().replace("Observed-Failure: external_verification_failed\n","")),True); result=self.validate_candidate(repo,c1,tree,"recovery"); self.assertIn("recovery requires exactly one failure tuple and observed-failure marker",result.stderr)
    def test_closeout_neg_12_invalid_recovery_tuple(self):
        repo=self.repo(); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); self.candidate(repo); self.git(repo,"commit","-qm","c1"); c1=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo,lambda root,target:target.write_text(target.read_text().replace("predicate=actual_remote_mismatch","predicate=untyped")),True); result=self.validate_candidate(repo,c1,tree,"recovery"); self.assertIn("invalid failure tuple",result.stderr)
    def test_closeout_neg_10_recovery_cannot_change_scope(self):
        repo=self.repo(); self.candidate(repo); self.git(repo,"commit","-qm","c1"); c1=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo,lambda root,target:target.write_text(target.read_text().replace("MonitorDeNotas","Changed Foundation",1)),True); result=self.validate_candidate(repo,c1,tree,"recovery"); self.assertIn("closeout recovery may only restore lifecycle truth and observed failure evidence",result.stderr)
    def test_closeout_neg_13_recovery_promotion_status_is_exact(self):
        def mutate(_root,target):
            text=target.read_text(); text=re.sub(r"(^\| Foundation UniNotas cutover \|.*\| )C1 external activation failed; C1R recovery in progress( \|$)", r"\1unexpected recovery status\2", text, count=1, flags=re.M); target.write_text(text)
        repo=self.repo(); self.candidate(repo); self.git(repo,"commit","-qm","c1"); c1=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo,mutate,True); result=self.validate_candidate(repo,c1,tree,"recovery"); self.assertIn("invalid failure tuple",result.stderr)
    def test_closeout_neg_14_recovery_preserves_c0_attestation(self):
        repo=self.repo(); self.candidate(repo); self.git(repo,"commit","-qm","c1"); c1=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.candidate(repo,lambda root,target:target.write_text(target.read_text().replace("fresh remote/origin/main/base HEAD all observed as", "changed C0 verification for")),True); result=self.validate_candidate(repo,c1,tree,"recovery"); self.assertIn("invalid failure tuple",result.stderr)
