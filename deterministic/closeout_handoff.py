#!/usr/bin/env python3
"""Strict, durable closeout phase evidence with expected-value CAS promotion."""
import argparse, hashlib, json, os, pathlib, re, subprocess, sys, tempfile

PHASES={"c0","c1","c1r"}
OID_RE=__import__("re").compile(r"^[0-9a-f]{40}$")
ACTIVE_TODO="todos/active/process/TODO-uninotas-canonical-foundation-transition.md"
COMPLETED_TODO="todos/completed/process/TODO-uninotas-canonical-foundation-transition.md"
DELIVERY_BASELINE="0fe906c1e496a1d38f1603cf188c224711011c32"
FAILURE_PREDICATES={"parent_mismatch","ancestry_failure","head_origin_mismatch","actual_remote_mismatch","semantic_scan_mismatch"}
FAILURE_RE=re.compile(r"^Failure-Tuple: failure_id=([A-Za-z0-9._-]{1,64}); failed_c1_oid=([0-9a-f]{40}); predicate=(parent_mismatch|ancestry_failure|head_origin_mismatch|actual_remote_mismatch|semantic_scan_mismatch); observed=([A-Za-z0-9._:-]{1,160}); recorded_at_utc=(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)$",re.M)
C0_GO=("foundation-validator-c0","semantic-suite-c0","foundation-suite-c0","change-set-suite-c0","closeout-handoff-suite-c0","paced-readiness-c0","diff-expectation-c0","profile-scope-c0","todo-authority-c0","todo-completion-c0")
C0_REVIEW=("privacy-review-c0","architecture-adherence-c0","security-review-c0","test-quality-c0","final-review-c0","verification-debt-c0","triple-performance-c0","triple-test-quality-c0","triple-cutover-integrity-c0","performance-concurrency-c0")
C0_POST=("foundation-validator-c0-post","active-path-closeout-c0-post","active-set-scan-c0-post")
C1_PHASE=("closeout-proof-bridge-c1","todo-structure-c1","foundation-validator-c1","diff-expectation-c1","delivery-path-set-c1","lifecycle-path-set-c1","status-delivery-c1","status-lifecycle-c1","profile-scope-c1","diff-check-c1","todo-authority-c1","todo-completion-c1","todo-closeout-c1","closeout-integrity-review-c1")
C1R_PHASE=("recovery-proof-bridge-c1r","todo-structure-c1r","foundation-validator-c1r","diff-expectation-c1r","delivery-path-set-c1r","lifecycle-path-set-c1r","status-delivery-c1r","status-lifecycle-c1r","profile-scope-c1r","diff-check-c1r","todo-authority-c1r","todo-completion-c1r","todo-closeout-c1r","recovery-integrity-review-c1r")
INTENT_KEYS={"schema","state","phase","expected_remote","new_commit","candidate_tree","delivery_baseline","delivery_scope_set","phase_commit_delta_set","consumer_bindings","live_gate_evidence","delphi_root","proof_inputs","base_evidence","c0_post_evidence","proof_bridge","failure_tuple"}
C0_POST_KEYS={"schema","phase","commit","tree","remote","clean","foundation_validator","active_path_state","active_todo_count","active_paths","consumer_bindings"}
FAILURE_KEYS={"failure_id","failed_c1_oid","predicate","observed","recorded_at_utc"}
LIVE_GATE_KEYS={"consumer_id","candidate_tree_oid","command","exit_code","outcome","stdout_sha256","stderr_sha256"}
LIVE_GATE_IDS=("diff-expectation-c0","todo-authority-c0","todo-completion-c0")
PROOF_INPUT_KEYS={"implementation_reviews","focused_review"}
IMPLEMENTATION_REVIEW_KEYS={"consumer_id","phase","candidate_tree_oid","exact_path_set","reviewer_or_session","outcome","scope"}
FOCUSED_REVIEW_KEYS={"consumer_id","phase","candidate_tree_oid","exact_path_set","reviewer_or_session","outcome"}
REVIEWER_SESSION_RE=re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:@/-]{0,127}$")
TRANSITION_TODO="todos/active/process/TODO-uninotas-canonical-foundation-transition.md"
DISCOVERY_TODO="todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md"
def atomic_json(path, value):
    target=pathlib.Path(path); target.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile("w",dir=target.parent,delete=False,encoding="utf-8") as handle:
        json.dump(value,handle,sort_keys=True); handle.write("\n"); handle.flush(); os.fsync(handle.fileno()); temporary=handle.name
    pathlib.Path(temporary).replace(target)
    descriptor=os.open(target.parent,os.O_RDONLY); os.fsync(descriptor); os.close(descriptor)
def remote(repo):
    result=subprocess.run(["git","-C",repo,"ls-remote","--exit-code","origin","refs/heads/main"],text=True,capture_output=True)
    return result.stdout.split()[0] if result.returncode==0 and result.stdout.split() else None
def promotion_record(repo, expected, commit, lease_result="success", observation="fresh_pre_push"):
    """The one phase-evidence CAS shape consumed by verify and activate."""
    return {"fresh_pre_push_oid":expected,"expected_lease_oid":expected,"lease_result":lease_result,"promotion_observation":observation,"parent_and_fast_forward":True,"post_push_remote_main_oid":remote(repo),"local_head_oid":oid(repo,"HEAD"),"local_tracking_oid":oid(repo,"refs/remotes/origin/main")}
def strict_object(pairs):
    result={}
    for key,value in pairs:
        if key in result: raise ValueError("duplicate JSON member")
        result[key]=value
    return result
def load_json(value):
    try: return json.loads(pathlib.Path(value).read_text(),object_pairs_hook=strict_object,parse_constant=lambda _: (_ for _ in ()).throw(ValueError("non-finite JSON number")))
    except (OSError,json.JSONDecodeError,ValueError): raise ValueError("invalid JSON input")
def normalized_artifact_path(repo, value):
    if not isinstance(value,(str,os.PathLike)): return None
    root=pathlib.Path(repo).resolve(); raw=pathlib.Path(value)
    candidates=[raw.resolve()] if raw.is_absolute() else [(pathlib.Path.cwd()/raw).resolve(),(root/raw).resolve()]
    for candidate in dict.fromkeys(candidates):
        try:
            if candidate.is_relative_to(root/"artifacts/tmp"): return str(candidate)
        except ValueError: pass
    return str(candidates[0])
def tmp_path(repo, value):
    normalized=normalized_artifact_path(repo,value)
    if normalized is None: return False
    try: return pathlib.Path(normalized).is_relative_to((pathlib.Path(repo)/"artifacts/tmp").resolve())
    except ValueError: return False
def ignored_tmp_path(repo, value):
    normalized=normalized_artifact_path(repo,value)
    if normalized is None or not tmp_path(repo,normalized): return False
    relative=str(pathlib.Path(normalized).relative_to(pathlib.Path(repo).resolve()))
    return subprocess.run(["git","-C",repo,"check-ignore","-q","--",relative],capture_output=True).returncode == 0
def local_temporary_remote(remote_url):
    try:
        remote_path=pathlib.Path(remote_url).resolve(strict=True); temporary_root=pathlib.Path(tempfile.gettempdir()).resolve(strict=True)
        return remote_path.is_dir() and remote_path.is_relative_to(temporary_root)
    except (OSError,ValueError):
        return False
def canonical_delphi_root():
    return (pathlib.Path(__file__).resolve().parents[2]/"delphi-ai").resolve()
def resolve_delphi_root(repo, requested=None):
    canonical=canonical_delphi_root(); chosen=pathlib.Path(requested).resolve() if requested else canonical
    if chosen==canonical: return canonical
    remote_url=subprocess.run(["git","-C",repo,"remote","get-url","origin"],text=True,capture_output=True).stdout.strip()
    try: under_tmp=chosen.is_relative_to(pathlib.Path(tempfile.gettempdir()).resolve())
    except ValueError: under_tmp=False
    if local_temporary_remote(remote_url) and under_tmp: return chosen
    raise ValueError("Delphi root does not match the canonical sibling checkout")
def run_post_push_test_hook(repo, remote_url):
    hook=os.environ.get("UNINOTAS_TEST_POST_PUSH_HOOK")
    if not hook: return True
    return subprocess.run([hook,str(repo),remote_url],text=True,capture_output=True).returncode==0
