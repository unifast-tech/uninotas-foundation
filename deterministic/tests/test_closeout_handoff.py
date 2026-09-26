import json
import importlib.util
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest


SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "closeout_handoff.py"
SPEC = importlib.util.spec_from_file_location("handoff", SCRIPT)
FOUNDATION = pathlib.Path(__file__).resolve().parents[2]
DELPHI = FOUNDATION.parent / "delphi-ai"


class CloseoutHandoffTests(unittest.TestCase):
    def handoff_module(self): module=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(module); return module
    def production_fixture(self):
        c0="a"*40; c1="b"*40; tree0="c"*40; tree1="d"*40; parent="0"*40
        record=lambda commit,tree,parent_oid,delta:{"commit_oid":commit,"candidate_tree_oid":tree,"commit_tree_oid":tree,"tree_equal":True,"parent_oid":parent_oid,"delivery_scope_set":["delivery"],"phase_commit_delta_set":delta}
        promotion=lambda expected,commit:{"fresh_pre_push_oid":expected,"expected_lease_oid":expected,"lease_result":"success","promotion_observation":"fresh_pre_push","parent_and_fast_forward":True,"post_push_remote_main_oid":commit,"local_head_oid":commit,"local_tracking_oid":commit}
        active=["todos/active/process/TODO-uninotas-canonical-foundation-transition.md","todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md"]
        return {"schema":"uninotas-closeout-handoff-v1","handoff_kind":"production","c0":record(c0,tree0,parent,["delivery"]),"c1":record(c1,tree1,c0,["closeout"]),"proof_bridge":{"validator":"validate_closeout_diff.py","base_commit_oid":c0,"base_tree_oid":tree0,"candidate_tree_oid":tree1,"exact_delta_set":["closeout"],"outcome":"go"},"consumer_bindings":self.c0_bindings()+self.c0post_bindings()+self.c1_bindings(),"remote_promotions":{"c0":promotion(parent,c0),"c1":promotion(c0,c1)},"c0_post_verify":{"head_oid":c0,"commit_tree_oid":tree0,"remote_main_oid":c0,"checkout_clean":True,"foundation_validator":"go","active_path_state":"active","active_todo_count":2,"active_paths":active},"post_c1_active_scan":{"scanned_head_oid":c1,"outcome":"go","todo_count":1,"active_paths":[active[1]],"stale_transition_path":False},"actual_remote_main_oid":c1,"production_ready_effective":True,"recovery_effective":False}
    def c0_bindings(self):
        go=("foundation-validator-c0","semantic-suite-c0","foundation-suite-c0","change-set-suite-c0","closeout-handoff-suite-c0","paced-readiness-c0","diff-expectation-c0","profile-scope-c0","todo-authority-c0","todo-completion-c0")
        review=("privacy-review-c0","architecture-adherence-c0","security-review-c0","test-quality-c0","final-review-c0","verification-debt-c0","triple-performance-c0","triple-test-quality-c0","triple-cutover-integrity-c0","performance-concurrency-c0")
        return [{"consumer_id":identifier,"phase":"C0","class":"worktree-proxy","scope":"implementation_content","binding_subject":"C0_CANDIDATE_TREE","change_scope_source":"DELIVERY_SCOPE_SET","outcome":"go"} for identifier in go]+[{"consumer_id":identifier,"phase":"C0","class":"implementation-human-review","scope":"implementation_content","binding_subject":"C0_CANDIDATE_TREE","change_scope_source":"DELIVERY_SCOPE_SET","outcome":"no_material_findings"} for identifier in review]
    def c1_bindings(self):
        ids=("closeout-proof-bridge-c1","todo-structure-c1","foundation-validator-c1","diff-expectation-c1","delivery-path-set-c1","lifecycle-path-set-c1","status-delivery-c1","status-lifecycle-c1","profile-scope-c1","diff-check-c1","todo-authority-c1","todo-completion-c1","todo-closeout-c1","closeout-integrity-review-c1")
        delivery={"diff-expectation-c1","delivery-path-set-c1","status-delivery-c1","profile-scope-c1","diff-check-c1"}; native={"closeout-proof-bridge-c1","delivery-path-set-c1","lifecycle-path-set-c1"}
        return [{"consumer_id":identifier,"phase":"C1","class":"tree-native" if identifier in native else "closeout-human-review" if identifier=="closeout-integrity-review-c1" else "worktree-proxy","scope":"closeout_transform","binding_subject":"C1_CANDIDATE_TREE","change_scope_source":"DELIVERY_SCOPE_SET" if identifier in delivery else "PHASE_COMMIT_DELTA_SET","outcome":"no_material_findings" if identifier=="closeout-integrity-review-c1" else "go"} for identifier in ids]
    def c1r_bindings(self):
        ids=("recovery-proof-bridge-c1r","todo-structure-c1r","foundation-validator-c1r","diff-expectation-c1r","delivery-path-set-c1r","lifecycle-path-set-c1r","status-delivery-c1r","status-lifecycle-c1r","profile-scope-c1r","diff-check-c1r","todo-authority-c1r","todo-completion-c1r","todo-closeout-c1r","recovery-integrity-review-c1r")
        delivery={"diff-expectation-c1r","delivery-path-set-c1r","status-delivery-c1r","profile-scope-c1r","diff-check-c1r"}; native={"recovery-proof-bridge-c1r","delivery-path-set-c1r","lifecycle-path-set-c1r"}
        return [{"consumer_id":identifier,"phase":"C1R","class":"tree-native" if identifier in native else "closeout-human-review" if identifier=="recovery-integrity-review-c1r" else "worktree-proxy","scope":"recovery_transform","binding_subject":"C1R_CANDIDATE_TREE","change_scope_source":"DELIVERY_SCOPE_SET" if identifier in delivery else "PHASE_COMMIT_DELTA_SET","outcome":"no_material_findings" if identifier=="recovery-integrity-review-c1r" else "go"} for identifier in ids]
    def c0post_bindings(self): return [{"consumer_id":identifier,"phase":"C0_POST","class":"worktree-proxy","scope":"published_bootstrap","binding_subject":"C0_COMMIT_TREE_CLEAN","change_scope_source":"CLEAN_C0_TREE","outcome":"go"} for identifier in ("foundation-validator-c0-post","active-path-closeout-c0-post","active-set-scan-c0-post")]
    def live_gate_evidence(self, tree, repo=None, delphi_root=None):
        commands=dict(self.handoff_module().c0_live_gate_commands(repo,delphi_root)) if repo is not None and delphi_root is not None else {identifier:["python3",identifier] for identifier in ("diff-expectation-c0","todo-authority-c0","todo-completion-c0")}
        return [{"consumer_id":identifier,"candidate_tree_oid":tree,"command":commands[identifier],"exit_code":0,"outcome":"go","stdout_sha256":"a"*64,"stderr_sha256":"b"*64} for identifier in ("diff-expectation-c0","todo-authority-c0","todo-completion-c0")]
    def implementation_reviews(self, tree, paths):
        return [{"consumer_id":identifier,"phase":"C0","candidate_tree_oid":tree,"exact_path_set":sorted(paths),"reviewer_or_session":f"test-session-{identifier}","outcome":"no_material_findings","scope":"implementation_content"} for identifier in self.handoff_module().C0_REVIEW]
    def focused_review(self, phase, tree, paths):
        identifier="closeout-integrity-review-c1" if phase=="c1" else "recovery-integrity-review-c1r"
        return {"consumer_id":identifier,"phase":phase.upper(),"candidate_tree_oid":tree,"exact_path_set":sorted(paths),"reviewer_or_session":f"test-session-{identifier}","outcome":"no_material_findings"}
    def failure_tuple(self, failed): return {"failure_id":"failure-001","failed_c1_oid":failed,"predicate":"actual_remote_mismatch","observed":"remote-tip-mismatch","recorded_at_utc":"2026-09-26T00:00:00Z"}
    def promotion_record_value(self, expected, commit): return {"fresh_pre_push_oid":expected,"expected_lease_oid":expected,"lease_result":"success","promotion_observation":"fresh_pre_push","parent_and_fast_forward":True,"post_push_remote_main_oid":commit,"local_head_oid":commit,"local_tracking_oid":commit}
    def c0post_value(self, commit, tree):
        active=["todos/active/process/TODO-uninotas-canonical-foundation-transition.md","todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md"]
        return {"schema":"uninotas-c0-post-v1","phase":"c0","commit":commit,"tree":tree,"remote":commit,"clean":True,"foundation_validator":"go","active_path_state":"active","active_todo_count":2,"active_paths":active,"consumer_bindings":self.c0post_bindings()}
    def synthetic_phase_evidence(self, phase, expected, commit, tree, baseline, scope, delta, base=None, post=None, bridge=None, failure=None, repo=None, delphi_root=None):
        proof_inputs={"implementation_reviews":self.implementation_reviews(tree,scope)} if phase=="c0" else {"implementation_reviews":bridge["implementation_reviews"],"focused_review":bridge["focused_review"]} if isinstance(bridge,dict) else None
        value={"schema":"uninotas-closeout-intent-v1","state":"prepared","phase":phase,"expected_remote":expected,"new_commit":commit,"candidate_tree":tree,"delivery_baseline":baseline,"delivery_scope_set":scope,"phase_commit_delta_set":delta,"consumer_bindings":self.c0_bindings() if phase=="c0" else self.c1_bindings() if phase=="c1" else self.c1r_bindings(),"live_gate_evidence":self.live_gate_evidence(tree,repo,delphi_root) if phase=="c0" else None,"delphi_root":str(delphi_root) if phase=="c0" else None,"proof_inputs":proof_inputs,"base_evidence":base,"c0_post_evidence":post,"proof_bridge":bridge,"failure_tuple":failure,"provenance":"promoted","post_push_remote_main_oid":commit,"remote_promotion":self.promotion_record_value(expected,commit)}
        if phase=="c1r": value["reverse_bridge"]=bridge
        return value
    def delivery_ready_todo(self, text):
        return (text.replace("`not_run`","`no_material_findings`")
                .replace("| bounded Foundation diff | P1/P2 contract/privacy/validator drift | planned | pending | pending | pre-delivery |","| bounded Foundation diff | P1/P2 contract/privacy/validator drift | passed | clean candidate-bound review artifact | no P1/P2 findings | pre-delivery |")
                .replace("| TODO authority + Foundation sync | future-as-current, weakened validator, hidden tenancy/fallback | planned | pending | pending | pre-delivery |","| TODO authority + Foundation sync | future-as-current, weakened validator, hidden tenancy/fallback | passed | clean candidate-bound review artifact | no findings | pre-delivery |"))
    def completed_todo(self, text, c0):
        fields={"Lifecycle state":"`Completed — conditional Production-Ready candidate`","Current delivery stage":"`Production-Ready`","Qualifiers":"`Provisional`","Next exact step":"external C1 remote verification + semantic active scan handoff","Work state":"`review`","Disposition":"`move-completed`","Disposition reason":"candidate C1 guards green; Production-Ready remains conditional on external handoff","Post-commit/push status":"`C0 verified; C1 external verification pending`","Next path/status action":"external C1 verification + active scan handoff"}
        for label,value in fields.items(): text=re.sub(rf"^- \*\*{re.escape(label)}:\*\*.*$",f"- **{label}:** {value}",text,count=1,flags=re.M)
        text=re.sub(r"^\| Foundation UniNotas cutover \|.*$",f"| Foundation UniNotas cutover | `main@{c0}` | `n/a — main-only authority` | `n/a` | `origin/main@{c0}` | C1 conditional; external activation pending |",text,count=1,flags=re.M)
        return text.replace("**C0 active implementation/genesis commit:** `pending delivery — persisted in C1 after observation`",f"**C0 active implementation/genesis commit:** `{c0}`").replace("**C0 remote verification:** `pending delivery — typed C0 promotion + C0_POST clean validator/active-path/exact-two-active evidence persisted externally and C0 facts persisted in C1`",f"**C0 remote verification:** `fresh remote/origin/main/base HEAD all observed as {c0}`").replace("`not_run`","`passed`")
    def c0_foundation_fixture(self):
        temp=tempfile.TemporaryDirectory(); self.addCleanup(temp.cleanup); root=pathlib.Path(temp.name); repo=root/"foundation"; remote=root/"remote.git"; shutil.copytree(FOUNDATION,repo,ignore=shutil.ignore_patterns(".git","__pycache__")); ledger=repo/"deterministic/capability_identity_ledger.json"; ledger_text=ledger.read_text(); ledger.unlink(); subprocess.run(["git","init","--bare","-q",str(remote)],check=True); self.git(repo,"init","-q"); self.git(repo,"config","user.email","test@example.invalid"); self.git(repo,"config","user.name","Test"); self.git(repo,"add","."); self.git(repo,"commit","-qm","pre-c0 base"); self.git(repo,"branch","-M","main"); self.git(repo,"remote","add","origin",str(remote)); self.git(repo,"push","-q","origin","main"); subprocess.run(["git","-C",str(remote),"symbolic-ref","HEAD","refs/heads/main"],check=True)
        base=self.git(repo,"rev-parse","HEAD").stdout.strip(); ledger.write_text(ledger_text); todo=repo/"todos/active/process/TODO-uninotas-canonical-foundation-transition.md"; text=self.delivery_ready_todo(todo.read_text()); text=text.replace("- [ ] `VAL-04`","- [x] `VAL-04`").replace("- [ ] `VAL-05`","- [x] `VAL-05`"); text=re.sub(r"(\| `VAL-04` \|.*?\| local \| )(?:completed|planned)( \|)",r"\1passed\2",text); text=re.sub(r"(\| `VAL-05` \|.*?\| local \| )(?:completed|planned)( \|)",r"\1passed\2",text); todo.write_text(text); self.git(repo,"add",str(ledger.relative_to(repo)),str(todo.relative_to(repo))); self.git(repo,"commit","-qm","c0 candidate"); head=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.git(repo,"rev-parse","HEAD^{tree}").stdout.strip(); scope=self.git(repo,"diff","--no-renames","--name-only",base,head).stdout.splitlines(); tmp=repo/"artifacts/tmp"; evidence=tmp/"c0.json"; output=tmp/"post.json"; bindings=tmp/"c0-bindings.json"; reviews=tmp/"c0-implementation-reviews.json"; journal=tmp/"c0-intent.json"; bindings.write_text(json.dumps(self.c0_bindings())); reviews.write_text(json.dumps(self.implementation_reviews(tree,scope))); promoted=subprocess.run(["python3",str(SCRIPT),"promote","--phase","c0","--repo",str(repo),"--expected-remote",base,"--new-commit",head,"--candidate-tree",tree,"--delivery-baseline",base,"--consumer-bindings",str(bindings),"--implementation-reviews",str(reviews),"--delphi-root",str(self.fake_c0_delphi_gates(root)),"--journal",str(journal),"--output",str(evidence)],text=True,capture_output=True); self.assertEqual(0,promoted.returncode,promoted.stderr)
        return root,repo,remote,evidence,output,head,tree
    def verify_c0(self, repo, evidence, output, delphi_root=DELPHI):
        return subprocess.run(["python3",str(SCRIPT),"verify","--phase","c0","--repo",str(repo),"--phase-evidence",str(evidence),"--delphi-root",str(delphi_root),"--output",str(output)],text=True,capture_output=True)
    def activation_fixture(self, transition_completed=True):
        root,repo,remote,c0e,c0post,c0,tree0=self.c0_foundation_fixture(); tmp=repo/"artifacts/tmp"
        verified=self.verify_c0(repo,c0e,c0post); self.assertEqual(0,verified.returncode,verified.stderr)
        if transition_completed:
            active="todos/active/process/TODO-uninotas-canonical-foundation-transition.md"; completed="todos/completed/process/TODO-uninotas-canonical-foundation-transition.md"; (repo/"todos/completed/process").mkdir(parents=True,exist_ok=True); self.git(repo,"mv",active,completed); path=repo/completed; text=self.completed_todo(path.read_text(),c0); path.write_text(text)
            for relative in ("artifacts/publication-manifest.txt","artifacts/feature-briefs/uninotas-smart-notas-central.md","todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md"):
                target=repo/relative; target.write_text(target.read_text().replace(active,completed))
            self.git(repo,"add","-A")
        else: (repo/"c1-marker").write_text("C1 pending closeout\n"); self.git(repo,"add","c1-marker")
        tree1=self.git(repo,"write-tree").stdout.strip(); delta=self.git(repo,"diff","--cached","--no-renames","--name-only").stdout.splitlines(); reviews=tmp/"implementation-reviews.json"; focused=tmp/"c1-focused-review.json"
        if transition_completed:
            reviews.write_text(json.dumps(self.implementation_reviews(tree0,json.loads(c0e.read_text())["delivery_scope_set"]))); focused.write_text(json.dumps(self.focused_review("c1",tree1,delta)))
        else:
            reviews.write_text(json.dumps(self.implementation_reviews(tree0,json.loads(c0e.read_text())["delivery_scope_set"]))); focused.write_text(json.dumps(self.focused_review("c1",tree1,delta)))
        self.git(repo,"commit","-qm","c1 closeout"); c1=self.git(repo,"rev-parse","HEAD").stdout.strip()
        bindings=tmp/"c1-bindings.json"; journal=tmp/"c1-intent.json"; c1e=tmp/"c1.json"
        bindings.write_text(json.dumps(self.c1_bindings()))
        promoted=subprocess.run(["python3",str(SCRIPT),"promote","--phase","c1","--repo",str(repo),"--expected-remote",c0,"--new-commit",c1,"--candidate-tree",tree1,"--consumer-bindings",str(bindings),"--base-evidence",str(c0e),"--c0-post-evidence",str(c0post),"--implementation-reviews",str(reviews),"--focused-review",str(focused),"--journal",str(journal),"--output",str(c1e)],text=True,capture_output=True)
        if transition_completed: self.assertEqual(0,promoted.returncode,promoted.stderr)
        else: self.assertEqual(2,promoted.returncode)
        return root,repo,remote,c0e,c0post,c1e,c0,c1,tree1
    def activate_c1(self, repo, c0, c0post, c1, output, delphi_root=DELPHI):
        return subprocess.run(["python3",str(SCRIPT),"activate","--phase","c1","--repo",str(repo),"--c0-evidence",str(c0),"--c0-post-evidence",str(c0post),"--c1-evidence",str(c1),"--delphi-root",str(delphi_root),"--output",str(output)],text=True,capture_output=True)
    def recovery_activation_fixture(self, completed_transition=False, stale_tracking=False):
        if completed_transition:
            root,repo,remote,_evidence,_output,c0,tree0=self.c0_foundation_fixture(); tmp=repo/"artifacts/tmp"
            (repo/"failed-c1-marker").write_text("failed c1\n"); self.git(repo,"add","failed-c1-marker"); self.git(repo,"commit","-qm","failed c1"); failed=self.git(repo,"rev-parse","HEAD").stdout.strip(); failed_tree=self.git(repo,"rev-parse","HEAD^{tree}").stdout.strip(); self.git(repo,"push","-q","origin","main")
            (repo/"todos/completed/process").mkdir(parents=True,exist_ok=True); self.git(repo,"mv","todos/active/process/TODO-uninotas-canonical-foundation-transition.md","todos/completed/process/TODO-uninotas-canonical-foundation-transition.md"); self.git(repo,"commit","-qm","invalid completed recovery"); c1r=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree1r=self.git(repo,"rev-parse","HEAD^{tree}").stdout.strip(); self.git(repo,"push","-q","origin","main")
            c0post={"schema":"uninotas-c0-post-v1","phase":"c0","commit":c0,"tree":tree0,"remote":c0,"clean":True,"foundation_validator":"go","active_path_state":"active","active_todo_count":2,"active_paths":["todos/active/process/TODO-uninotas-canonical-foundation-transition.md","todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md"],"consumer_bindings":self.c0post_bindings()}; c0e={"phase":"c0","new_commit":c0,"candidate_tree":tree0,"post_push_remote_main_oid":c0,"consumer_bindings":self.c0_bindings()}; failed_e={"phase":"c1","new_commit":failed,"candidate_tree":failed_tree,"consumer_bindings":self.c1_bindings(),"base_evidence":c0e}; delta=self.git(repo,"diff","--no-renames","--name-only",failed,c1r).stdout.splitlines(); reverse={"validator":"validate_closeout_diff.py","phase":"c1r","base_commit":failed,"base_tree":failed_tree,"candidate_tree":tree1r,"exact_delta":delta,"outcome":"go","implementation_reviews":self.implementation_reviews(tree0,["item"]),"focused_review":self.focused_review("c1r",tree1r,delta)}; c1r_e={"phase":"c1r","new_commit":c1r,"candidate_tree":tree1r,"post_push_remote_main_oid":c1r,"consumer_bindings":self.c1r_bindings(),"reverse_bridge":reverse}; failure={"failed_c1":failed,"failure_class":"remote_mismatch"}; values=(c0e,c0post,failed_e,c1r_e,failure)
            failure=self.failure_tuple(failed); reverse["failure_tuple"]=failure; c1r_e["failure_tuple"]=failure; c1r_e["proof_bridge"]=reverse
            c0e=json.loads(_evidence.read_text()); delivery_baseline=c0e["delivery_baseline"]; delivery_scope=c0e["delivery_scope_set"]
            promote=lambda expected,commit:{"fresh_pre_push_oid":expected,"expected_lease_oid":expected,"lease_result":"success","promotion_observation":"fresh_pre_push","parent_and_fast_forward":True,"post_push_remote_main_oid":commit,"local_head_oid":commit,"local_tracking_oid":commit}
            failed_e.update({"delivery_baseline":delivery_baseline,"delivery_scope_set":self.git(repo,"diff","--no-renames","--name-only",delivery_baseline,failed).stdout.splitlines(),"phase_commit_delta_set":self.git(repo,"diff","--no-renames","--name-only",c0,failed).stdout.splitlines(),"base_evidence":c0e,"c0_post_evidence":c0post,"remote_promotion":promote(c0,failed)})
            c1r_e.update({"delivery_baseline":delivery_baseline,"delivery_scope_set":self.git(repo,"diff","--no-renames","--name-only",delivery_baseline,c1r).stdout.splitlines(),"phase_commit_delta_set":delta,"base_evidence":failed_e,"c0_post_evidence":c0post,"proof_bridge":reverse,"remote_promotion":promote(failed,c1r)})
            values=(c0e,c0post,failed_e,c1r_e,failure)
            paths=[]
            for name,value in zip(("recovery-c0.json","recovery-c0post.json","failed-c1.json","c1r.json","failure.json"),values): path=tmp/name; path.write_text(json.dumps(value)); paths.append(path)
            return root,repo,remote,*paths,c1r,tree1r

        root,repo,remote,c0e,c0post,failed_e,_c0,failed,_failed_tree=self.activation_fixture(); tmp=repo/"artifacts/tmp"
        completed="todos/completed/process/TODO-uninotas-canonical-foundation-transition.md"; active="todos/active/process/TODO-uninotas-canonical-foundation-transition.md"; self.git(repo,"mv",completed,active); path=repo/active; text=path.read_text()
        replacements={
            "Lifecycle state":"`Active — blocked recovery`", "Current delivery stage":"`Local-Implemented`", "Qualifiers":"`Blocked`", "Next exact step":"reconcile observed C1 failure and rerun atomic closeout", "Work state":"`blocked`", "Why this state now":"published C1 failed external activation", "Exit condition":"failure reconciled and exact closeout protocol green", "Disposition":"`blocked`", "Disposition reason":"published C1 failed external activation", "Post-commit/push status":"`FAILED_C1 observed; C1R recovery pending`", "Next path/status action":"publish/verify C1R then reconcile blocker",
        }
        for label,value in replacements.items(): text=re.sub(rf"^- \*\*{re.escape(label)}:\*\*.*$",f"- **{label}:** {value}",text,count=1,flags=re.M)
        c0=json.loads(c0e.read_text())["new_commit"]
        text=re.sub(r"^\| Foundation UniNotas cutover \|.*$",f"| Foundation UniNotas cutover | `main@{c0}` | `n/a — main-only authority` | `n/a` | `origin/main@{c0}` | C1 external activation failed; C1R recovery in progress |",text,count=1,flags=re.M)
        text += f"\nFailure-Tuple: failure_id=failure-001; failed_c1_oid={failed}; predicate=actual_remote_mismatch; observed=remote-tip-mismatch; recorded_at_utc=2026-09-26T00:00:00Z\nObserved-Failure: external_verification_failed\n"; path.write_text(text)
        for relative in ("artifacts/publication-manifest.txt","artifacts/feature-briefs/uninotas-smart-notas-central.md","todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md"):
            target=repo/relative; target.write_text(target.read_text().replace(completed,active))
        self.git(repo,"add","-A"); tree1r=self.git(repo,"write-tree").stdout.strip(); delta=self.git(repo,"diff","--cached","--no-renames","--name-only").stdout.splitlines(); reviews=tmp/"recovery-implementation-reviews.json"; focused=tmp/"c1r-focused-review.json"; c0_value=json.loads(c0e.read_text()); reviews.write_text(json.dumps(self.implementation_reviews(c0_value["candidate_tree"],c0_value["delivery_scope_set"]))); focused.write_text(json.dumps(self.focused_review("c1r",tree1r,delta)))
        self.git(repo,"commit","-qm","c1r recovery"); c1r=self.git(repo,"rev-parse","HEAD").stdout.strip(); bindings=tmp/"c1r-bindings.json"; bindings.write_text(json.dumps(self.c1r_bindings())); failure=tmp/"failure.json"; failure.write_text(json.dumps(self.failure_tuple(failed))); c1r_e=tmp/"c1r.json"; journal=tmp/"c1r-intent.json"
        if stale_tracking: self.git(repo,"update-ref","refs/remotes/origin/main",c0)
        promoted=subprocess.run(["python3",str(SCRIPT),"promote","--phase","c1r","--repo",str(repo),"--expected-remote",failed,"--new-commit",c1r,"--candidate-tree",tree1r,"--consumer-bindings",str(bindings),"--base-evidence",str(failed_e),"--c0-post-evidence",str(c0post),"--implementation-reviews",str(reviews),"--focused-review",str(focused),"--failure-tuple",str(failure),"--journal",str(journal),"--output",str(c1r_e)],text=True,capture_output=True); self.assertEqual(0,promoted.returncode,promoted.stderr)
        return root,repo,remote,c0e,c0post,failed_e,c1r_e,failure,c1r,tree1r
    def activate_c1r(self, repo, c0, c0post, failed, c1r, failure, output, delphi_root=DELPHI):
        return subprocess.run(["python3",str(SCRIPT),"activate","--phase","c1r","--repo",str(repo),"--c0-evidence",str(c0),"--c0-post-evidence",str(c0post),"--failed-c1-evidence",str(failed),"--c1r-evidence",str(c1r),"--failure-tuple",str(failure),"--delphi-root",str(delphi_root),"--output",str(output)],text=True,capture_output=True)
    def git(self, repo, *args): return subprocess.run(["git","-C",str(repo),*args],text=True,capture_output=True,check=True)
    def fixture(self):
        temp=tempfile.TemporaryDirectory(); self.addCleanup(temp.cleanup); root=pathlib.Path(temp.name); remote=root/"remote.git"; repo=root/"repo"; subprocess.run(["git","init","--bare","-q",str(remote)],check=True); subprocess.run(["git","init","-q",str(repo)],check=True); self.git(repo,"config","user.email","test@example.invalid"); self.git(repo,"config","user.name","Test")
        (repo/"item").write_text("prebase"); (repo/".gitignore").write_text("artifacts/tmp/\n"); self.git(repo,"add","."); self.git(repo,"commit","-qm","prebase"); (repo/"item").write_text("base"); self.git(repo,"add","item"); self.git(repo,"commit","-qm","base"); self.git(repo,"branch","-M","main"); self.git(repo,"remote","add","origin",str(remote)); self.git(repo,"push","-q","origin","main"); subprocess.run(["git","-C",str(remote),"symbolic-ref","HEAD","refs/heads/main"],check=True)
        return root,remote,repo,self.git(repo,"rev-parse","HEAD").stdout.strip()
    def candidate(self, repo, text="candidate"):
        (repo/"item").write_text(text); self.git(repo,"add","item")
        if "c1r" in text:
            failed=self.git(repo,"rev-parse","HEAD").stdout.strip(); path=repo/"todos/active/process/TODO-uninotas-canonical-foundation-transition.md"; path.parent.mkdir(parents=True,exist_ok=True); path.write_text(f"Failure-Tuple: failure_id=failure-001; failed_c1_oid={failed}; predicate=actual_remote_mismatch; observed=remote-tip-mismatch; recorded_at_utc=2026-09-26T00:00:00Z\n"); self.git(repo,"add",str(path.relative_to(repo)))
        tree=self.git(repo,"write-tree").stdout.strip(); self.git(repo,"commit","-qm",text); return self.git(repo,"rev-parse","HEAD").stdout.strip(),tree
    def promote_args(self, repo, phase, expected, commit, tree):
        tmp=repo/"artifacts/tmp"; tmp.mkdir(parents=True,exist_ok=True); bindings=tmp/"bindings.json"; bindings.write_text(json.dumps(self.c0_bindings() if phase=="c0" else self.c1_bindings() if phase=="c1" else self.c1r_bindings()))
        args=["python3",str(SCRIPT),"promote","--phase",phase,"--repo",str(repo),"--expected-remote",expected,"--new-commit",commit,"--candidate-tree",tree,"--consumer-bindings",str(bindings),"--journal",str(tmp/"intent.json"),"--output",str(tmp/"output.json")]
        if phase=="c0":
            reviews=tmp/"c0-implementation-reviews.json"; reviews.write_text(json.dumps(self.implementation_reviews(tree,self.git(repo,"diff","--no-renames","--name-only",expected,commit).stdout.splitlines())))
            args += ["--delivery-baseline",expected,"--implementation-reviews",str(reviews),"--delphi-root",str(self.fake_c0_delphi_gates(repo.parent))]
        if phase in {"c1","c1r"}:
            base=tmp/"base.json"; post=tmp/"post.json"; reviews=tmp/"implementation-reviews.json"; focused=tmp/"focused-review.json"; base_tree=self.git(repo,"rev-parse",expected+"^{tree}").stdout.strip()
            if phase=="c1": c0_commit,c0_tree=expected,base_tree
            else:
                parent=subprocess.run(["git","-C",str(repo),"rev-parse","--verify",expected+"^"],text=True,capture_output=True); c0_commit=parent.stdout.strip() if parent.returncode==0 else expected; c0_tree=self.git(repo,"rev-parse",c0_commit+"^{tree}").stdout.strip()
            post_value=self.c0post_value(c0_commit,c0_tree); c0_parent=self.git(repo,"rev-parse",c0_commit+"^").stdout.strip(); c0_scope=self.git(repo,"diff","--no-renames","--name-only",c0_parent,c0_commit).stdout.splitlines(); fake_delphi=self.fake_c0_delphi_gates(repo.parent)
            c0_value=self.synthetic_phase_evidence("c0",c0_parent,c0_commit,c0_tree,c0_parent,c0_scope,c0_scope,repo=repo,delphi_root=fake_delphi)
            if phase=="c1": base_value=c0_value
            else:
                base_delta=self.git(repo,"diff","--no-renames","--name-only",c0_commit,expected).stdout.splitlines()
                base_bridge={"validator":"validate_closeout_diff.py","phase":"c1","base_commit":c0_commit,"base_tree":c0_tree,"candidate_tree":base_tree,"exact_delta":base_delta,"outcome":"go","implementation_reviews":self.implementation_reviews(c0_tree,["item"]),"focused_review":self.focused_review("c1",base_tree,base_delta)}
                base_value=self.synthetic_phase_evidence("c1",c0_commit,expected,base_tree,c0_parent,self.git(repo,"diff","--no-renames","--name-only",c0_parent,expected).stdout.splitlines(),base_delta,c0_value,post_value,base_bridge)
            base.write_text(json.dumps(base_value)); post.write_text(json.dumps(post_value)); delta=self.git(repo,"diff","--no-renames","--name-only",expected,commit).stdout.splitlines(); bridge_value={"validator":"validate_closeout_diff.py","phase":phase,"base_commit":expected,"base_tree":base_tree,"candidate_tree":tree,"exact_delta":delta,"outcome":"go","implementation_reviews":self.implementation_reviews(c0_tree,["item"]),"focused_review":self.focused_review(phase,tree,delta)}
            if phase=="c1r":
                failure=tmp/"failure.json"; failure_value=self.failure_tuple(expected); failure.write_text(json.dumps(failure_value)); bridge_value["failure_tuple"]=failure_value; args += ["--failure-tuple",str(failure)]
            reviews.write_text(json.dumps(bridge_value["implementation_reviews"])); focused.write_text(json.dumps(bridge_value["focused_review"])); args += ["--base-evidence",str(base),"--c0-post-evidence",str(post),"--implementation-reviews",str(reviews),"--focused-review",str(focused)]
        return args,tmp/"intent.json",tmp/"output.json"
    def advance_remote(self, root, remote, text):
        sibling=root/"sibling"; self.git(root,"clone","-q",str(remote),str(sibling)); self.git(sibling,"config","user.email","test@example.invalid"); self.git(sibling,"config","user.name","Test"); (sibling/"item").write_text(text); self.git(sibling,"add","item"); self.git(sibling,"commit","-qm",text); self.git(sibling,"push","-q","origin","main"); return self.git(sibling,"rev-parse","HEAD").stdout.strip()
    def fake_delphi_guard(self, root, all_count, all_paths):
        tools=root/"fake-delphi"/"tools"; tools.mkdir(parents=True)
        script=tools/"todo_closeout_guard.py"
        script.write_text("""#!/usr/bin/env python3
import pathlib, sys
transition='todos/active/process/TODO-uninotas-canonical-foundation-transition.md'
all_count=int(sys.argv[1])
all_paths=sys.argv[2:]
paths=all_paths if '--all-active' in sys.argv else [transition]
count=all_count if '--all-active' in sys.argv else 1
print('TODO Closeout Guard')
print('Overall outcome: go')
print('Context:')
print(f'  - todo_count: {count}')
for relative in paths:
    print(f'  - todo: {pathlib.Path.cwd() / relative}')
    print('    path_state: active')
""".replace("all_count=int(sys.argv[1])\nall_paths=sys.argv[2:]",f"all_count={all_count!r}\nall_paths={all_paths!r}"))
        script.chmod(0o755)
        return tools.parent
    def fake_c0_delphi_gates(self, root, failure=None):
        tools=root/"fake-c0-delphi"/"tools"; tools.mkdir(parents=True,exist_ok=True)
        for name in ("todo_diff_expectation_guard.py","todo_authority_guard.py","todo_completion_guard.py"):
            script=tools/name
            outcome="no-go" if name==failure else "go"
            exit_code=2 if name==failure else 0
            script.write_text(f"#!/usr/bin/env python3\nprint('Overall outcome: {outcome}')\nraise SystemExit({exit_code})\n")
            script.chmod(0o755)
        return tools.parent
    def post_push_race_hook(self, root):
        script=root/"post-push-race.py"
        script.write_text("""#!/usr/bin/env python3
import pathlib, subprocess, sys, tempfile
remote=sys.argv[2]
sibling=pathlib.Path(tempfile.mkdtemp(prefix='post-push-race-',dir=str(pathlib.Path(remote).parent)))
subprocess.run(['git','clone','-q',remote,str(sibling)],check=True)
subprocess.run(['git','-C',str(sibling),'config','user.email','test@example.invalid'],check=True)
subprocess.run(['git','-C',str(sibling),'config','user.name','Test'],check=True)
(sibling/'post-push-race').write_text('third remote commit\\n')
subprocess.run(['git','-C',str(sibling),'add','post-push-race'],check=True)
subprocess.run(['git','-C',str(sibling),'commit','-qm','post-push race'],check=True)
subprocess.run(['git','-C',str(sibling),'push','-q','origin','main'],check=True)
""")
        script.chmod(0o755)
        return script
    def test_help_is_available(self):
        result = subprocess.run(["python3", str(SCRIPT), "--help"], text=True, capture_output=True)
        self.assertEqual(0, result.returncode)
        self.assertIn("promote", result.stdout)

    def test_c0_canonical_runbook_requires_implementation_review_catalog(self):
        todo=(FOUNDATION/"todos/active/process/TODO-uninotas-canonical-foundation-transition.md").read_text(encoding="utf-8")
        command=next(line for line in todo.splitlines() if line.startswith("- C0 CAS promotion/evidence:"))
        self.assertIn("--implementation-reviews <IGNORED_C0_IMPLEMENTATION_REVIEWS_JSON>",command)
        binding=next(line for line in todo.splitlines() if line.startswith("- Human-review binding:"))
        for field in ("consumer_id","phase","candidate_tree_oid","exact_path_set","reviewer_or_session","outcome","scope"):
            self.assertIn(field,binding)

    def test_promote_uses_expected_value_lease_against_bare_remote(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp); remote=root/"remote.git"; repo=root/"repo"; journal=repo/"artifacts/tmp/intent.json"; output=repo/"artifacts/tmp/evidence.json"; bindings=repo/"artifacts/tmp/bindings.json"
            subprocess.run(["git","init","--bare","-q",str(remote)],check=True)
            subprocess.run(["git","init","-q",str(repo)],check=True)
            for key,value in (("user.email","test@example.invalid"),("user.name","Test")):
                subprocess.run(["git","-C",str(repo),"config",key,value],check=True)
            (repo/"item").write_text("one"); (repo/".gitignore").write_text("artifacts/tmp/\n"); subprocess.run(["git","-C",str(repo),"add","."],check=True); subprocess.run(["git","-C",str(repo),"commit","-qm","base"],check=True)
            subprocess.run(["git","-C",str(repo),"branch","-M","main"],check=True); subprocess.run(["git","-C",str(repo),"remote","add","origin",str(remote)],check=True); subprocess.run(["git","-C",str(repo),"push","-q","origin","main"],check=True)
            base=subprocess.run(["git","-C",str(repo),"rev-parse","HEAD"],text=True,capture_output=True,check=True).stdout.strip()
            (repo/"item").write_text("two"); subprocess.run(["git","-C",str(repo),"add","."],check=True); tree=subprocess.run(["git","-C",str(repo),"write-tree"],text=True,capture_output=True,check=True).stdout.strip(); subprocess.run(["git","-C",str(repo),"commit","-qm","next"],check=True); commit=subprocess.run(["git","-C",str(repo),"rev-parse","HEAD"],text=True,capture_output=True,check=True).stdout.strip()
            bindings.parent.mkdir(parents=True); bindings.write_text(json.dumps(self.c0_bindings())); reviews=repo/"artifacts/tmp/reviews.json"; reviews.write_text(json.dumps(self.implementation_reviews(tree,["item"])))
            result=subprocess.run(["python3",str(SCRIPT),"promote","--phase","c0","--repo",str(repo),"--expected-remote",base,"--new-commit",commit,"--candidate-tree",tree,"--delivery-baseline",base,"--consumer-bindings",str(bindings),"--implementation-reviews",str(reviews),"--delphi-root",str(self.fake_c0_delphi_gates(root)),"--journal",str(journal),"--output",str(output)],text=True,capture_output=True)
            self.assertEqual(0,result.returncode,result.stderr); self.assertEqual(commit,json.loads(output.read_text())["post_push_remote_main_oid"])

    def test_handoff_pos_05_resume_after_push_before_evidence_for_all_phases(self):
        for phase in ("c0",):
            with self.subTest(phase=phase):
                root,remote,repo,base=self.fixture(); commit,tree=self.candidate(repo,phase); command,journal,output=self.promote_args(repo,phase,base,commit,tree)
                result=subprocess.run(command,text=True,capture_output=True,env={**os.environ,"UNINOTAS_TEST_AFTER_PUSH_FAILPOINT":"1","UNINOTAS_HANDOFF_TEST_MODE":"1"})
                self.assertNotEqual(0,result.returncode); self.assertTrue(journal.is_file())
                intent=json.loads(journal.read_text()); intent["live_gate_evidence"][0]["command"]=["forged-command"]; intent["live_gate_evidence"][0]["stdout_sha256"]="f"*64; journal.write_text(json.dumps(intent))
                resumed=subprocess.run(["python3",str(SCRIPT),"resume","--phase",phase,"--repo",str(repo),"--journal",str(journal),"--output",str(output)],text=True,capture_output=True)
                self.assertEqual(0,resumed.returncode,resumed.stderr); evidence=json.loads(output.read_text()); self.assertEqual("resumed_remote_already_at_new_commit",evidence["provenance"]); self.assertEqual("not_observed_after_interruption",evidence["lease_result"]); self.assertEqual(commit,evidence["post_push_remote_main_oid"]); self.assertNotEqual(["forged-command"],evidence["live_gate_evidence"][0]["command"])

    def test_handoff_pos_06_resume_reexecutes_internal_proof_for_c1_and_c1r(self):
        fixtures=(self.activation_fixture(),self.recovery_activation_fixture())
        for phase,fixture in zip(("c1","c1r"),fixtures):
            with self.subTest(phase=phase):
                if phase=="c1": _root,repo,remote,_c0,_post,evidence,_base,_commit,_tree=fixture
                else: _root,repo,remote,_c0,_post,_failed,evidence,_failure,_commit,_tree=fixture
                value=json.loads(evidence.read_text()); intent={key:value[key] for key in self.handoff_module().INTENT_KEYS}; journal=repo/f"artifacts/tmp/{phase}-resume-intent.json"; output=repo/f"artifacts/tmp/{phase}-resume-output.json"; original_bridge=json.loads(json.dumps(intent["proof_bridge"])); intent["proof_bridge"]["implementation_reviews"].reverse(); journal.write_text(json.dumps(intent)); evidence.unlink()
                subprocess.run(["git","--git-dir",str(remote),"update-ref","refs/heads/main",intent["expected_remote"]],check=True); self.git(repo,"update-ref","refs/remotes/origin/main",intent["expected_remote"])
                rejected=subprocess.run(["python3",str(SCRIPT),"resume","--phase",phase,"--repo",str(repo),"--journal",str(journal),"--output",str(output)],text=True,capture_output=True)
                self.assertEqual(2,rejected.returncode); self.assertIn("resume intent is invalid",rejected.stderr); self.assertFalse(output.exists())
                intent["proof_bridge"]=original_bridge; journal.write_text(json.dumps(intent))
                base_record=intent["base_evidence"]; original_expected=base_record["expected_remote"]; base_record["expected_remote"]=base_record["new_commit"]
                for key in ("fresh_pre_push_oid","expected_lease_oid"): base_record["remote_promotion"][key]=base_record["new_commit"]
                journal.write_text(json.dumps(intent)); rejected=subprocess.run(["python3",str(SCRIPT),"resume","--phase",phase,"--repo",str(repo),"--journal",str(journal),"--output",str(output)],text=True,capture_output=True)
                self.assertEqual(2,rejected.returncode); self.assertIn("resume intent is invalid",rejected.stderr); self.assertFalse(output.exists())
                base_record["expected_remote"]=original_expected
                for key in ("fresh_pre_push_oid","expected_lease_oid"): base_record["remote_promotion"][key]=original_expected
                journal.write_text(json.dumps(intent))
                result=subprocess.run(["python3",str(SCRIPT),"resume","--phase",phase,"--repo",str(repo),"--journal",str(journal),"--output",str(output)],text=True,capture_output=True)
                self.assertEqual(0,result.returncode,result.stderr); self.assertEqual(intent["proof_bridge"],json.loads(output.read_text())["proof_bridge"])

    def test_c1_and_c1r_promote_reject_invalid_recorded_base_chain_before_push(self):
        commands=[self.c1_command()]
        _root,_remote,repo,base=self.fixture(); failed,_tree=self.candidate(repo,"failed c1"); self.git(repo,"push","-q","origin","main"); c1r,tree=self.candidate(repo,"c1r chain"); command,_,_=self.promote_args(repo,"c1r",failed,c1r,tree); commands.append((repo,command))
        for repo,command in commands:
            with self.subTest(phase=command[command.index("--phase")+1]):
                base_path=pathlib.Path(command[command.index("--base-evidence")+1]); post_path=pathlib.Path(command[command.index("--c0-post-evidence")+1]); base=json.loads(base_path.read_text()); target=base if base["phase"]=="c0" else base["base_evidence"]
                original_expected=target["expected_remote"]; target["expected_remote"]=target["new_commit"]
                for key in ("fresh_pre_push_oid","expected_lease_oid"): target["remote_promotion"][key]=target["new_commit"]
                base_path.write_text(json.dumps(base)); expected=command[command.index("--expected-remote")+1]; result=subprocess.run(command,text=True,capture_output=True)
                self.assertEqual(2,result.returncode); self.assertEqual(expected,self.git(repo,"ls-remote","origin","refs/heads/main").stdout.split()[0])
                target["expected_remote"]=original_expected
                for key in ("fresh_pre_push_oid","expected_lease_oid"): target["remote_promotion"][key]=original_expected
                base_path.write_text(json.dumps(base)); post=json.loads(post_path.read_text()); post["remote"]="f"*40; post_path.write_text(json.dumps(post)); result=subprocess.run(command,text=True,capture_output=True)
                self.assertEqual(2,result.returncode); self.assertEqual(expected,self.git(repo,"ls-remote","origin","refs/heads/main").stdout.split()[0])

    def test_c0_requires_closed_candidate_bound_implementation_review_attestations(self):
        mutations={
            "missing_phase":lambda rows:rows[0].pop("phase"),
            "wrong_phase":lambda rows:rows[0].__setitem__("phase","C1"),
            "blank_reviewer":lambda rows:rows[0].__setitem__("reviewer_or_session",""),
            "invisible_reviewer":lambda rows:rows[0].__setitem__("reviewer_or_session","\u200b"),
            "combining_reviewer":lambda rows:rows[0].__setitem__("reviewer_or_session","\u034f"),
            "control_reviewer":lambda rows:rows[0].__setitem__("reviewer_or_session","reviewer\nforged"),
            "overlong_reviewer":lambda rows:rows[0].__setitem__("reviewer_or_session","a"*129),
            "wrong_outcome":lambda rows:rows[0].__setitem__("outcome","go"),
            "wrong_scope":lambda rows:rows[0].__setitem__("scope","other"),
            "wrong_paths":lambda rows:rows[0].__setitem__("exact_path_set",["wrong"]),
            "duplicate_consumer":lambda rows:rows[1].__setitem__("consumer_id",rows[0]["consumer_id"]),
        }
        for case,mutate in mutations.items():
            with self.subTest(case=case):
                _root,_remote,repo,base=self.fixture(); commit,tree=self.candidate(repo); command,_,output=self.promote_args(repo,"c0",base,commit,tree); review_path=pathlib.Path(command[command.index("--implementation-reviews")+1]); rows=json.loads(review_path.read_text()); mutate(rows); review_path.write_text(json.dumps(rows)); result=subprocess.run(command,text=True,capture_output=True)
                self.assertEqual(2,result.returncode); self.assertFalse(output.exists()); self.assertEqual(base,self.git(repo,"ls-remote","origin","refs/heads/main").stdout.split()[0])
        _root,_remote,repo,base=self.fixture(); commit,tree=self.candidate(repo); command,_,_=self.promote_args(repo,"c0",base,commit,tree); index=command.index("--implementation-reviews"); del command[index:index+2]; result=subprocess.run(command,text=True,capture_output=True); self.assertEqual(2,result.returncode); self.assertEqual(base,self.git(repo,"ls-remote","origin","refs/heads/main").stdout.split()[0])

    def test_handoff_neg_failpoint_requires_explicit_test_mode(self):
        _root,_remote,repo,base=self.fixture(); commit,tree=self.candidate(repo); command,_journal,output=self.promote_args(repo,"c0",base,commit,tree)
        result=subprocess.run(command,text=True,capture_output=True,env={**os.environ,"UNINOTAS_TEST_AFTER_PUSH_FAILPOINT":"1"})
        self.assertEqual(2,result.returncode); self.assertIn("test controls require UNINOTAS_HANDOFF_TEST_MODE=1",result.stderr); self.assertFalse(output.exists()); self.assertEqual(base,self.git(repo,"ls-remote","origin","refs/heads/main").stdout.split()[0])

    def test_handoff_neg_canonical_delphi_root_and_delivery_baseline_are_not_caller_substitutable(self):
        module=self.handoff_module()
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(ValueError,"canonical sibling checkout"): module.resolve_delphi_root(FOUNDATION,pathlib.Path(temporary)/"fake-delphi")
        head=self.git(FOUNDATION,"rev-parse","HEAD").stdout.strip()
        if head!=module.DELIVERY_BASELINE:
            with self.assertRaisesRegex(ValueError,"approved baseline"): module.phase_sets(FOUNDATION,"c0",head,head,head,None)

    def test_remote_neg_post_push_race_blocks_promote_and_resumed_push_evidence(self):
        root,_remote,repo,base=self.fixture(); commit,tree=self.candidate(repo,"post-push race"); command,journal,output=self.promote_args(repo,"c0",base,commit,tree); hook=self.post_push_race_hook(root); environment={**os.environ,"UNINOTAS_HANDOFF_TEST_MODE":"1","UNINOTAS_TEST_POST_PUSH_HOOK":str(hook)}
        promoted=subprocess.run(command,text=True,capture_output=True,env=environment)
        self.assertEqual(2,promoted.returncode); self.assertIn("post-push remote verification failed",promoted.stderr); self.assertFalse(output.exists())

        root,_remote,repo,base=self.fixture(); commit,tree=self.candidate(repo,"resumed post-push race"); command,journal,output=self.promote_args(repo,"c0",base,commit,tree)
        interrupted=subprocess.run(command,text=True,capture_output=True,env={**os.environ,"UNINOTAS_HANDOFF_TEST_MODE":"1","UNINOTAS_TEST_AFTER_PUSH_FAILPOINT":"1"}); self.assertEqual(2,interrupted.returncode); self.assertTrue(journal.exists())
        self.git(repo,"push","-q","--force","origin",f"{base}:refs/heads/main"); hook=self.post_push_race_hook(root)
        resumed=subprocess.run(["python3",str(SCRIPT),"resume","--phase","c0","--repo",str(repo),"--journal",str(journal),"--output",str(output)],text=True,capture_output=True,env={**os.environ,"UNINOTAS_HANDOFF_TEST_MODE":"1","UNINOTAS_TEST_POST_PUSH_HOOK":str(hook)})
        self.assertEqual(2,resumed.returncode); self.assertIn("post-push remote verification failed",resumed.stderr); self.assertFalse(output.exists())

    def test_handoff_neg_journal_and_output_must_be_gitignored(self):
        _root,_remote,repo,_base=self.fixture(); (repo/".gitignore").write_text(""); self.git(repo,"add",".gitignore"); self.git(repo,"commit","-qm","remove ignore"); self.git(repo,"push","-q","origin","main"); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); commit,tree=self.candidate(repo); command,_journal,output=self.promote_args(repo,"c0",base,commit,tree)
        result=subprocess.run(command,text=True,capture_output=True)
        self.assertEqual(2,result.returncode); self.assertIn("must be ignored",result.stderr); self.assertFalse(output.exists())

    def test_handoff_neg_verify_and_activate_reject_git_tracked_external_artifacts(self):
        _root,_remote,repo,_base=self.fixture(); tracked=repo/"artifacts/tmp/tracked.json"; tracked.parent.mkdir(parents=True,exist_ok=True); tracked.write_text("{}\n"); self.git(repo,"add","-f",str(tracked.relative_to(repo))); self.git(repo,"commit","-qm","tracked external artifact"); self.git(repo,"push","-q","origin","main")
        verify=subprocess.run(["python3",str(SCRIPT),"verify","--phase","c0","--repo",str(repo),"--phase-evidence",str(tracked),"--delphi-root",str(DELPHI),"--output",str(tracked)],text=True,capture_output=True)
        activate=subprocess.run(["python3",str(SCRIPT),"activate","--phase","c1","--repo",str(repo),"--c0-evidence",str(tracked),"--c0-post-evidence",str(tracked),"--c1-evidence",str(tracked),"--delphi-root",str(DELPHI),"--output",str(tracked)],text=True,capture_output=True)
        self.assertEqual(2,verify.returncode); self.assertIn("must be ignored",verify.stderr)
        self.assertEqual(2,activate.returncode); self.assertIn("must be ignored",activate.stderr)

    def test_handoff_pos_workspace_relative_promote_and_resume_paths(self):
        root,_remote,repo,base=self.fixture(); (root/"uninotas-foundation").symlink_to(repo,target_is_directory=True); commit,tree=self.candidate(repo,"relative c0"); command,journal,output=self.promote_args(repo,"c0",base,commit,tree); command[command.index("--repo")+1]="uninotas-foundation"
        for flag in ("--consumer-bindings","--journal","--output"):
            index=command.index(flag)+1; command[index]=str(pathlib.Path("uninotas-foundation")/pathlib.Path(command[index]).relative_to(repo))
        first=subprocess.run(command,cwd=root,text=True,capture_output=True,env={**os.environ,"UNINOTAS_TEST_AFTER_PUSH_FAILPOINT":"1","UNINOTAS_HANDOFF_TEST_MODE":"1"})
        self.assertEqual(2,first.returncode); self.assertTrue(journal.exists())
        resume=subprocess.run(["python3",str(SCRIPT),"resume","--phase","c0","--repo","uninotas-foundation","--journal",str(pathlib.Path("uninotas-foundation")/journal.relative_to(repo)),"--output",str(pathlib.Path("uninotas-foundation")/output.relative_to(repo))],cwd=root,text=True,capture_output=True)
        self.assertEqual(0,resume.returncode,resume.stderr); self.assertEqual(commit,json.loads(output.read_text())["post_push_remote_main_oid"])

    def test_handoff_pos_workspace_relative_verify_paths(self):
        root,repo,_remote,c0,default_output,head,_tree=self.c0_foundation_fixture(); (root/"uninotas-foundation").symlink_to(repo,target_is_directory=True); (root/"delphi-ai").symlink_to(DELPHI,target_is_directory=True); output=repo/"artifacts/tmp/relative-post.json"
        relative=lambda path:str(pathlib.Path("uninotas-foundation")/path.relative_to(repo))
        command=["python3","uninotas-foundation/deterministic/closeout_handoff.py","verify","--phase","c0","--repo","uninotas-foundation","--phase-evidence",relative(c0),"--delphi-root","delphi-ai","--output",relative(output)]
        result=subprocess.run(command,cwd=root,text=True,capture_output=True)
        self.assertEqual(0,result.returncode,result.stderr); self.assertEqual(head,json.loads(output.read_text())["remote"]); self.assertFalse(default_output.exists())

    def test_handoff_pos_workspace_relative_production_activate_paths(self):
        root,repo,_remote,c0,c0post,c1,_base,head,_tree=self.activation_fixture(); (root/"uninotas-foundation").symlink_to(repo,target_is_directory=True); (root/"delphi-ai").symlink_to(DELPHI,target_is_directory=True); output=repo/"artifacts/tmp/relative-activation.json"
        command=["python3","uninotas-foundation/deterministic/closeout_handoff.py","activate","--phase","c1","--repo","uninotas-foundation","--c0-evidence",str(pathlib.Path("uninotas-foundation")/c0.relative_to(repo)),"--c0-post-evidence",str(pathlib.Path("uninotas-foundation")/c0post.relative_to(repo)),"--c1-evidence",str(pathlib.Path("uninotas-foundation")/c1.relative_to(repo)),"--delphi-root","delphi-ai","--output",str(pathlib.Path("uninotas-foundation")/output.relative_to(repo))]
        result=subprocess.run(command,cwd=root,text=True,capture_output=True)
        self.assertEqual(0,result.returncode,result.stderr); self.assertEqual(head,json.loads(output.read_text())["actual_remote_main_oid"])

    def test_handoff_pos_workspace_relative_recovery_activate_paths(self):
        root,repo,_remote,c0,c0post,failed,c1r,failure,head,_tree=self.recovery_activation_fixture(); (root/"uninotas-foundation").symlink_to(repo,target_is_directory=True); (root/"delphi-ai").symlink_to(DELPHI,target_is_directory=True); output=repo/"artifacts/tmp/relative-recovery.json"
        relative=lambda path:str(pathlib.Path("uninotas-foundation")/path.relative_to(repo))
        command=["python3","uninotas-foundation/deterministic/closeout_handoff.py","activate","--phase","c1r","--repo","uninotas-foundation","--c0-evidence",relative(c0),"--c0-post-evidence",relative(c0post),"--failed-c1-evidence",relative(failed),"--c1r-evidence",relative(c1r),"--failure-tuple",relative(failure),"--delphi-root","delphi-ai","--output",relative(output)]
        result=subprocess.run(command,cwd=root,text=True,capture_output=True)
        self.assertEqual(0,result.returncode,result.stderr); self.assertEqual(head,json.loads(output.read_text())["actual_remote_main_oid"])

    def test_handoff_neg_11_remote_third_oid_is_not_adopted(self):
        root,remote,repo,base=self.fixture(); commit,tree=self.candidate(repo); command,journal,output=self.promote_args(repo,"c0",base,commit,tree)
        subprocess.run(command,text=True,capture_output=True,env={**os.environ,"UNINOTAS_TEST_AFTER_PUSH_FAILPOINT":"1","UNINOTAS_HANDOFF_TEST_MODE":"1"}); third=self.advance_remote(root,remote,"third")
        result=subprocess.run(["python3",str(SCRIPT),"resume","--phase","c0","--repo",str(repo),"--journal",str(journal),"--output",str(output)],text=True,capture_output=True)
        self.assertEqual(2,result.returncode); self.assertIn("remote third OID prevents resume",result.stderr); self.assertNotEqual(third,commit)

    def assert_race_rejected(self, phase, known_advance=False):
        root,remote,repo,base=self.fixture()
        if known_advance:
            advance=self.candidate(repo,"known-advance")[0]; self.git(repo,"push","-q","origin","main"); self.git(repo,"reset","--hard",base)
        commit,tree=self.candidate(repo,phase); advanced=self.advance_remote(root,remote,"race")
        command,_,output=self.promote_args(repo,phase,base,commit,tree); result=subprocess.run(command,text=True,capture_output=True)
        self.assertEqual(2,result.returncode); self.assertIn("local-unpublished-diverged",result.stderr); self.assertFalse(output.exists()); self.assertNotEqual(advanced,commit)

    def test_remote_neg_01_c0_sibling_advance_rejects_lease(self): self.assert_race_rejected("c0")
    def test_remote_neg_02_c1_sibling_advance_rejects_lease(self): self.assert_race_rejected("c1")
    def test_remote_neg_04_known_local_history_advance_rejects_lease(self): self.assert_race_rejected("c0",known_advance=True)

    def test_tree_pos_01_staged_candidate_tree_matches_commit_tree(self):
        root,remote,repo,base=self.fixture(); (repo/"item").write_text("staged"); self.git(repo,"add","item"); candidate=self.git(repo,"write-tree").stdout.strip(); self.git(repo,"commit","-qm","staged"); commit=self.git(repo,"rev-parse","HEAD").stdout.strip()
        self.assertEqual(candidate,self.git(repo,"rev-parse","HEAD^{tree}").stdout.strip()); command,_,output=self.promote_args(repo,"c0",base,commit,candidate); result=subprocess.run(command,text=True,capture_output=True); self.assertEqual(0,result.returncode,result.stderr); self.assertEqual(candidate,json.loads(output.read_text())["candidate_tree"])

    def test_tree_pos_02_delivery_baseline_precedes_base_head(self):
        root,remote,repo,delivery_base=self.fixture(); (repo/"delivery.txt").write_text("earlier"); self.git(repo,"add","delivery.txt"); self.git(repo,"commit","-qm","delivery"); self.git(repo,"push","-q","origin","main"); base=self.git(repo,"rev-parse","HEAD").stdout.strip(); commit,tree=self.candidate(repo,"phase")
        delivery_paths=self.git(repo,"diff","--no-renames","--name-only",delivery_base,commit).stdout.splitlines(); phase_paths=self.git(repo,"diff","--no-renames","--name-only",base,commit).stdout.splitlines()
        self.assertIn("delivery.txt",delivery_paths); self.assertNotIn("delivery.txt",phase_paths); self.assertEqual(["item"],phase_paths); command,_,_=self.promote_args(repo,"c0",base,commit,tree); command[command.index("--delivery-baseline")+1]=delivery_base; review_path=pathlib.Path(command[command.index("--implementation-reviews")+1]); review_path.write_text(json.dumps(self.implementation_reviews(tree,delivery_paths))); self.assertEqual(0,subprocess.run(command,text=True,capture_output=True).returncode)

    def test_tree_neg_01_authorized_change_left_unstaged(self):
        root,remote,repo,base=self.fixture(); commit,tree=self.candidate(repo); (repo/"item").write_text("unstaged"); command,_,_=self.promote_args(repo,"c0",base,commit,tree); result=subprocess.run(command,text=True,capture_output=True); self.assertEqual(2,result.returncode); self.assertIn("working tree differs from validated candidate index",result.stderr)

    def test_tree_neg_02_unrelated_path_pre_staged(self):
        root,remote,repo,base=self.fixture(); commit,tree=self.candidate(repo); (repo/"unrelated.txt").write_text("staged"); self.git(repo,"add","unrelated.txt"); command,_,_=self.promote_args(repo,"c0",base,commit,tree); result=subprocess.run(command,text=True,capture_output=True); self.assertEqual(2,result.returncode); self.assertIn("staged candidate contains path outside phase allowlist",result.stderr)

    def test_tree_neg_03_candidate_mutation_after_validation(self):
        root,remote,repo,base=self.fixture(); commit,tree=self.candidate(repo); (repo/"item").write_text("mutated-after-capture"); self.git(repo,"add","item"); command,_,_=self.promote_args(repo,"c0",base,commit,tree); result=subprocess.run(command,text=True,capture_output=True); self.assertEqual(2,result.returncode); self.assertIn("candidate tree changed after final validation",result.stderr)

    def test_tree_neg_04_commit_tree_differs_from_captured_candidate(self):
        root,remote,repo,base=self.fixture(); commit,tree=self.candidate(repo); wrong_tree=self.git(repo,"rev-parse",base+"^{tree}").stdout.strip(); command,_,_=self.promote_args(repo,"c0",base,commit,wrong_tree); result=subprocess.run(command,text=True,capture_output=True); self.assertEqual(2,result.returncode); self.assertIn("commit tree does not match validated candidate tree",result.stderr)

    def test_handoff_pos_04_c0_post_publish_verification_chain(self):
        root,repo,remote,evidence,output,head,tree=self.c0_foundation_fixture(); result=self.verify_c0(repo,evidence,output)
        self.assertEqual(0,result.returncode,result.stderr); actual=json.loads(output.read_text()); self.assertEqual({"schema","phase","commit","tree","remote","clean","foundation_validator","active_path_state","active_todo_count","active_paths","consumer_bindings"},set(actual)); self.assertEqual((head,tree,head),(actual["commit"],actual["tree"],actual["remote"])); self.assertEqual("active",actual["active_path_state"]); self.assertEqual(2,actual["active_todo_count"]); self.assertEqual(["foundation-validator-c0-post","active-path-closeout-c0-post","active-set-scan-c0-post"],[row["consumer_id"] for row in actual["consumer_bindings"]])

    def test_handoff_neg_10_c0_post_rejects_invalid_inputs(self):
        cases=("absent","wrong_tree","non_active","wrong_count","dirty","remote")
        for case in cases:
            with self.subTest(case=case):
                root,repo,remote,evidence,output,head,tree=self.c0_foundation_fixture()
                if case=="absent": evidence.unlink()
                elif case=="wrong_tree": evidence.write_text(json.dumps({"phase":"c0","new_commit":head,"candidate_tree":"a"*40,"post_push_remote_main_oid":head}))
                elif case=="non_active": self.git(repo,"mv","todos/active/process/TODO-uninotas-canonical-foundation-transition.md","todos/completed/process/TODO-uninotas-canonical-foundation-transition.md")
                elif case=="wrong_count": (repo/"todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md").unlink()
                elif case=="dirty": (repo/"dirty.txt").write_text("dirty")
                elif case=="remote": self.advance_remote(root,remote,"remote-advance")
                result=self.verify_c0(repo,evidence,output); self.assertEqual(2,result.returncode); self.assertFalse(output.exists())

    def test_handoff_neg_strict_json_rejects_duplicate_members_and_nonfinite_numbers(self):
        module=self.handoff_module()
        with tempfile.TemporaryDirectory() as temporary:
            root=pathlib.Path(temporary)
            for name,payload in (("duplicate.json",'{"phase":"c0","phase":"c1"}'),("nonfinite.json",'{"value":NaN}')):
                with self.subTest(name=name):
                    path=root/name; path.write_text(payload)
                    with self.assertRaisesRegex(ValueError,"invalid JSON input"): module.load_json(path)

    def test_handoff_neg_phase_c0post_bridge_and_failure_schemas_reject_unknown_members(self):
        _root,repo,_remote,evidence,output,_head,_tree=self.c0_foundation_fixture()
        value=json.loads(evidence.read_text()); value["unexpected"]=True; evidence.write_text(json.dumps(value))
        result=self.verify_c0(repo,evidence,output)
        self.assertEqual(2,result.returncode); self.assertIn("phase evidence is not a published exact commit",result.stderr); self.assertFalse(output.exists())

        _root,repo,_remote,c0,c0post,c1,_base,_head,_tree=self.activation_fixture(); value=json.loads(c0post.read_text()); value["unexpected"]=True; c0post.write_text(json.dumps(value)); output=repo/"artifacts/tmp/unknown-c0post.json"
        result=self.activate_c1(repo,c0,c0post,c1,output)
        self.assertEqual(2,result.returncode); self.assertIn("incomplete or incompatible phase chain",result.stderr); self.assertFalse(output.exists())

        _root,repo,_remote,c0,c0post,c1,_base,_head,_tree=self.activation_fixture(); value=json.loads(c1.read_text()); value["proof_bridge"]["unexpected"]=True; c1.write_text(json.dumps(value)); result=self.activate_c1(repo,c0,c0post,c1,repo/"artifacts/tmp/unknown-bridge.json")
        self.assertEqual(2,result.returncode); self.assertIn("incomplete or incompatible phase chain",result.stderr)

        _root,_remote,repo,base=self.fixture(); failed,_tree=self.candidate(repo,"failed c1"); self.git(repo,"push","-q","origin","main"); c1r,tree=self.candidate(repo,"c1r schema"); command,_journal,output=self.promote_args(repo,"c1r",failed,c1r,tree); failure=pathlib.Path(command[command.index("--failure-tuple")+1]); value=json.loads(failure.read_text()); value["unexpected"]=True; failure.write_text(json.dumps(value)); result=subprocess.run(command,text=True,capture_output=True)
        self.assertEqual(2,result.returncode); self.assertIn("failure tuple schema is invalid",result.stderr); self.assertFalse(output.exists())

    def test_closeout_neg_active_scan_requires_exact_count_and_exact_path_set_in_all_phases(self):
        transition="todos/active/process/TODO-uninotas-canonical-foundation-transition.md"; discovery="todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md"; rogue="todos/active/process/TODO-rogue.md"

        root,repo,_remote,evidence,output,_head,_tree=self.c0_foundation_fixture(); fake=self.fake_delphi_guard(root,20,[transition,discovery]); result=self.verify_c0(repo,evidence,output,fake)
        self.assertEqual(2,result.returncode); self.assertIn("C0 semantic validator or active TODO scan failed",result.stderr); self.assertFalse(output.exists())

        root,repo,_remote,c0,c0post,c1,_base,_head,_tree=self.activation_fixture(); fake=self.fake_delphi_guard(root,10,[discovery,rogue]); output=repo/"artifacts/tmp/c1-wrong-scan.json"; result=self.activate_c1(repo,c0,c0post,c1,output,fake)
        self.assertEqual(2,result.returncode); self.assertIn("C1 active TODO scan failed",result.stderr); self.assertFalse(output.exists())

        root,repo,_remote,c0,c0post,failed,c1r,failure,_head,_tree=self.recovery_activation_fixture(); fake=self.fake_delphi_guard(root,2,[transition,rogue]); output=repo/"artifacts/tmp/c1r-wrong-scan.json"; result=self.activate_c1r(repo,c0,c0post,failed,c1r,failure,output,fake)
        self.assertEqual(2,result.returncode); self.assertIn("C1R active TODO scan failed",result.stderr); self.assertFalse(output.exists())

    def test_handoff_neg_01_03_04_09_c0_consumer_catalog(self):
        mutations={
            "HANDOFF-NEG-01":lambda rows: rows.__setitem__(0,{**rows[0],"binding_subject":"OTHER_TREE"}),
            "HANDOFF-NEG-03":lambda rows: rows.pop(),
            "HANDOFF-NEG-04":lambda rows: rows.append(rows[0]),
            "HANDOFF-NEG-09":lambda rows: rows.__setitem__(0,{**rows[0],"change_scope_source":"PHASE_COMMIT_DELTA_SET"}),
        }
        for case,mutate in mutations.items():
            with self.subTest(case=case):
                root,remote,repo,base=self.fixture(); commit,tree=self.candidate(repo,case); command,_,_=self.promote_args(repo,"c0",base,commit,tree); binding_path=pathlib.Path(command[command.index("--consumer-bindings")+1]); rows=json.loads(binding_path.read_text()); mutate(rows); binding_path.write_text(json.dumps(rows)); result=subprocess.run(command,text=True,capture_output=True); self.assertEqual(2,result.returncode); self.assertIn("C0 consumer bindings must exactly match the canonical catalog",result.stderr)

    def test_c0_promote_rejects_declared_go_when_live_authority_guard_fails(self):
        root,_remote,repo,base=self.fixture(); commit,tree=self.candidate(repo,"contradictory binding")
        command,_journal,output=self.promote_args(repo,"c0",base,commit,tree)
        command[command.index("--delphi-root")+1]=str(self.fake_c0_delphi_gates(root,"todo_authority_guard.py"))
        result=subprocess.run(command,text=True,capture_output=True)
        self.assertEqual(2,result.returncode)
        self.assertIn("C0 live gate failed: todo-authority-c0",result.stderr)
        self.assertFalse(output.exists())

    def test_c0_promote_accepts_exact_delivery_tree_with_real_delphi_guards(self):
        self.assertEqual(0,subprocess.run(["git","-C",str(FOUNDATION),"diff","--quiet","--"],capture_output=True).returncode,"source worktree must equal its staged index")
        source_tree=self.git(FOUNDATION,"write-tree").stdout.strip()
        with tempfile.TemporaryDirectory() as temporary:
            root=pathlib.Path(temporary); repo=root/"foundation"; remote=root/"remote.git"; archive=root/"candidate.tar"
            subprocess.run(["git","clone","-q",str(FOUNDATION),str(repo)],check=True)
            subprocess.run(["git","init","--bare","-q",str(remote)],check=True)
            self.git(repo,"config","user.email","test@example.invalid"); self.git(repo,"config","user.name","Test")
            base=self.git(repo,"rev-parse","HEAD").stdout.strip(); self.git(repo,"remote","set-url","origin",str(remote)); self.git(repo,"push","-q","origin","HEAD:main"); subprocess.run(["git","-C",str(remote),"symbolic-ref","HEAD","refs/heads/main"],check=True)
            subprocess.run(["git","-C",str(FOUNDATION),"archive","--format=tar",f"--output={archive}",source_tree],check=True)
            self.git(repo,"rm","-rq",".")
            with tarfile.open(archive) as candidate:
                members=candidate.getmembers(); self.assertTrue(all(not pathlib.PurePosixPath(member.name).is_absolute() and ".." not in pathlib.PurePosixPath(member.name).parts for member in members)); candidate.extractall(repo,members=members,filter="data")
            self.git(repo,"add","-A"); self.assertEqual(source_tree,self.git(repo,"write-tree").stdout.strip()); self.git(repo,"commit","-qm","exact C0 candidate")
            commit=self.git(repo,"rev-parse","HEAD").stdout.strip(); tree=self.git(repo,"rev-parse","HEAD^{tree}").stdout.strip(); self.assertEqual(source_tree,tree)
            baseline=self.handoff_module().DELIVERY_BASELINE; scope=self.git(repo,"diff","--no-renames","--name-only",baseline,commit).stdout.splitlines(); tmp=repo/"artifacts/tmp"; tmp.mkdir(parents=True,exist_ok=True)
            bindings=tmp/"c0-bindings.json"; reviews=tmp/"c0-implementation-reviews.json"; journal=tmp/"c0-intent.json"; output=tmp/"c0-promotion.json"
            bindings.write_text(json.dumps(self.c0_bindings())); reviews.write_text(json.dumps(self.implementation_reviews(tree,scope)))
            command=[sys.executable,str(SCRIPT),"promote","--phase","c0","--repo",str(repo),"--expected-remote",base,"--new-commit",commit,"--candidate-tree",tree,"--delivery-baseline",baseline,"--consumer-bindings",str(bindings),"--implementation-reviews",str(reviews),"--delphi-root",str(DELPHI),"--journal",str(journal),"--output",str(output)]
            result=subprocess.run(command,text=True,capture_output=True)
            self.assertEqual(0,result.returncode,f"stdout={result.stdout}\nstderr={result.stderr}")
            evidence=json.loads(output.read_text()); live={row["consumer_id"]:row for row in evidence["live_gate_evidence"]}; expected=dict(self.handoff_module().c0_live_gate_commands(repo,DELPHI))
            self.assertEqual(set(self.handoff_module().LIVE_GATE_IDS),set(live)); self.assertTrue(all(live[identifier]["command"]==expected[identifier] and live[identifier]["outcome"]=="go" for identifier in expected)); self.assertEqual(tree,evidence["candidate_tree"])

    def c1_command(self):
        root,remote,repo,base=self.fixture(); commit,tree=self.candidate(repo,"c1"); command,_,_=self.promote_args(repo,"c1",base,commit,tree); return repo,command
    def test_tree_pos_03_implementation_carry_and_focused_c1_binding(self):
        _root,_repo,_remote,_c0,_c0post,c1,_base,_head,_tree=self.activation_fixture(); evidence=json.loads(c1.read_text()); self.assertEqual(evidence["proof_inputs"]["implementation_reviews"],evidence["proof_bridge"]["implementation_reviews"]); self.assertEqual(evidence["proof_inputs"]["focused_review"],evidence["proof_bridge"]["focused_review"])
    def test_tree_neg_05_stale_worktree_proxy_tree(self):
        repo,command=self.c1_command(); path=pathlib.Path(command[command.index("--consumer-bindings")+1]); rows=json.loads(path.read_text()); rows[1]["binding_subject"]="STALE_TREE"; path.write_text(json.dumps(rows)); result=subprocess.run(command,text=True,capture_output=True); self.assertEqual(2,result.returncode); self.assertIn("C1 consumer bindings",result.stderr)
    def test_tree_neg_06_stale_human_attestation(self):
        _root,repo,_remote,c0,c0post,c1,_base,_head,_tree=self.activation_fixture(); value=json.loads(c1.read_text()); value["proof_inputs"]["implementation_reviews"][0]["candidate_tree_oid"]="a"*40; c1.write_text(json.dumps(value)); result=self.activate_c1(repo,c0,c0post,c1,repo/"artifacts/tmp/stale-review.json"); self.assertEqual(2,result.returncode); self.assertIn("incomplete or incompatible phase chain",result.stderr)
    def test_tree_neg_07_absent_or_invalid_bridge(self):
        repo,command=self.c1_command(); index=command.index("--implementation-reviews"); del command[index:index+2]; result=subprocess.run(command,text=True,capture_output=True); self.assertNotEqual(0,result.returncode)
    def test_tree_neg_08_focused_review_wrong_tree_or_path_set(self):
        _root,repo,_remote,c0,c0post,c1,_base,_head,_tree=self.activation_fixture(); value=json.loads(c1.read_text()); value["proof_inputs"]["focused_review"]["exact_path_set"]=["wrong"]; c1.write_text(json.dumps(value)); result=self.activate_c1(repo,c0,c0post,c1,repo/"artifacts/tmp/wrong-focused.json"); self.assertEqual(2,result.returncode); self.assertIn("incomplete or incompatible phase chain",result.stderr)
    def test_c1r_promote_rejects_failure_tuple_mismatch_with_candidate_and_bridge(self):
        _root,_remote,repo,base=self.fixture(); failed,_tree=self.candidate(repo,"failed c1"); self.git(repo,"push","-q","origin","main"); c1r,tree=self.candidate(repo,"c1r mismatch"); command,_journal,output=self.promote_args(repo,"c1r",failed,c1r,tree); path=pathlib.Path(command[command.index("--failure-tuple")+1]); value=json.loads(path.read_text()); value["predicate"]="parent_mismatch"; path.write_text(json.dumps(value)); result=subprocess.run(command,text=True,capture_output=True)
        self.assertEqual(2,result.returncode); self.assertIn("does not match candidate",result.stderr); self.assertFalse(output.exists())
    def test_handoff_pos_03_production_partition_excludes_c1r(self): self.assertIsNone(self.handoff_module().validate_production_handoff(self.production_fixture()))
    def test_handoff_neg_02_commit_tree_mismatch(self):
        fixture=self.production_fixture(); fixture["c1"]["commit_tree_oid"]="e"*40; self.assertIn("commit tree unequal",self.handoff_module().validate_production_handoff(fixture))
    def test_handoff_neg_05_contradictory_c0_cas_evidence(self):
        fixture=self.production_fixture(); fixture["remote_promotions"]["c0"]["post_push_remote_main_oid"]="f"*40; self.assertIn("complete C0",self.handoff_module().validate_production_handoff(fixture))
    def test_handoff_neg_production_serialized_schema_mutations(self):
        mutations=(
            lambda value:value["proof_bridge"].__setitem__("exact_delta_set",["wrong"]),
            lambda value:value["c0_post_verify"].__setitem__("remote_main_oid","f"*40),
            lambda value:value["post_c1_active_scan"].__setitem__("todo_count",2),
            lambda value:value.__setitem__("actual_remote_main_oid","f"*40),
            lambda value:value["remote_promotions"]["c1"].__setitem__("post_push_remote_main_oid","f"*40),
            lambda value:value["c1"].__setitem__("delivery_scope_set",["wrong","wrong"]),
            lambda value:value.__setitem__("unexpected",True),
        )
        for mutate in mutations:
            value=self.production_fixture(); mutate(value); self.assertIsNotNone(self.handoff_module().validate_production_handoff(value))
    def recovery_fixture(self):
        parent="0"*40; c0="e"*40; c0tree="f"*40; c1="c"*40; c1tree="d"*40; c1r="a"*40; tree="b"*40
        record=lambda commit,tree,parent_oid,delta:{"commit_oid":commit,"candidate_tree_oid":tree,"commit_tree_oid":tree,"tree_equal":True,"parent_oid":parent_oid,"delivery_scope_set":["delivery"],"phase_commit_delta_set":delta}
        promotion=lambda expected,commit:{"fresh_pre_push_oid":expected,"expected_lease_oid":expected,"lease_result":"success","promotion_observation":"fresh_pre_push","parent_and_fast_forward":True,"post_push_remote_main_oid":commit,"local_head_oid":commit,"local_tracking_oid":commit}
        active=["todos/active/process/TODO-uninotas-canonical-foundation-transition.md","todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md"]
        failure=self.failure_tuple(c1); reverse={"validator":"validate_closeout_diff.py","base_commit_oid":c1,"base_tree_oid":c1tree,"candidate_tree_oid":tree,"exact_delta_set":["x"],"outcome":"go","failure_tuple":dict(failure)}
        return {"schema":"uninotas-closeout-handoff-v1","handoff_kind":"recovery","c0":record(c0,c0tree,parent,["delivery"]),"c1":record(c1,c1tree,c0,["closeout"]),"c1r":record(c1r,tree,c1,["x"]),"consumer_bindings":self.c0_bindings()+self.c0post_bindings()+self.c1_bindings()+self.c1r_bindings(),"reverse_bridge":reverse,"failure_tuple":failure,"remote_promotions":{"c0":promotion(parent,c0),"c1":promotion(c0,c1),"c1r":promotion(c1,c1r)},"c0_post_verify":{"head_oid":c0,"commit_tree_oid":c0tree,"remote_main_oid":c0,"checkout_clean":True,"foundation_validator":"go","active_path_state":"active","active_todo_count":2,"active_paths":active},"post_c1r_active_scan":{"scanned_head_oid":c1r,"outcome":"go","todo_count":2,"active_paths":active,"stale_completed_path":False},"actual_remote_main_oid":c1r,"recovery_effective":True,"production_ready_effective":False}
    def test_handoff_pos_02_complete_c1r_recovery_handoff(self): self.assertIsNone(self.handoff_module().validate_recovery_handoff(self.recovery_fixture()))
    def test_handoff_neg_recovery_serialized_schema_mutations(self):
        mutations=(
            lambda value:value["reverse_bridge"].__setitem__("exact_delta_set",["wrong"]),
            lambda value:value["c0_post_verify"].__setitem__("checkout_clean",False),
            lambda value:value["post_c1r_active_scan"].__setitem__("stale_completed_path",True),
            lambda value:value.__setitem__("actual_remote_main_oid","f"*40),
            lambda value:value["remote_promotions"]["c1"].__setitem__("expected_lease_oid","f"*40),
            lambda value:value["c1r"].__setitem__("phase_commit_delta_set",["wrong"]),
            lambda value:value["failure_tuple"].__setitem__("predicate","fabricated_but_schema_valid"),
            lambda value:value["reverse_bridge"]["failure_tuple"].__setitem__("predicate","parent_mismatch"),
            lambda value:value.__setitem__("unexpected",True),
        )
        for mutate in mutations:
            value=self.recovery_fixture(); mutate(value); self.assertIsNotNone(self.handoff_module().validate_recovery_handoff(value))
    def test_c1r_catalog_and_recovery_negative_schema(self):
        mutations={
            "missing":lambda value:value["consumer_bindings"].pop(),
            "extra":lambda value:value["consumer_bindings"].append({"consumer_id":"extra"}),
            "duplicate":lambda value:value["consumer_bindings"].append(dict(value["consumer_bindings"][0])),
            "wrong_phase":lambda value:value["consumer_bindings"].__setitem__(-1,{**value["consumer_bindings"][-1],"phase":"C1"}),
            "wrong_class":lambda value:value["consumer_bindings"].__setitem__(-1,{**value["consumer_bindings"][-1],"class":"worktree-proxy"}),
            "wrong_scope":lambda value:value["consumer_bindings"].__setitem__(-1,{**value["consumer_bindings"][-1],"scope":"closeout_transform"}),
            "wrong_binding":lambda value:value["consumer_bindings"].__setitem__(-1,{**value["consumer_bindings"][-1],"binding_subject":"C1_CANDIDATE_TREE"}),
            "wrong_source":lambda value:value["consumer_bindings"].__setitem__(-1,{**value["consumer_bindings"][-1],"change_scope_source":"DELIVERY_SCOPE_SET"}),
            "wrong_outcome":lambda value:value["consumer_bindings"].__setitem__(-1,{**value["consumer_bindings"][-1],"outcome":"go"}),
            "invalid_failure_tuple":lambda value:value.__setitem__("failure_tuple",{"failure_id":"bad","failed_c1_oid":"bad","predicate":"fabricated","observed":"bad","recorded_at_utc":"bad"}),
            "production_ready":lambda value:value.__setitem__("production_ready_effective",True),
        }
        for case,mutate in mutations.items():
            with self.subTest(case=case): value=self.recovery_fixture(); mutate(value); self.assertIsNotNone(self.handoff_module().validate_recovery_handoff(value))

    def test_remote_pos_01_and_handoff_pos_01_c1_activation(self):
        _root,repo,_remote,c0,c0post,c1,_base,head,tree=self.activation_fixture(); output=repo/"artifacts/tmp/activation.json"
        result=self.activate_c1(repo,c0,c0post,c1,output)
        self.assertEqual(0,result.returncode,result.stderr)
        evidence=json.loads(output.read_text())
        self.assertEqual("uninotas-closeout-handoff-v1",evidence["schema"])
        self.assertEqual((head,tree,head),(evidence["c1"]["commit_oid"],evidence["c1"]["candidate_tree_oid"],evidence["actual_remote_main_oid"]))
        self.assertIsNone(self.handoff_module().validate_production_handoff(evidence))

    def test_closeout_pos_03_c1_scan_has_exact_discovery_successor(self):
        _root,repo,_remote,c0,c0post,c1,_base,head,_tree=self.activation_fixture(); output=repo/"artifacts/tmp/activation.json"
        self.assertEqual(0,self.activate_c1(repo,c0,c0post,c1,output).returncode)
        evidence=json.loads(output.read_text())
        scan=evidence["post_c1_active_scan"]
        self.assertEqual((head,"go",1,["todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md"],False),(scan["scanned_head_oid"],scan["outcome"],scan["todo_count"],scan["active_paths"],scan["stale_transition_path"]))

    def test_remote_neg_03_c1_activation_rejects_fresh_remote_mismatch(self):
        root,repo,remote,c0,c0post,c1,_base,_head,_tree=self.activation_fixture(); self.advance_remote(root,remote,"remote-race"); output=repo/"artifacts/tmp/activation.json"
        result=self.activate_c1(repo,c0,c0post,c1,output)
        self.assertEqual(2,result.returncode); self.assertIn("activation remote or clean-tree binding failed",result.stderr); self.assertFalse(output.exists())

    def test_handoff_neg_08_c1_activation_rejects_noncanonical_production_input(self):
        _root,repo,_remote,c0,c0post,c1,_base,_head,_tree=self.activation_fixture(); value=json.loads(c0.read_text()); value["consumer_bindings"][0]["outcome"]="no_material_findings"; c0.write_text(json.dumps(value)); output=repo/"artifacts/tmp/activation.json"
        result=self.activate_c1(repo,c0,c0post,c1,output)
        self.assertEqual(2,result.returncode); self.assertIn("incomplete or incompatible phase chain",result.stderr)

    def test_closeout_neg_07_c1_activation_rejects_stale_transition_active(self):
        _root,repo,_remote,_c0,_c0post,c1,_base,_head,_tree=self.activation_fixture(transition_completed=False)
        self.assertFalse(c1.exists())

    def test_closeout_neg_15_c1_activation_rejects_dirty_untracked_checkout(self):
        _root,repo,_remote,c0,c0post,c1,_base,_head,_tree=self.activation_fixture(); (repo/"untracked.txt").write_text("dirty\n"); output=repo/"artifacts/tmp/activation.json"
        result=self.activate_c1(repo,c0,c0post,c1,output)
        self.assertEqual(2,result.returncode); self.assertIn("activation remote or clean-tree binding failed",result.stderr); self.assertFalse(output.exists())

    def test_handoff_neg_path_python_substitution_is_not_used_by_verify_or_activation(self):
        def run_path_safe(root,command):
            fake_bin=root/"fake-bin"; fake_bin.mkdir(exist_ok=True); fake_python=fake_bin/"python3"; marker=root/"fake-python-ran"; fake_python.write_text(f"#!/bin/sh\ntouch '{marker}'\nexit 0\n"); fake_python.chmod(0o755)
            result=subprocess.run(command,text=True,capture_output=True,env={**os.environ,"PATH":str(fake_bin)+os.pathsep+os.environ.get("PATH","")}); self.assertEqual(0,result.returncode,result.stderr); self.assertFalse(marker.exists())
        root,repo,_remote,c0,c0post,c1,_base,_head,_tree=self.activation_fixture(); output=repo/"artifacts/tmp/path-safe-activation.json"
        run_path_safe(root,[sys.executable,str(SCRIPT),"activate","--phase","c1","--repo",str(repo),"--c0-evidence",str(c0),"--c0-post-evidence",str(c0post),"--c1-evidence",str(c1),"--delphi-root",str(DELPHI),"--output",str(output)])
        root,repo,_remote,c0,output,_head,_tree=self.c0_foundation_fixture(); verified=repo/"artifacts/tmp/path-safe-c0-post.json"
        run_path_safe(root,[sys.executable,str(SCRIPT),"verify","--phase","c0","--repo",str(repo),"--phase-evidence",str(c0),"--delphi-root",str(DELPHI),"--output",str(verified)])
        root,repo,_remote,c0,c0post,failed,c1r,failure,_head,_tree=self.recovery_activation_fixture(); output=repo/"artifacts/tmp/path-safe-recovery.json"
        run_path_safe(root,[sys.executable,str(SCRIPT),"activate","--phase","c1r","--repo",str(repo),"--c0-evidence",str(c0),"--c0-post-evidence",str(c0post),"--failed-c1-evidence",str(failed),"--c1r-evidence",str(c1r),"--failure-tuple",str(failure),"--delphi-root",str(DELPHI),"--output",str(output)])

    def test_handoff_pos_02_and_closeout_pos_04_c1r_activation(self):
        _root,repo,_remote,c0,c0post,failed,c1r,failure,head,tree=self.recovery_activation_fixture(); output=repo/"artifacts/tmp/recovery-activation.json"
        result=self.activate_c1r(repo,c0,c0post,failed,c1r,failure,output)
        self.assertEqual(0,result.returncode,result.stderr); evidence=json.loads(output.read_text())
        scan=evidence["post_c1r_active_scan"]
        self.assertEqual(("uninotas-closeout-handoff-v1",head,tree,"go",2,True,False),(evidence["schema"],evidence["c1r"]["commit_oid"],evidence["c1r"]["candidate_tree_oid"],scan["outcome"],scan["todo_count"],evidence["recovery_effective"],evidence["production_ready_effective"]))
        self.assertEqual(json.loads(failure.read_text()),evidence["failure_tuple"])
        self.assertIsNone(self.handoff_module().validate_recovery_handoff(evidence))

    def test_c1r_promote_uses_fresh_remote_failed_c1_when_tracking_is_stale(self):
        _root,_repo,_remote,_c0,_c0post,_failed,evidence,_failure,c1r,_tree=self.recovery_activation_fixture(stale_tracking=True)
        self.assertEqual(c1r,json.loads(evidence.read_text())["post_push_remote_main_oid"])

    def test_handoff_neg_06_c1r_activation_rejects_mutable_failure_tuple(self):
        _root,repo,_remote,c0,c0post,failed,c1r,failure,_head,_tree=self.recovery_activation_fixture(); value=json.loads(failure.read_text()); value["predicate"]="parent_mismatch"; failure.write_text(json.dumps(value)); output=repo/"artifacts/tmp/recovery-activation.json"
        result=self.activate_c1r(repo,c0,c0post,failed,c1r,failure,output)
        self.assertEqual(2,result.returncode); self.assertIn("incomplete or incompatible recovery chain",result.stderr); self.assertFalse(output.exists())

    def test_handoff_neg_07_c1r_activation_rejects_wrong_recovery_catalog(self):
        _root,repo,_remote,c0,c0post,failed,c1r,failure,_head,_tree=self.recovery_activation_fixture(); value=json.loads(c1r.read_text()); value["consumer_bindings"][-1]["outcome"]="go"; c1r.write_text(json.dumps(value)); output=repo/"artifacts/tmp/recovery-activation.json"
        result=self.activate_c1r(repo,c0,c0post,failed,c1r,failure,output)
        self.assertEqual(2,result.returncode); self.assertIn("incomplete or incompatible recovery chain",result.stderr)

    def test_closeout_neg_11_c1r_activation_rejects_completed_transition(self):
        _root,repo,_remote,c0,c0post,failed,c1r,failure,_head,_tree=self.recovery_activation_fixture(completed_transition=True); output=repo/"artifacts/tmp/recovery-activation.json"
        result=self.activate_c1r(repo,c0,c0post,failed,c1r,failure,output)
        self.assertEqual(2,result.returncode); self.assertIn("incomplete or incompatible recovery chain",result.stderr); self.assertFalse(output.exists())

    def test_closeout_neg_13_c1r_activation_rejects_dirty_checkout(self):
        _root,repo,_remote,c0,c0post,failed,c1r,failure,_head,_tree=self.recovery_activation_fixture(); (repo/"dirty-c1r.txt").write_text("dirty\n"); output=repo/"artifacts/tmp/recovery-activation.json"
        result=self.activate_c1r(repo,c0,c0post,failed,c1r,failure,output)
        self.assertEqual(2,result.returncode); self.assertIn("activation remote or clean-tree binding failed",result.stderr); self.assertFalse(output.exists())

    def test_closeout_pos_02_candidate_tree_is_immutable_across_real_closeout_guards(self):
        _root,repo,_remote,_c0,_c0post,_c1,_base,head,tree=self.activation_fixture(); completed="todos/completed/process/TODO-uninotas-canonical-foundation-transition.md"
        reviews=repo/"artifacts/tmp/implementation-reviews.json"; focused=repo/"artifacts/tmp/c1-focused-review.json"
        commands=(
            ["python3","-B",str(FOUNDATION/"deterministic/validate_foundation.py"),"--root",str(repo)],
            ["python3","-B",str(FOUNDATION/"deterministic/validate_closeout_diff.py"),"--repo",str(repo),"--base",head+"^","--candidate-tree",tree,"--todo",completed,"--implementation-reviews",str(reviews),"--focused-review",str(focused)],
            ["python3","-B",str(DELPHI/"tools/todo_deterministic_validator.py"),"--todo",completed],
            ["python3","-B",str(DELPHI/"tools/todo_authority_guard.py"),completed,"--require-delivery-gates"],
            ["python3","-B",str(DELPHI/"tools/todo_completion_guard.py"),completed,"--require-delivery"],
            ["python3","-B",str(DELPHI/"tools/todo_closeout_guard.py"),"--all-active","--repo","."],
        )
        results=[subprocess.run(command,cwd=repo,text=True,capture_output=True) for command in commands]
        self.assertEqual(6,len(results))
        for command,result in zip(commands,results): self.assertEqual(0,result.returncode,f"{' '.join(command)}\nstdout={result.stdout}\nstderr={result.stderr}")
        self.assertIn("Foundation validation passed",results[0].stdout); self.assertEqual("go",json.loads(results[1].stdout)["outcome"]); self.assertIn("Result: PASS",results[2].stdout); self.assertIn("Overall outcome: go",results[-1].stdout)
        self.assertEqual(tree,self.git(repo,"write-tree").stdout.strip()); self.assertEqual(tree,self.git(repo,"rev-parse","HEAD^{tree}").stdout.strip())

    def test_closeout_neg_14_unpublished_c0_c1_remote_race_blocks_c1r_shortcut(self):
        root,remote,repo,base=self.fixture(); c0,_tree0=self.candidate(repo,"unpublished c0"); c1,_tree1=self.candidate(repo,"unpublished c1"); c1r,tree1r=self.candidate(repo,"attempted c1r")
        self.advance_remote(root,remote,"remote race"); command,_journal,output=self.promote_args(repo,"c1r",c1,c1r,tree1r)
        result=subprocess.run(command,text=True,capture_output=True)
        self.assertEqual(2,result.returncode); self.assertIn("reconciliation, rebaseline, and renewed approval required",result.stderr); self.assertFalse(output.exists()); self.assertNotEqual(c0,self.git(repo,"ls-remote","origin","refs/heads/main").stdout.split()[0]); self.assertNotEqual(c1,self.git(repo,"ls-remote","origin","refs/heads/main").stdout.split()[0])