def check_bindings(value, phase):
    keys={"consumer_id","phase","class","scope","binding_subject","change_scope_source","outcome"}
    if not isinstance(value,list) or any(not isinstance(row,dict) or set(row)!=keys or any(not isinstance(item,str) or not item for item in row.values()) for row in value): raise ValueError("consumer binding schema is invalid")
    if phase == "c0":
        expected={identifier:("C0","worktree-proxy","implementation_content","C0_CANDIDATE_TREE","DELIVERY_SCOPE_SET","go") for identifier in C0_GO}
        expected.update({identifier:("C0","implementation-human-review","implementation_content","C0_CANDIDATE_TREE","DELIVERY_SCOPE_SET","no_material_findings") for identifier in C0_REVIEW})
        error="C0 consumer bindings must exactly match the canonical catalog"
    elif phase == "c1":
        expected={identifier:("C1","tree-native" if identifier in {"closeout-proof-bridge-c1","delivery-path-set-c1","lifecycle-path-set-c1"} else "closeout-human-review" if identifier=="closeout-integrity-review-c1" else "worktree-proxy","closeout_transform","C1_CANDIDATE_TREE","DELIVERY_SCOPE_SET" if identifier in {"diff-expectation-c1","delivery-path-set-c1","status-delivery-c1","profile-scope-c1","diff-check-c1"} else "PHASE_COMMIT_DELTA_SET","no_material_findings" if identifier=="closeout-integrity-review-c1" else "go") for identifier in C1_PHASE}
        error="C1 consumer bindings must exactly match the canonical catalog"
    elif phase == "c1r":
        expected={identifier:("C1R","tree-native" if identifier in {"recovery-proof-bridge-c1r","delivery-path-set-c1r","lifecycle-path-set-c1r"} else "closeout-human-review" if identifier=="recovery-integrity-review-c1r" else "worktree-proxy","recovery_transform","C1R_CANDIDATE_TREE","DELIVERY_SCOPE_SET" if identifier in {"diff-expectation-c1r","delivery-path-set-c1r","status-delivery-c1r","profile-scope-c1r","diff-check-c1r"} else "PHASE_COMMIT_DELTA_SET","no_material_findings" if identifier=="recovery-integrity-review-c1r" else "go") for identifier in C1R_PHASE}
        error="C1R consumer bindings must exactly match the canonical catalog"
    else: raise ValueError("unknown phase")
    actual={row["consumer_id"]:(row["phase"],row["class"],row["scope"],row["binding_subject"],row["change_scope_source"],row["outcome"]) for row in value}
    if len(actual)!=len(value) or actual != expected: raise ValueError(error)
def check_c0_post_bindings(value):
    expected={identifier:("C0_POST","worktree-proxy","published_bootstrap","C0_COMMIT_TREE_CLEAN","CLEAN_C0_TREE","go") for identifier in C0_POST}
    actual={row.get("consumer_id"):(row.get("phase"),row.get("class"),row.get("scope"),row.get("binding_subject"),row.get("change_scope_source"),row.get("outcome")) for row in value} if isinstance(value,list) else {}
    if len(actual)!=len(value or []) or actual != expected: raise ValueError("C0_POST consumer bindings must exactly match the canonical catalog")
def c0_live_gate_commands(repo, delphi_root):
    root=pathlib.Path(delphi_root).resolve(); todo=str((pathlib.Path(repo)/ACTIVE_TODO).resolve())
    return (
        ("diff-expectation-c0",[sys.executable,"-B",str(root/"tools/todo_diff_expectation_guard.py"),todo,"--repo-root",str(pathlib.Path(repo).resolve())]),
        ("todo-authority-c0",[sys.executable,"-B",str(root/"tools/todo_authority_guard.py"),todo,"--require-delivery-gates"]),
        ("todo-completion-c0",[sys.executable,"-B",str(root/"tools/todo_completion_guard.py"),todo,"--require-delivery"]),
    )
def validate_live_gate_evidence(value, tree, repo=None, delphi_root=None):
    if not isinstance(value,list) or len(value)!=len(LIVE_GATE_IDS): raise ValueError("C0 live gate evidence is invalid")
    actual={}
    for row in value:
        if not isinstance(row,dict) or set(row)!=LIVE_GATE_KEYS or row.get("consumer_id") in actual: raise ValueError("C0 live gate evidence is invalid")
        command=row.get("command")
        if row.get("candidate_tree_oid")!=tree or not isinstance(command,list) or not command or any(not isinstance(item,str) or not item for item in command) or row.get("exit_code")!=0 or row.get("outcome")!="go" or not all(re.fullmatch(r"[0-9a-f]{64}",row.get(key,"")) for key in ("stdout_sha256","stderr_sha256")): raise ValueError("C0 live gate evidence is invalid")
        actual[row["consumer_id"]]=row
    if set(actual)!=set(LIVE_GATE_IDS): raise ValueError("C0 live gate evidence is invalid")
    if repo is not None and delphi_root is not None:
        expected=dict(c0_live_gate_commands(repo,delphi_root))
        if any(actual[identifier]["command"]!=expected[identifier] for identifier in LIVE_GATE_IDS): raise ValueError("C0 live gate command identity is invalid")
def run_c0_live_gates(repo, delphi_root, tree):
    commands=c0_live_gate_commands(repo,delphi_root)
    evidence=[]
    for consumer_id,command in commands:
        result=subprocess.run(command,cwd=repo,text=True,capture_output=True)
        outcomes=re.findall(r"^Overall outcome:\s*(\S+)\s*$",result.stdout,re.M)
        if result.returncode!=0 or outcomes!=["go"]: raise ValueError(f"C0 live gate failed: {consumer_id}")
        if oid(repo,"HEAD","^{tree}")!=tree or subprocess.run(["git","-C",repo,"status","--porcelain"],text=True,capture_output=True).stdout.strip(): raise ValueError("candidate tree changed during C0 live gates")
        evidence.append({"consumer_id":consumer_id,"candidate_tree_oid":tree,"command":command,"exit_code":result.returncode,"outcome":"go","stdout_sha256":hashlib.sha256(result.stdout.encode()).hexdigest(),"stderr_sha256":hashlib.sha256(result.stderr.encode()).hexdigest()})
    validate_live_gate_evidence(evidence,tree,repo,delphi_root)
    return evidence
def validate_implementation_reviews(value, tree, paths=None):
    if not isinstance(value,list): raise ValueError("implementation review attestations are required")
    actual={}
    for row in value:
        row_paths=row.get("exact_path_set") if isinstance(row,dict) else None
        if (not isinstance(row,dict) or set(row)!=IMPLEMENTATION_REVIEW_KEYS or row.get("consumer_id") in actual
                or row.get("phase")!="C0" or row.get("candidate_tree_oid")!=tree
                or not isinstance(row_paths,list) or row_paths!=sorted(set(row_paths)) or not row_paths
                or any(not isinstance(path,str) or not path for path in row_paths)
                or not isinstance(row.get("reviewer_or_session"),str) or not REVIEWER_SESSION_RE.fullmatch(row["reviewer_or_session"])
                or row.get("outcome")!="no_material_findings" or row.get("scope")!="implementation_content"):
            raise ValueError("implementation review attestations are not bound to C0 tree and exact path set")
        actual[row["consumer_id"]]=row
    if set(actual)!=set(C0_REVIEW) or len({tuple(row["exact_path_set"]) for row in actual.values()})!=1: raise ValueError("implementation review attestations are not bound to C0 tree and exact path set")
    if paths is not None and any(row["exact_path_set"]!=paths for row in actual.values()): raise ValueError("implementation review attestations are not bound to C0 tree and exact path set")
def validate_proof_inputs(value, phase="c1", tree=None, paths=None):
    if phase=="c0":
        if not isinstance(value,dict) or set(value)!={"implementation_reviews"}: raise ValueError("proof input schema is invalid")
        validate_implementation_reviews(value["implementation_reviews"],tree,paths); return
    if not isinstance(value,dict) or set(value)!=PROOF_INPUT_KEYS: raise ValueError("proof input schema is invalid")
    if not isinstance(value.get("implementation_reviews"),list) or not isinstance(value.get("focused_review"),dict): raise ValueError("proof input schema is invalid")
def run_closeout_proof(repo, phase, base, tree, proof_inputs):
    if phase not in {"c1","c1r"}: raise ValueError("proof bridge phase is invalid")
    validate_proof_inputs(proof_inputs)
    tmp=pathlib.Path(repo)/"artifacts/tmp"; tmp.mkdir(parents=True,exist_ok=True)
    review_path=focused_path=None
    try:
        with tempfile.NamedTemporaryFile("w",dir=tmp,delete=False,encoding="utf-8") as handle:
            json.dump(proof_inputs["implementation_reviews"],handle,sort_keys=True); handle.write("\n"); review_path=handle.name
        with tempfile.NamedTemporaryFile("w",dir=tmp,delete=False,encoding="utf-8") as handle:
            json.dump(proof_inputs["focused_review"],handle,sort_keys=True); handle.write("\n"); focused_path=handle.name
        command=[sys.executable,"-B",str(pathlib.Path(__file__).with_name("validate_closeout_diff.py")),"--mode","closeout" if phase=="c1" else "recovery","--repo",str(pathlib.Path(repo).resolve()),"--base",base,"--candidate-tree",tree,"--todo",COMPLETED_TODO if phase=="c1" else ACTIVE_TODO,"--implementation-reviews",review_path,"--focused-review",focused_path]
        result=subprocess.run(command,cwd=repo,text=True,capture_output=True)
        if result.returncode: raise ValueError(f"{phase.upper()} closeout proof failed")
        try: bridge=json.loads(result.stdout,object_pairs_hook=strict_object,parse_constant=lambda _: (_ for _ in ()).throw(ValueError("non-finite JSON number")))
        except (json.JSONDecodeError,ValueError): raise ValueError(f"{phase.upper()} closeout proof output is invalid")
        validate_bridge_schema(bridge,phase)
        return bridge
    finally:
        for value in (review_path,focused_path):
            if value:
                try: pathlib.Path(value).unlink()
                except FileNotFoundError: pass
def oid(repo, value, suffix=""):
    result=subprocess.run(["git","-C",repo,"rev-parse","--verify",value+suffix],text=True,capture_output=True)
    return result.stdout.strip() if result.returncode==0 else None
def canonical_failure_tuple(repo, commit):
    result=subprocess.run(["git","-C",repo,"show",f"{commit}:{ACTIVE_TODO}"],text=True,capture_output=True)
    matches=list(FAILURE_RE.finditer(result.stdout)) if result.returncode==0 else []
    if len(matches)!=1: raise ValueError("canonical recovery failure tuple is missing")
    match=matches[0]
    return {"failure_id":match.group(1),"failed_c1_oid":match.group(2),"predicate":match.group(3),"observed":match.group(4),"recorded_at_utc":match.group(5)}
def validate_failure_tuple(repo, commit, value):
    canonical=canonical_failure_tuple(repo,commit)
    if value!=canonical: raise ValueError("recovery failure tuple does not match candidate")
    return canonical
def validate_failure_schema(value):
    if not isinstance(value,dict) or set(value)!=FAILURE_KEYS: raise ValueError("failure tuple schema is invalid")
    if not re.fullmatch(r"[A-Za-z0-9._-]{1,64}",value.get("failure_id","")) or not OID_RE.fullmatch(value.get("failed_c1_oid","")) or value.get("predicate") not in FAILURE_PREDICATES or not re.fullmatch(r"[A-Za-z0-9._:-]{1,160}",value.get("observed","")) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",value.get("recorded_at_utc","")): raise ValueError("failure tuple schema is invalid")
def validate_c0_post_schema(value):
    active=[TRANSITION_TODO,DISCOVERY_TODO]
    if not isinstance(value,dict) or set(value)!=C0_POST_KEYS or value.get("schema")!="uninotas-c0-post-v1" or value.get("phase")!="c0" or not all(OID_RE.fullmatch(value.get(key,"")) for key in ("commit","tree","remote")) or value.get("clean") is not True or value.get("foundation_validator")!="go" or value.get("active_path_state")!="active" or value.get("active_todo_count")!=2 or value.get("active_paths")!=active: raise ValueError("C0_POST evidence schema is invalid")
    check_c0_post_bindings(value.get("consumer_bindings"))
def validate_bridge_schema(value, phase):
    keys={"validator","phase","base_commit","base_tree","candidate_tree","exact_delta","outcome","implementation_reviews","focused_review"}|({"failure_tuple"} if phase=="c1r" else set())
    if not isinstance(value,dict) or set(value)!=keys or value.get("validator")!="validate_closeout_diff.py" or value.get("phase")!=phase or not all(OID_RE.fullmatch(value.get(key,"")) for key in ("base_commit","base_tree","candidate_tree")) or not isinstance(value.get("exact_delta"),list) or value["exact_delta"]!=sorted(set(value["exact_delta"])) or any(not isinstance(path,str) or not path for path in value["exact_delta"]) or value.get("outcome")!="go": raise ValueError("proof bridge schema is invalid")
    if not isinstance(value.get("implementation_reviews"),list) or any(not isinstance(row,dict) or set(row)!=IMPLEMENTATION_REVIEW_KEYS or not isinstance(row.get("consumer_id"),str) or row.get("phase")!="C0" or not OID_RE.fullmatch(row.get("candidate_tree_oid","")) or not isinstance(row.get("exact_path_set"),list) or row["exact_path_set"]!=sorted(set(row["exact_path_set"])) or not row["exact_path_set"] or any(not isinstance(path,str) or not path for path in row["exact_path_set"]) or not isinstance(row.get("reviewer_or_session"),str) or not REVIEWER_SESSION_RE.fullmatch(row["reviewer_or_session"]) or row.get("outcome")!="no_material_findings" or row.get("scope")!="implementation_content" for row in value["implementation_reviews"]): raise ValueError("proof bridge schema is invalid")
    focused=value.get("focused_review")
    paths=focused.get("exact_path_set") if isinstance(focused,dict) else None
    if not isinstance(focused,dict) or set(focused)!=FOCUSED_REVIEW_KEYS or not isinstance(focused.get("consumer_id"),str) or focused.get("phase")!=phase.upper() or not OID_RE.fullmatch(focused.get("candidate_tree_oid","")) or not isinstance(paths,list) or paths!=sorted(set(paths)) or any(not isinstance(path,str) or not path for path in paths) or not isinstance(focused.get("reviewer_or_session"),str) or not REVIEWER_SESSION_RE.fullmatch(focused["reviewer_or_session"]) or focused.get("outcome")!="no_material_findings": raise ValueError("proof bridge schema is invalid")
    if phase=="c1r": validate_failure_schema(value.get("failure_tuple"))
def parse_active_scan(stdout, repo):
    if not isinstance(stdout,str) or len(re.findall(r"^Overall outcome:\s*go\s*$",stdout,re.M))!=1: raise ValueError("active TODO scan is invalid")
    counts=re.findall(r"^\s{2}- todo_count:\s*(\d+)\s*$",stdout,re.M)
    if len(counts)!=1: raise ValueError("active TODO scan is invalid")
    records=[]; current=None
    for line in stdout.splitlines():
        todo=re.fullmatch(r"\s{2}- todo:\s*(.+?)\s*",line)
        if todo:
            if current is not None: records.append(current)
            current={"path":todo.group(1),"state":None}
            continue
        state=re.fullmatch(r"\s{4}path_state:\s*(\S+)\s*",line)
        if state and current is not None: current["state"]=state.group(1)
    if current is not None: records.append(current)
    root=pathlib.Path(repo).resolve(); paths=[]
    for record in records:
        raw=pathlib.Path(record["path"])
        resolved=raw.resolve() if raw.is_absolute() else (root/raw).resolve()
        try: relative=resolved.relative_to(root).as_posix()
        except ValueError: raise ValueError("active TODO scan is invalid")
        if record["state"]!="active": raise ValueError("active TODO scan is invalid")
        paths.append(relative)
    if int(counts[0])!=len(paths) or len(paths)!=len(set(paths)): raise ValueError("active TODO scan is invalid")
    return sorted(paths)
def changed_paths(repo, base, commit):
    result=subprocess.run(["git","-C",repo,"diff","--no-renames","--name-only",base,commit],text=True,capture_output=True)
    if result.returncode: raise ValueError("phase path set cannot be resolved")
    return sorted(line for line in result.stdout.splitlines() if line)
def c0_evidence_from(phase, base_evidence):
    return base_evidence if phase=="c1" else base_evidence.get("base_evidence") if phase=="c1r" and isinstance(base_evidence,dict) else None
def phase_sets(repo, phase, expected, commit, delivery_baseline, base_evidence):
    phase_delta=changed_paths(repo,expected,commit)
    if phase=="c0":
        remote_url=subprocess.run(["git","-C",repo,"remote","get-url","origin"],text=True,capture_output=True).stdout.strip()
        test_baseline=local_temporary_remote(remote_url)
        if (delivery_baseline!=DELIVERY_BASELINE and not test_baseline) or oid(repo,delivery_baseline)!=delivery_baseline: raise ValueError("C0 delivery baseline must equal the approved baseline")
        return changed_paths(repo,delivery_baseline,commit),phase_delta
    c0=c0_evidence_from(phase,base_evidence)
    if not isinstance(c0,dict) or not isinstance(c0.get("delivery_scope_set"),list) or not c0.get("delivery_baseline"): raise ValueError("phase base evidence is invalid")
    return changed_paths(repo,c0["delivery_baseline"],commit),phase_delta
def validate_phase_evidence_schema(value):
    if not isinstance(value,dict): raise ValueError("phase evidence schema is invalid")
    phase=value.get("phase"); provenance=value.get("provenance")
    keys=INTENT_KEYS|{"provenance","post_push_remote_main_oid","remote_promotion"}|({"lease_result"} if provenance in {"resumed_push","resumed_remote_already_at_new_commit"} else set())|({"reverse_bridge"} if phase=="c1r" else set())
    if set(value)!=keys or value.get("schema")!="uninotas-closeout-intent-v1" or value.get("state")!="prepared" or phase not in PHASES or provenance not in {"promoted","resumed_push","resumed_remote_already_at_new_commit"}: raise ValueError("phase evidence schema is invalid")
    if not all(OID_RE.fullmatch(value.get(key,"")) for key in ("expected_remote","new_commit","candidate_tree","delivery_baseline","post_push_remote_main_oid")) or value["post_push_remote_main_oid"]!=value["new_commit"]: raise ValueError("phase evidence schema is invalid")
    if not valid_promotion(value.get("remote_promotion"),value["expected_remote"],value["new_commit"]): raise ValueError("phase evidence schema is invalid")
    if provenance=="promoted" and value["remote_promotion"]["lease_result"]!="success": raise ValueError("phase evidence schema is invalid")
    if provenance!="promoted" and (value.get("lease_result")!="not_observed_after_interruption" or value["remote_promotion"]["lease_result"]!="not_observed_after_interruption"): raise ValueError("phase evidence schema is invalid")
    check_bindings(value.get("consumer_bindings"),phase)
    if phase=="c0":
        validate_live_gate_evidence(value.get("live_gate_evidence"),value["candidate_tree"])
        validate_proof_inputs(value.get("proof_inputs"),"c0",value["candidate_tree"],value.get("delivery_scope_set"))
        if not isinstance(value.get("delphi_root"),str) or not value["delphi_root"] or any(value.get(key) is not None for key in ("base_evidence","c0_post_evidence","proof_bridge","failure_tuple")): raise ValueError("phase evidence schema is invalid")
    else:
        if value.get("live_gate_evidence") is not None or value.get("delphi_root") is not None: raise ValueError("phase evidence schema is invalid")
        validate_proof_inputs(value.get("proof_inputs"))
        expected_base="c0" if phase=="c1" else "c1"
        validate_phase_evidence_schema(value.get("base_evidence"))
        if value["base_evidence"].get("phase")!=expected_base: raise ValueError("phase evidence schema is invalid")
        validate_c0_post_schema(value.get("c0_post_evidence")); validate_bridge_schema(value.get("proof_bridge"),phase)
        if phase=="c1" and value.get("failure_tuple") is not None: raise ValueError("phase evidence schema is invalid")
        if phase=="c1r":
            validate_failure_schema(value.get("failure_tuple"))
            if value.get("reverse_bridge")!=value.get("proof_bridge"): raise ValueError("phase evidence schema is invalid")
def validate_recorded_phase_sets(repo, evidence):
    validate_phase_evidence_schema(evidence)
    if evidence.get("base_evidence") is not None: validate_recorded_phase_sets(repo,evidence["base_evidence"])
    commit=evidence.get("new_commit"); baseline=evidence.get("delivery_baseline"); parent=oid(repo,commit,"^") if commit else None
    expected=evidence.get("expected_remote")
    if not commit or not baseline or not parent or oid(repo,commit)!=commit or oid(repo,baseline)!=baseline or oid(repo,commit,"^{tree}")!=evidence.get("candidate_tree") or parent!=expected or oid(repo,expected)!=expected or subprocess.run(["git","-C",repo,"merge-base","--is-ancestor",expected,commit],capture_output=True).returncode: raise ValueError("phase path-set evidence is invalid")
    expected_delivery,expected_delta=phase_sets(repo,evidence["phase"],expected,commit,baseline,evidence.get("base_evidence"))
    if evidence.get("delivery_scope_set")!=expected_delivery or evidence.get("phase_commit_delta_set")!=expected_delta: raise ValueError("phase path-set evidence is invalid")
    if evidence["phase"]=="c0":
        root=resolve_delphi_root(repo,evidence.get("delphi_root")); validate_live_gate_evidence(evidence.get("live_gate_evidence"),evidence["candidate_tree"],repo,root)
    else:
        c0=c0_evidence_from(evidence["phase"],evidence["base_evidence"]); c0post=evidence.get("c0_post_evidence")
        if not isinstance(c0,dict) or c0post.get("commit")!=c0.get("new_commit") or c0post.get("tree")!=c0.get("candidate_tree") or c0post.get("remote")!=c0.get("new_commit"): raise ValueError("C0_POST evidence is required")
        proof=run_closeout_proof(repo,evidence["phase"],evidence["expected_remote"],evidence["candidate_tree"],evidence["proof_inputs"])
        if proof!=evidence.get("proof_bridge"): raise ValueError("recorded proof bridge does not match canonical proof execution")
def phase_record(repo, evidence):
    commit=evidence["new_commit"]; tree=evidence["candidate_tree"]
    return {"commit_oid":commit,"candidate_tree_oid":tree,"commit_tree_oid":oid(repo,commit,"^{tree}"),"tree_equal":oid(repo,commit,"^{tree}")==tree,"parent_oid":oid(repo,commit,"^"),"delivery_scope_set":evidence["delivery_scope_set"],"phase_commit_delta_set":evidence["phase_commit_delta_set"]}
def external_bridge(bridge):
    result={"validator":bridge["validator"],"base_commit_oid":bridge["base_commit"],"base_tree_oid":bridge["base_tree"],"candidate_tree_oid":bridge["candidate_tree"],"exact_delta_set":bridge["exact_delta"],"outcome":bridge["outcome"]}
    if "failure_tuple" in bridge: result["failure_tuple"]=bridge["failure_tuple"]
    return result
def external_c0_post(value):
    return {"head_oid":value["commit"],"commit_tree_oid":value["tree"],"remote_main_oid":value["remote"],"checkout_clean":value["clean"],"foundation_validator":value["foundation_validator"],"active_path_state":value["active_path_state"],"active_todo_count":value["active_todo_count"],"active_paths":value["active_paths"]}
def valid_phase_record(value):
    keys={"commit_oid","candidate_tree_oid","commit_tree_oid","tree_equal","parent_oid","delivery_scope_set","phase_commit_delta_set"}
    paths=lambda rows: isinstance(rows,list) and rows==sorted(set(rows)) and all(isinstance(row,str) and row for row in rows)
    return isinstance(value,dict) and set(value)==keys and value.get("tree_equal") is True and value.get("candidate_tree_oid")==value.get("commit_tree_oid") and all(OID_RE.fullmatch(value.get(key,"")) for key in ("commit_oid","candidate_tree_oid","commit_tree_oid","parent_oid")) and paths(value.get("delivery_scope_set")) and paths(value.get("phase_commit_delta_set"))
def valid_promotion(value, expected, commit):
    keys={"fresh_pre_push_oid","expected_lease_oid","lease_result","promotion_observation","parent_and_fast_forward","post_push_remote_main_oid","local_head_oid","local_tracking_oid"}
    return isinstance(value,dict) and set(value)==keys and value.get("fresh_pre_push_oid")==expected and value.get("expected_lease_oid")==expected and value.get("lease_result") in {"success","not_observed_after_interruption"} and value.get("promotion_observation") in {"fresh_pre_push","resumed_push","resumed_remote_already_at_new_commit"} and value.get("parent_and_fast_forward") is True and value.get("post_push_remote_main_oid")==commit and value.get("local_head_oid")==commit and value.get("local_tracking_oid")==commit
def validate_intent(repo, phase, expected, commit, tree, bindings, base_evidence, c0post, bridge, delivery_baseline=None, delivery_scope=None, phase_delta=None, failure_tuple=None):
    if phase not in PHASES: raise ValueError("unknown phase")
    check_bindings(bindings, phase)
    if oid(repo,commit)!=commit or oid(repo,commit,"^{tree}")!=tree: raise ValueError("commit tree does not match validated candidate tree")
    if subprocess.run(["git","-C",repo,"merge-base","--is-ancestor",expected,commit]).returncode: raise ValueError("new commit is not a fast-forward descendant of expected remote")
    parent=oid(repo,commit,"^" )
    if parent!=expected: raise ValueError("new commit parent does not equal expected remote")
    status=subprocess.run(["git","-C",repo,"status","--porcelain"],text=True,capture_output=True).stdout.strip()
    if oid(repo,"HEAD")!=commit: raise ValueError("working tree differs from validated candidate index")
    cached=subprocess.run(["git","-C",repo,"diff","--cached","--name-only"],text=True,capture_output=True).stdout.splitlines()
    if cached:
        allowed=subprocess.run(["git","-C",repo,"diff","--no-renames","--name-only",parent,commit],text=True,capture_output=True).stdout.splitlines()
        if set(cached)-set(allowed): raise ValueError("staged candidate contains path outside phase allowlist")
        raise ValueError("candidate tree changed after final validation")
    if status: raise ValueError("working tree differs from validated candidate index")
    if delivery_scope is not None and phase_delta is not None:
        expected_delivery,expected_delta=phase_sets(repo,phase,expected,commit,delivery_baseline,base_evidence)
        if delivery_scope!=expected_delivery or phase_delta!=expected_delta or delivery_scope!=sorted(set(delivery_scope)) or phase_delta!=sorted(set(phase_delta)): raise ValueError("phase path-set evidence is invalid")
    if phase in {"c1","c1r"}:
        validate_phase_evidence_schema(base_evidence)
        validate_c0_post_schema(c0post)
        validate_bridge_schema(bridge,phase)
        expected_base_phase="c0" if phase=="c1" else "c1"
        if not isinstance(base_evidence,dict) or base_evidence.get("phase")!=expected_base_phase or base_evidence.get("new_commit")!=expected or base_evidence.get("candidate_tree")!=oid(repo,expected,"^{tree}"): raise ValueError("phase base evidence is invalid")
        c0_evidence=base_evidence if phase=="c1" else base_evidence.get("base_evidence")
        if not isinstance(c0_evidence,dict) or c0_evidence.get("phase")!="c0": raise ValueError("phase base evidence is invalid")
        c0_commit,c0_tree=c0_evidence.get("new_commit"),c0_evidence.get("candidate_tree")
        if not isinstance(c0post,dict) or c0post.get("phase")!="c0" or c0post.get("commit")!=c0_commit or c0post.get("tree")!=c0_tree or c0post.get("remote")!=c0_commit or c0post.get("active_path_state")!="active" or c0post.get("active_todo_count")!=2: raise ValueError("C0_POST evidence is required")
        check_c0_post_bindings(c0post.get("consumer_bindings"))
        bridge_keys={"validator","phase","base_commit","base_tree","candidate_tree","exact_delta","outcome","implementation_reviews","focused_review"}|({"failure_tuple"} if phase=="c1r" else set())
        if not isinstance(bridge,dict) or set(bridge)!=bridge_keys or bridge.get("validator")!="validate_closeout_diff.py" or bridge.get("phase")!=phase or bridge.get("base_commit")!=expected or bridge.get("base_tree")!=oid(repo,expected,"^{tree}") or bridge.get("candidate_tree")!=tree or not isinstance(bridge.get("exact_delta"),list) or bridge.get("outcome")!="go": raise ValueError("proof bridge is required")
        if phase_delta is not None and bridge["exact_delta"]!=phase_delta: raise ValueError("proof bridge phase delta is invalid")
        carried={row.get("consumer_id"):row for row in bridge["implementation_reviews"]} if isinstance(bridge.get("implementation_reviews"),list) else {}
        if set(carried)!=set(C0_REVIEW) or any(row.get("candidate_tree_oid")!=c0_tree or row.get("exact_path_set")!=c0_evidence.get("delivery_scope_set") for row in carried.values()): raise ValueError("implementation review carry is not bound to C0 tree and delivery scope")
        if bridge.get("implementation_reviews")!=c0_evidence.get("proof_inputs",{}).get("implementation_reviews"): raise ValueError("implementation review carry does not match published C0 attestations")
        focused=bridge.get("focused_review")
        focused_id="closeout-integrity-review-c1" if phase=="c1" else "recovery-integrity-review-c1r"
        expected_focused={"consumer_id":focused_id,"phase":phase.upper(),"candidate_tree_oid":tree,"exact_path_set":bridge["exact_delta"],"reviewer_or_session":focused.get("reviewer_or_session") if isinstance(focused,dict) else None,"outcome":"no_material_findings"}
        if not isinstance(focused,dict) or set(focused)!=FOCUSED_REVIEW_KEYS or not isinstance(focused.get("reviewer_or_session"),str) or not REVIEWER_SESSION_RE.fullmatch(focused["reviewer_or_session"]) or focused!=expected_focused: raise ValueError(f"focused {phase.upper()} review is not bound to current candidate tree and path set")
        if phase=="c1r":
            validate_failure_schema(failure_tuple)
            canonical=validate_failure_tuple(repo,commit,failure_tuple)
            if bridge.get("failure_tuple")!=canonical: raise ValueError("recovery proof bridge failure tuple is invalid")
def validate_production_handoff(value):
    required={"schema","handoff_kind","c0","c1","proof_bridge","consumer_bindings","remote_promotions","c0_post_verify","post_c1_active_scan","actual_remote_main_oid","production_ready_effective","recovery_effective"}
    if not isinstance(value,dict) or set(value)!=required or value.get("schema")!="uninotas-closeout-handoff-v1" or value.get("handoff_kind")!="production": return "production handoff schema is invalid"
    c0,c1=value["c0"],value["c1"]
    if not valid_phase_record(c0) or not valid_phase_record(c1): return "commit tree unequal to recorded candidate tree blocks Production-Ready"
    if c1["parent_oid"]!=c0["commit_oid"]: return "production phase relationship is invalid"
    bridge=value["proof_bridge"]
    bridge_keys={"validator","base_commit_oid","base_tree_oid","candidate_tree_oid","exact_delta_set","outcome"}
    if not isinstance(bridge,dict) or set(bridge)!=bridge_keys or bridge!={"validator":"validate_closeout_diff.py","base_commit_oid":c0["commit_oid"],"base_tree_oid":c0["commit_tree_oid"],"candidate_tree_oid":c1["candidate_tree_oid"],"exact_delta_set":c1["phase_commit_delta_set"],"outcome":"go"}: return "production proof bridge is invalid"
    rows=value["consumer_bindings"]
    try:
        check_bindings([row for row in rows if isinstance(row,dict) and row.get("phase")=="C0"],"c0")
        check_c0_post_bindings([row for row in rows if isinstance(row,dict) and row.get("phase")=="C0_POST"])
        check_bindings([row for row in rows if isinstance(row,dict) and row.get("phase")=="C1"],"c1")
    except (TypeError,ValueError): return "production consumer partition must exactly contain C0+C0_POST+C1"
    expected=set(C0_GO)|set(C0_REVIEW)|set(C0_POST)|set(C1_PHASE)
    ids=[row.get("consumer_id") for row in rows] if isinstance(rows,list) else []
    if len(ids)!=len(set(ids)) or set(ids)!=expected or len(ids)!=len(expected): return "production consumer partition must exactly contain C0+C0_POST+C1"
    promotions=value["remote_promotions"]
    if not isinstance(promotions,dict) or set(promotions)!={"c0","c1"} or not valid_promotion(promotions["c0"],c0["parent_oid"],c0["commit_oid"]) or not valid_promotion(promotions["c1"],c0["commit_oid"],c1["commit_oid"]): return "production handoff requires complete C0 and C1 CAS evidence"
    post=value["c0_post_verify"]
    post_keys={"head_oid","commit_tree_oid","remote_main_oid","checkout_clean","foundation_validator","active_path_state","active_todo_count","active_paths"}
    active=["todos/active/process/TODO-uninotas-canonical-foundation-transition.md","todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md"]
    if not isinstance(post,dict) or set(post)!=post_keys or post!={"head_oid":c0["commit_oid"],"commit_tree_oid":c0["commit_tree_oid"],"remote_main_oid":c0["commit_oid"],"checkout_clean":True,"foundation_validator":"go","active_path_state":"active","active_todo_count":2,"active_paths":active}: return "production C0 post verification is invalid"
    scan=value["post_c1_active_scan"]
    expected_scan={"scanned_head_oid":c1["commit_oid"],"outcome":"go","todo_count":1,"active_paths":["todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md"],"stale_transition_path":False}
    if scan!=expected_scan or value["actual_remote_main_oid"]!=c1["commit_oid"] or value["production_ready_effective"] is not True or value["recovery_effective"] is not False: return "production activation observation is invalid"
    return None
def validate_recovery_handoff(value):
    required={"schema","handoff_kind","c0","c1","c1r","consumer_bindings","reverse_bridge","failure_tuple","remote_promotions","c0_post_verify","post_c1r_active_scan","actual_remote_main_oid","recovery_effective","production_ready_effective"}
    if not isinstance(value,dict) or set(value)!=required or value.get("schema")!="uninotas-closeout-handoff-v1" or value.get("handoff_kind")!="recovery": return "recovery handoff schema is invalid"
    c0,c1,c1r=value["c0"],value["c1"],value["c1r"]
    if not all(valid_phase_record(row) for row in (c0,c1,c1r)): return "C1R commit tree must equal candidate tree"
    if c1["parent_oid"]!=c0["commit_oid"] or c1r["parent_oid"]!=c1["commit_oid"]: return "recovery phase relationship is invalid"
    rows=value["consumer_bindings"]
    if not isinstance(rows,list): return "recovery consumer partition must exactly contain C0+C0_POST+C1+C1R"
    try:
        check_bindings([row for row in rows if isinstance(row,dict) and row.get("phase")=="C0"],"c0")
        check_c0_post_bindings([row for row in rows if isinstance(row,dict) and row.get("phase")=="C0_POST"])
        check_bindings([row for row in rows if isinstance(row,dict) and row.get("phase")=="C1"],"c1")
        check_bindings([row for row in rows if isinstance(row,dict) and row.get("phase")=="C1R"],"c1r")
    except ValueError:
        return "recovery consumer partition must exactly contain C0+C0_POST+C1+C1R"
    if sum(1 for row in rows if isinstance(row,dict) and row.get("phase") in {"C0","C0_POST","C1","C1R"}) != len(rows): return "recovery consumer partition must exactly contain C0+C0_POST+C1+C1R"
    reverse=value["reverse_bridge"]
    failure=value["failure_tuple"]
    failure_keys={"failure_id","failed_c1_oid","predicate","observed","recorded_at_utc"}
    if not isinstance(failure,dict) or set(failure)!=failure_keys or failure.get("failed_c1_oid")!=c1.get("commit_oid") or failure.get("predicate") not in FAILURE_PREDICATES or not re.fullmatch(r"[A-Za-z0-9._-]{1,64}",failure.get("failure_id","")) or not re.fullmatch(r"[A-Za-z0-9._:-]{1,160}",failure.get("observed","")) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",failure.get("recorded_at_utc","")): return "recovery failure tuple is invalid"
    reverse_keys={"validator","base_commit_oid","base_tree_oid","candidate_tree_oid","exact_delta_set","outcome","failure_tuple"}
    expected_reverse={"validator":"validate_closeout_diff.py","base_commit_oid":c1["commit_oid"],"base_tree_oid":c1["commit_tree_oid"],"candidate_tree_oid":c1r["candidate_tree_oid"],"exact_delta_set":c1r["phase_commit_delta_set"],"outcome":"go","failure_tuple":failure}
    if not isinstance(reverse,dict) or set(reverse)!=reverse_keys or reverse!=expected_reverse: return "recovery reverse bridge is invalid"
    promotions=value["remote_promotions"]
    if not isinstance(promotions,dict) or set(promotions)!={"c0","c1","c1r"} or not valid_promotion(promotions["c0"],c0["parent_oid"],c0["commit_oid"]) or not valid_promotion(promotions["c1"],c0["commit_oid"],c1["commit_oid"]) or not valid_promotion(promotions["c1r"],c1["commit_oid"],c1r["commit_oid"]): return "recovery remote promotion is invalid"
    post=value["c0_post_verify"]
    active=["todos/active/process/TODO-uninotas-canonical-foundation-transition.md","todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md"]
    expected_post={"head_oid":c0["commit_oid"],"commit_tree_oid":c0["commit_tree_oid"],"remote_main_oid":c0["commit_oid"],"checkout_clean":True,"foundation_validator":"go","active_path_state":"active","active_todo_count":2,"active_paths":active}
    if post!=expected_post: return "recovery C0 post verification is invalid"
    scan=value["post_c1r_active_scan"]
    expected_scan={"scanned_head_oid":c1r["commit_oid"],"outcome":"go","todo_count":2,"active_paths":active,"stale_completed_path":False}
    if scan!=expected_scan: return "recovery requires exact two-active scan"
    if value["actual_remote_main_oid"]!=c1r["commit_oid"] or value["recovery_effective"] is not True or value["production_ready_effective"] is not False: return "recovery effectiveness state is invalid"
    return None
def promote(args):
    inputs=[args.consumer_bindings]+[value for value in (args.base_evidence,args.c0_post_evidence,args.implementation_reviews,args.focused_review,args.failure_tuple) if value]
    if not all(ignored_tmp_path(args.repo,value) for value in inputs+[args.journal,args.output]): return fail("promotion evidence, journal, and output must be ignored under artifacts/tmp")
    try:
        bindings=load_json(args.consumer_bindings); base=load_json(args.base_evidence) if args.base_evidence else None; c0post=load_json(args.c0_post_evidence) if args.c0_post_evidence else None; failure=load_json(args.failure_tuple) if args.failure_tuple else None
        check_bindings(bindings,args.phase)
        if remote(args.repo)!=args.expected_remote:
            if args.phase=="c1r": raise ValueError("C1R blocked: reconciliation, rebaseline, and renewed approval required")
            raise ValueError("local-unpublished-diverged: expected-value lease precondition failed")
        if args.phase=="c1r": validate_failure_schema(failure); validate_failure_tuple(args.repo,args.new_commit,failure)
        delivery_baseline=args.delivery_baseline if args.phase=="c0" else c0_evidence_from(args.phase,base).get("delivery_baseline") if isinstance(c0_evidence_from(args.phase,base),dict) else None
        delivery_scope,phase_delta=phase_sets(args.repo,args.phase,args.expected_remote,args.new_commit,delivery_baseline,base)
        delphi_root=str(resolve_delphi_root(args.repo,args.delphi_root)) if args.phase=="c0" else None
        if args.phase=="c0":
            proof_inputs={"implementation_reviews":load_json(args.implementation_reviews)} if args.implementation_reviews else None
            validate_proof_inputs(proof_inputs,"c0",args.candidate_tree,delivery_scope)
        else:
            proof_inputs={"implementation_reviews":load_json(args.implementation_reviews),"focused_review":load_json(args.focused_review)} if args.implementation_reviews and args.focused_review else None
        bridge=run_closeout_proof(args.repo,args.phase,args.expected_remote,args.candidate_tree,proof_inputs) if args.phase in {"c1","c1r"} else None
        if args.phase in {"c1","c1r"}:
            validate_recorded_phase_sets(args.repo,base)
            validate_c0_post_schema(c0post)
        validate_intent(args.repo,args.phase,args.expected_remote,args.new_commit,args.candidate_tree,bindings,base,c0post,bridge,delivery_baseline,delivery_scope,phase_delta,failure)
        live_gates=run_c0_live_gates(args.repo,delphi_root,args.candidate_tree) if args.phase=="c0" else None
    except ValueError as error: return fail(str(error))
    failpoint_requested=os.environ.get("UNINOTAS_TEST_AFTER_PUSH_FAILPOINT")=="1"; hook_requested=bool(os.environ.get("UNINOTAS_TEST_POST_PUSH_HOOK"))
    remote_url=subprocess.run(["git","-C",args.repo,"remote","get-url","origin"],text=True,capture_output=True).stdout.strip()
    if (failpoint_requested or hook_requested) and (os.environ.get("UNINOTAS_HANDOFF_TEST_MODE")!="1" or not local_temporary_remote(remote_url)): return fail("test controls require UNINOTAS_HANDOFF_TEST_MODE=1 and local temporary remote")
    intent={"schema":"uninotas-closeout-intent-v1","state":"prepared","phase":args.phase,"expected_remote":args.expected_remote,"new_commit":args.new_commit,"candidate_tree":args.candidate_tree,"delivery_baseline":delivery_baseline,"delivery_scope_set":delivery_scope,"phase_commit_delta_set":phase_delta,"consumer_bindings":bindings,"live_gate_evidence":live_gates,"delphi_root":delphi_root,"proof_inputs":proof_inputs,"base_evidence":base,"c0_post_evidence":c0post,"proof_bridge":bridge,"failure_tuple":failure}
    atomic_json(args.journal,intent)
    push=subprocess.run(["git","-C",args.repo,"push",f"--force-with-lease=refs/heads/main:{args.expected_remote}","origin",f"{args.new_commit}:refs/heads/main"],text=True,capture_output=True)
    if push.returncode: return fail("CAS push rejected")
    if hook_requested and not run_post_push_test_hook(args.repo,remote_url): return fail("test post-push hook failed")
    if failpoint_requested: return fail("test failpoint after push")
    record=promotion_record(args.repo,args.expected_remote,args.new_commit)
    if not valid_promotion(record,args.expected_remote,args.new_commit): return fail("post-push remote verification failed")
    evidence={**intent,"provenance":"promoted","post_push_remote_main_oid":record["post_push_remote_main_oid"],"remote_promotion":record}
    if args.phase=="c1r": evidence["reverse_bridge"]=bridge
    atomic_json(args.output,evidence); print(json.dumps(evidence,sort_keys=True)); return 0
def resume(args):
    if not ignored_tmp_path(args.repo,args.journal) or not ignored_tmp_path(args.repo,args.output): return fail("journals and outputs must be ignored under artifacts/tmp")
    try:
        intent=load_json(args.journal)
        if set(intent)!=INTENT_KEYS or intent.get("schema")!="uninotas-closeout-intent-v1": raise ValueError
        if intent.get("phase")=="c0":
            root=resolve_delphi_root(args.repo,intent.get("delphi_root")); validate_proof_inputs(intent.get("proof_inputs"),"c0",intent.get("candidate_tree"),intent.get("delivery_scope_set")); intent["live_gate_evidence"]=run_c0_live_gates(args.repo,root,intent.get("candidate_tree"))
        else:
            if intent.get("live_gate_evidence") is not None: raise ValueError
            validate_recorded_phase_sets(args.repo,intent.get("base_evidence")); validate_c0_post_schema(intent.get("c0_post_evidence"))
            proof=run_closeout_proof(args.repo,intent["phase"],intent["expected_remote"],intent["candidate_tree"],intent.get("proof_inputs"))
            if proof!=intent.get("proof_bridge"): raise ValueError
        validate_intent(args.repo,intent["phase"],intent["expected_remote"],intent["new_commit"],intent["candidate_tree"],intent["consumer_bindings"],intent.get("base_evidence"),intent.get("c0_post_evidence"),intent.get("proof_bridge"),intent.get("delivery_baseline"),intent.get("delivery_scope_set"),intent.get("phase_commit_delta_set"),intent.get("failure_tuple"))
    except (ValueError,KeyError): return fail("resume intent is invalid")
    if args.phase!=intent["phase"] or intent.get("state")!="prepared": return fail("resume intent is invalid")
    atomic_json(args.journal,intent)
    hook_requested=bool(os.environ.get("UNINOTAS_TEST_POST_PUSH_HOOK")); remote_url=subprocess.run(["git","-C",args.repo,"remote","get-url","origin"],text=True,capture_output=True).stdout.strip()
    if hook_requested and (os.environ.get("UNINOTAS_HANDOFF_TEST_MODE")!="1" or not local_temporary_remote(remote_url)): return fail("test controls require UNINOTAS_HANDOFF_TEST_MODE=1 and local temporary remote")
    observed=remote(args.repo)
    if observed not in {intent["expected_remote"],intent["new_commit"]}: return fail("remote third OID prevents resume")
    if observed==intent["expected_remote"]:
        push=subprocess.run(["git","-C",args.repo,"push",f"--force-with-lease=refs/heads/main:{observed}","origin",f"{intent['new_commit']}:refs/heads/main"],text=True,capture_output=True)
        if push.returncode: return fail("CAS push rejected")
        if hook_requested and not run_post_push_test_hook(args.repo,remote_url): return fail("test post-push hook failed")
        observed=remote(args.repo); provenance="resumed_push"
    else: provenance="resumed_remote_already_at_new_commit"
    record=promotion_record(args.repo,intent["expected_remote"],intent["new_commit"],"not_observed_after_interruption",provenance)
    if observed!=intent["new_commit"] or not valid_promotion(record,intent["expected_remote"],intent["new_commit"]): return fail("post-push remote verification failed")
    evidence={**intent,"provenance":provenance,"lease_result":"not_observed_after_interruption","post_push_remote_main_oid":observed,"remote_promotion":record}
    if intent["phase"]=="c1r": evidence["reverse_bridge"]=intent["proof_bridge"]
    atomic_json(args.output,evidence); print(json.dumps(evidence,sort_keys=True)); return 0
def verify(args):
    if args.phase != "c0": return fail("verify supports only C0")
    if not ignored_tmp_path(args.repo,args.phase_evidence) or not ignored_tmp_path(args.repo,args.output): return fail("verify evidence and output must be ignored under artifacts/tmp")
    try: evidence=load_json(args.phase_evidence); validate_recorded_phase_sets(args.repo,evidence)
    except ValueError: return fail("phase evidence is not a published exact commit")
    record=evidence.get("remote_promotion")
    if evidence.get("phase") != "c0" or evidence.get("post_push_remote_main_oid") != evidence.get("new_commit") or not evidence.get("candidate_tree") or not isinstance(record,dict) or record.get("post_push_remote_main_oid") != evidence.get("new_commit"): return fail("phase evidence is not a published exact commit")
    def clean():
        head=oid(args.repo,"HEAD"); tree=oid(args.repo,"HEAD","^{tree}"); dirty=subprocess.run(["git","-C",args.repo,"status","--porcelain"],text=True,capture_output=True).stdout.strip()
        return head,tree,dirty,remote(args.repo)
    head,tree,dirty,observed=clean()
    if head != evidence["new_commit"] or tree != evidence["candidate_tree"] or dirty or observed != head: return fail("clean published phase binding failed")
    validator=subprocess.run([sys.executable,"-B",str(pathlib.Path(args.repo)/"deterministic/validate_foundation.py"),"--root",args.repo],text=True,capture_output=True)
    transition=TRANSITION_TODO; discovery=DISCOVERY_TODO
    guard=pathlib.Path(args.delphi_root)/"tools/todo_closeout_guard.py"
    one=subprocess.run([sys.executable,"-B",str(guard),transition],cwd=args.repo,text=True,capture_output=True)
    scan=subprocess.run([sys.executable,"-B",str(guard),"--all-active","--repo","."],cwd=args.repo,text=True,capture_output=True)
    try:
        one_paths=parse_active_scan(one.stdout,args.repo); active_paths=parse_active_scan(scan.stdout,args.repo)
    except ValueError: one_paths=active_paths=[]
    if validator.returncode or one.returncode or scan.returncode or one_paths!=[transition] or active_paths!=sorted([transition,discovery]): return fail(f"C0 semantic validator or active TODO scan failed (validator={validator.returncode}, path={one.returncode}, scan={scan.returncode}): {validator.stdout[-300:]}")
    head2,tree2,dirty2,observed2=clean()
    if (head2,tree2,observed2)!=(head,tree,observed) or dirty2: return fail("clean published phase binding failed")
    bindings=[{"consumer_id":"foundation-validator-c0-post","phase":"C0_POST","class":"worktree-proxy","scope":"published_bootstrap","binding_subject":"C0_COMMIT_TREE_CLEAN","change_scope_source":"CLEAN_C0_TREE","outcome":"go"},{"consumer_id":"active-path-closeout-c0-post","phase":"C0_POST","class":"worktree-proxy","scope":"published_bootstrap","binding_subject":"C0_COMMIT_TREE_CLEAN","change_scope_source":"CLEAN_C0_TREE","outcome":"go"},{"consumer_id":"active-set-scan-c0-post","phase":"C0_POST","class":"worktree-proxy","scope":"published_bootstrap","binding_subject":"C0_COMMIT_TREE_CLEAN","change_scope_source":"CLEAN_C0_TREE","outcome":"go"}]
    output={"schema":"uninotas-c0-post-v1","phase":"c0","commit":head,"tree":tree,"remote":observed,"clean":True,"foundation_validator":"go","active_path_state":"active","active_todo_count":len(active_paths),"active_paths":active_paths,"consumer_bindings":bindings}
    atomic_json(args.output,output); print(json.dumps(output,sort_keys=True)); return 0
def activate(args):
    if args.phase == "c1r": return activate_c1r(args)
    if args.phase != "c1": return fail("activate supports only C1")
    if not all(ignored_tmp_path(args.repo,value) for value in (args.c0_evidence,args.c0_post_evidence,args.c1_evidence,args.output)): return fail("activation evidence and output must be ignored under artifacts/tmp")
    try:
        c0=load_json(args.c0_evidence); c0post=load_json(args.c0_post_evidence); c1=load_json(args.c1_evidence)
        validate_recorded_phase_sets(args.repo,c0); validate_recorded_phase_sets(args.repo,c1)
        validate_c0_post_schema(c0post)
        if c0.get("phase")!="c0" or c1.get("phase")!="c1" or c0post.get("schema")!="uninotas-c0-post-v1": raise ValueError("incomplete or incompatible phase chain")
        check_bindings(c0.get("consumer_bindings"),"c0"); check_c0_post_bindings(c0post.get("consumer_bindings")); check_bindings(c1.get("consumer_bindings"),"c1")
        if c0post.get("commit")!=c0.get("new_commit") or c0post.get("tree")!=c0.get("candidate_tree") or c0post.get("active_todo_count")!=2 or c0post.get("active_path_state")!="active": raise ValueError("incomplete or incompatible phase chain")
        validate_intent(args.repo,"c1",c0["new_commit"],c1["new_commit"],c1["candidate_tree"],c1["consumer_bindings"],c1.get("base_evidence"),c1.get("c0_post_evidence"),c1.get("proof_bridge"),c1.get("delivery_baseline"),c1.get("delivery_scope_set"),c1.get("phase_commit_delta_set"))
        if c1.get("post_push_remote_main_oid")!=c1["new_commit"]: raise ValueError("incomplete or incompatible phase chain")
    except ValueError as error:
        if str(error) in {"working tree differs from validated candidate index","candidate tree changed after final validation","staged candidate contains path outside phase allowlist"}: return fail("activation remote or clean-tree binding failed")
        return fail("incomplete or incompatible phase chain")
    except (KeyError,TypeError): return fail("incomplete or incompatible phase chain")
    transition=TRANSITION_TODO; discovery=DISCOVERY_TODO
    def binding():
        head=oid(args.repo,"HEAD"); tracking=oid(args.repo,"refs/remotes/origin/main"); tree=oid(args.repo,"HEAD","^{tree}"); dirty=subprocess.run(["git","-C",args.repo,"status","--porcelain","--untracked-files=all"],text=True,capture_output=True).stdout.strip(); observed=remote(args.repo)
        return head,tracking,tree,dirty,observed
    head,tracking,tree,dirty,observed_before=binding()
    if dirty or head!=c1["new_commit"] or tracking!=head or observed_before!=head or tree!=c1["candidate_tree"]: return fail("activation remote or clean-tree binding failed")
    guard=subprocess.run([sys.executable,"-B",str(pathlib.Path(args.delphi_root)/"tools/todo_closeout_guard.py"),"--all-active","--repo","."],cwd=args.repo,text=True,capture_output=True)
    try: active_paths=parse_active_scan(guard.stdout,args.repo)
    except ValueError: active_paths=[]
    if guard.returncode or active_paths!=[discovery]: return fail("C1 active TODO scan failed")
    head2,tracking2,tree2,dirty2,observed_after=binding()
    if dirty2 or (head2,tracking2,tree2,observed_after)!=(head,tracking,tree,observed_before): return fail("activation remote or clean-tree binding failed")
    output={"schema":"uninotas-closeout-handoff-v1","handoff_kind":"production","c0":phase_record(args.repo,c0),"c1":phase_record(args.repo,c1),"proof_bridge":external_bridge(c1["proof_bridge"]),"consumer_bindings":c0["consumer_bindings"]+c0post["consumer_bindings"]+c1["consumer_bindings"],"remote_promotions":{"c0":c0["remote_promotion"],"c1":c1["remote_promotion"]},"c0_post_verify":external_c0_post(c0post),"post_c1_active_scan":{"scanned_head_oid":head,"outcome":"go","todo_count":len(active_paths),"active_paths":active_paths,"stale_transition_path":transition in active_paths},"actual_remote_main_oid":observed_after,"production_ready_effective":True,"recovery_effective":False}
    error=validate_production_handoff(output)
    if error: return fail(error)
    atomic_json(args.output,output); print(json.dumps(output,sort_keys=True)); return 0
def activate_c1r(args):
    if not all(ignored_tmp_path(args.repo,value) for value in (args.c0_evidence,args.c0_post_evidence,args.failed_c1_evidence,args.c1r_evidence,args.failure_tuple,args.output)): return fail("activation evidence and output must be ignored under artifacts/tmp")
    try:
        c0=load_json(args.c0_evidence); c0post=load_json(args.c0_post_evidence); failed=load_json(args.failed_c1_evidence); c1r=load_json(args.c1r_evidence); failure=load_json(args.failure_tuple)
        validate_recorded_phase_sets(args.repo,c0); validate_recorded_phase_sets(args.repo,failed); validate_recorded_phase_sets(args.repo,c1r)
        validate_c0_post_schema(c0post); validate_failure_schema(failure)
        if c0.get("phase")!="c0" or failed.get("phase")!="c1" or c1r.get("phase")!="c1r" or c0post.get("schema")!="uninotas-c0-post-v1": raise ValueError
        check_bindings(c0.get("consumer_bindings"),"c0"); check_c0_post_bindings(c0post.get("consumer_bindings")); check_bindings(failed.get("consumer_bindings"),"c1"); check_bindings(c1r.get("consumer_bindings"),"c1r")
        if c0post.get("commit")!=c0.get("new_commit") or c0post.get("tree")!=c0.get("candidate_tree") or c0post.get("active_todo_count")!=2: raise ValueError
        if c1r.get("failure_tuple")!=failure: raise ValueError("recovery failure tuple does not match promotion evidence")
        validate_intent(args.repo,"c1r",failed["new_commit"],c1r["new_commit"],c1r["candidate_tree"],c1r["consumer_bindings"],failed,c0post,c1r.get("reverse_bridge"),c1r.get("delivery_baseline"),c1r.get("delivery_scope_set"),c1r.get("phase_commit_delta_set"),failure)
    except ValueError as error:
        if str(error) in {"working tree differs from validated candidate index","candidate tree changed after final validation","staged candidate contains path outside phase allowlist"}: return fail("activation remote or clean-tree binding failed")
        return fail("incomplete or incompatible recovery chain")
    except (KeyError,TypeError): return fail("incomplete or incompatible recovery chain")
    transition=TRANSITION_TODO; discovery=DISCOVERY_TODO
    def binding():
        head=oid(args.repo,"HEAD"); tracking=oid(args.repo,"refs/remotes/origin/main"); tree=oid(args.repo,"HEAD","^{tree}"); dirty=subprocess.run(["git","-C",args.repo,"status","--porcelain","--untracked-files=all"],text=True,capture_output=True).stdout.strip(); observed=remote(args.repo)
        return head,tracking,tree,dirty,observed
    head,tracking,tree,dirty,observed_before=binding()
    if dirty or head!=c1r["new_commit"] or tracking!=head or observed_before!=head or tree!=c1r["candidate_tree"]: return fail("activation remote or clean-tree binding failed")
    guard=subprocess.run([sys.executable,"-B",str(pathlib.Path(args.delphi_root)/"tools/todo_closeout_guard.py"),"--all-active","--repo","."],cwd=args.repo,text=True,capture_output=True)
    try: active_paths=parse_active_scan(guard.stdout,args.repo)
    except ValueError: active_paths=[]
    if guard.returncode or active_paths!=sorted([transition,discovery]): return fail("C1R active TODO scan failed")
    head2,tracking2,tree2,dirty2,observed_after=binding()
    if dirty2 or (head2,tracking2,tree2,observed_after)!=(head,tracking,tree,observed_before): return fail("activation remote or clean-tree binding failed")
    output={"schema":"uninotas-closeout-handoff-v1","handoff_kind":"recovery","c0":phase_record(args.repo,c0),"c1":phase_record(args.repo,failed),"c1r":phase_record(args.repo,c1r),"consumer_bindings":c0["consumer_bindings"]+c0post["consumer_bindings"]+failed["consumer_bindings"]+c1r["consumer_bindings"],"reverse_bridge":external_bridge(c1r["reverse_bridge"]),"failure_tuple":failure,"remote_promotions":{"c0":c0["remote_promotion"],"c1":failed["remote_promotion"],"c1r":c1r["remote_promotion"]},"c0_post_verify":external_c0_post(c0post),"post_c1r_active_scan":{"scanned_head_oid":head,"outcome":"go","todo_count":len(active_paths),"active_paths":active_paths,"stale_completed_path":False},"actual_remote_main_oid":observed_after,"recovery_effective":True,"production_ready_effective":False}
    error=validate_recovery_handoff(output)
    if error: return fail(error)
    atomic_json(args.output,output); print(json.dumps(output,sort_keys=True)); return 0
def fail(message): print(f"closeout_handoff: {message}",file=sys.stderr); return 2
def main():
    parser=argparse.ArgumentParser(); subs=parser.add_subparsers(dest="command",required=True)
    p=subs.add_parser("promote"); p.add_argument("--phase",required=True); p.add_argument("--repo",required=True); p.add_argument("--expected-remote",required=True); p.add_argument("--new-commit",required=True); p.add_argument("--candidate-tree",required=True); p.add_argument("--delivery-baseline"); p.add_argument("--consumer-bindings",required=True); p.add_argument("--base-evidence"); p.add_argument("--c0-post-evidence"); p.add_argument("--implementation-reviews"); p.add_argument("--focused-review"); p.add_argument("--failure-tuple"); p.add_argument("--delphi-root"); p.add_argument("--journal",required=True); p.add_argument("--output",required=True); p.set_defaults(run=promote)
    r=subs.add_parser("resume"); r.add_argument("--phase",required=True); r.add_argument("--repo",required=True); r.add_argument("--journal",required=True); r.add_argument("--output",required=True); r.set_defaults(run=resume)
    v=subs.add_parser("verify"); v.add_argument("--phase",required=True); v.add_argument("--repo",required=True); v.add_argument("--phase-evidence",required=True); v.add_argument("--delphi-root",required=True); v.add_argument("--output",required=True); v.set_defaults(run=verify)
    a=subs.add_parser("activate"); a.add_argument("--phase",choices=("c1","c1r"),required=True); a.add_argument("--repo",required=True); a.add_argument("--c0-evidence",required=True); a.add_argument("--c0-post-evidence",required=True); a.add_argument("--c1-evidence"); a.add_argument("--failed-c1-evidence"); a.add_argument("--c1r-evidence"); a.add_argument("--failure-tuple"); a.add_argument("--delphi-root",required=True); a.add_argument("--output",required=True); a.set_defaults(run=activate)
    args=parser.parse_args(); args.repo=str(pathlib.Path(args.repo).resolve())
    for name in ("consumer_bindings","base_evidence","c0_post_evidence","implementation_reviews","focused_review","failure_tuple","journal","phase_evidence","c0_evidence","c1_evidence","failed_c1_evidence","c1r_evidence","output"):
        if hasattr(args,name) and getattr(args,name,None): setattr(args,name,normalized_artifact_path(args.repo,getattr(args,name)))
    if hasattr(args,"delphi_root") and args.delphi_root:
        try: args.delphi_root=str(resolve_delphi_root(args.repo,args.delphi_root))
        except ValueError as error: return fail(str(error))
    return args.run(args)
if __name__ == "__main__": raise SystemExit(main())
