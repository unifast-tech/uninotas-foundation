#!/usr/bin/env python3
"""Tree-native validator for the bounded C0→C1 and C1→C1R closeout deltas."""
import argparse
import json
import re
import subprocess
import sys

ACTIVE = "todos/active/process/TODO-uninotas-canonical-foundation-transition.md"
COMPLETED = "todos/completed/process/TODO-uninotas-canonical-foundation-transition.md"
STATIC = {"artifacts/publication-manifest.txt", "artifacts/feature-briefs/uninotas-smart-notas-central.md", "todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md"}
EXPECTED = STATIC | {ACTIVE, COMPLETED}
MUTABLE = re.compile(r"^(?:- \*\*(?:Lifecycle state|Current delivery stage|Qualifiers|Next exact step|Work state|Why this state now|Exit condition|C0 active implementation/genesis commit|C0 remote verification|Disposition|Disposition reason|Post-commit/push status|Next path/status action):\*\*.*|\| Foundation UniNotas cutover \|.*|(?:Failure-Tuple|Observed-Failure):.*)\n?", re.M)
OID = re.compile(r"\b[0-9a-f]{40}\b")
FAILURE_RE=re.compile(r"^Failure-Tuple: failure_id=([A-Za-z0-9._-]{1,64}); failed_c1_oid=([0-9a-f]{40}); predicate=(parent_mismatch|ancestry_failure|head_origin_mismatch|actual_remote_mismatch|semantic_scan_mismatch); observed=([A-Za-z0-9._:-]{1,160}); recorded_at_utc=(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)$",re.M)
C0_REVIEW=("privacy-review-c0","architecture-adherence-c0","security-review-c0","test-quality-c0","final-review-c0","verification-debt-c0","triple-performance-c0","triple-test-quality-c0","triple-cutover-integrity-c0","performance-concurrency-c0")
IMPLEMENTATION_REVIEW_KEYS={"consumer_id","phase","candidate_tree_oid","exact_path_set","reviewer_or_session","outcome","scope"}
FOCUSED_REVIEW_KEYS={"consumer_id","phase","candidate_tree_oid","exact_path_set","reviewer_or_session","outcome"}
REVIEWER_SESSION_RE=re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:@/-]{0,127}$")

def git(repo, *args): return subprocess.run(["git", "-C", repo, *args], text=True, capture_output=True)
def blob(repo, tree, path):
    result = git(repo, "show", f"{tree}:{path}")
    return None if result.returncode else result.stdout
def frozen(text): return MUTABLE.sub("", text).strip()
def fail(message): print(f"validate_closeout_diff: {message}", file=sys.stderr); return 2

def strict_object(pairs):
    value={}
    for key,item in pairs:
        if key in value: raise ValueError("duplicate JSON member")
        value[key]=item
    return value

def load_json(path):
    try: return json.loads(open(path, encoding="utf-8").read(),object_pairs_hook=strict_object,parse_constant=lambda _: (_ for _ in ()).throw(ValueError("non-finite JSON number")))
    except (OSError, json.JSONDecodeError, ValueError): raise ValueError("review attestation input is invalid")

def complete_proof(proof, mode, implementation_reviews, focused_review, implementation_tree):
    phase="c1" if mode=="closeout" else "c1r"
    focused_id="closeout-integrity-review-c1" if phase=="c1" else "recovery-integrity-review-c1r"
    if not isinstance(implementation_reviews,list): raise ValueError("implementation review attestations are required")
    carried={}
    for row in implementation_reviews:
        paths=row.get("exact_path_set") if isinstance(row,dict) else None
        if (not isinstance(row,dict) or set(row)!=IMPLEMENTATION_REVIEW_KEYS or row.get("consumer_id") in carried
                or row.get("phase")!="C0" or row.get("candidate_tree_oid")!=implementation_tree
                or not isinstance(paths,list) or paths!=sorted(set(paths)) or not paths
                or any(not isinstance(path,str) or not path for path in paths)
                or not isinstance(row.get("reviewer_or_session"),str) or not REVIEWER_SESSION_RE.fullmatch(row["reviewer_or_session"])
                or row.get("outcome")!="no_material_findings" or row.get("scope")!="implementation_content"):
            raise ValueError("implementation review attestations are not bound to C0 tree and exact path set")
        carried[row["consumer_id"]]=row
    if set(carried)!=set(C0_REVIEW) or len({tuple(row["exact_path_set"]) for row in carried.values()})!=1:
        raise ValueError("implementation review attestations are not bound to C0 tree and exact path set")
    expected_focused={"consumer_id":focused_id,"phase":phase.upper(),"candidate_tree_oid":proof["candidate_tree"],"exact_path_set":proof["exact_delta"],"reviewer_or_session":focused_review.get("reviewer_or_session") if isinstance(focused_review,dict) else None,"outcome":"no_material_findings"}
    if (not isinstance(focused_review,dict) or set(focused_review)!=FOCUSED_REVIEW_KEYS
            or not isinstance(focused_review.get("reviewer_or_session"),str) or not REVIEWER_SESSION_RE.fullmatch(focused_review["reviewer_or_session"])
            or focused_review!=expected_focused):
        raise ValueError(f"focused {phase.upper()} review is not bound to candidate tree and exact delta")
    return {**proof,"phase":phase,"implementation_reviews":implementation_reviews,"focused_review":focused_review}

def completed_prerequisites(text):
    """Read the governing TODO's checked criteria and evidence matrix, not a toy schema."""
    if not all(section in text for section in ("## Definition of Done", "## Validation Steps", "## Completion Evidence Matrix")): return False
    dod = re.findall(r"^- \[([ x])\] `DOD-\d+`", text, re.M)
    val = re.findall(r"^- \[([ x])\] `VAL-(\d+)`", text, re.M)
    if len(dod) != 15 or any(mark != "x" for mark in dod): return False
    if len(val) != 10 or any(mark != "x" for mark, _ in val): return False
    rows = re.findall(r"^\| `(DOD-\d+|VAL-\d+)` \|.*?\| (passed|planned|completed) \|", text, re.M)
    statuses = dict(rows)
    return all(statuses.get(f"DOD-{number:02d}") == "passed" for number in range(1, 16)) and all(statuses.get(f"VAL-{number:02d}") == "passed" for number in range(1, 11))

def field_line(text, label):
    match=re.search(rf"^- \*\*{re.escape(label)}:\*\*.*$", text, re.M)
    return match.group(0) if match else None

def typed_fields_unique(text):
    labels=("Lifecycle state","Current delivery stage","Qualifiers","Next exact step","Work state","Why this state now","Exit condition","C0 active implementation/genesis commit","C0 remote verification","Disposition","Disposition reason","Post-commit/push status","Next path/status action")
    return all(len(re.findall(rf"^- \*\*{re.escape(label)}:\*\*",text,re.M)) == 1 for label in labels) and len(re.findall(r"^\| Foundation UniNotas cutover \|",text,re.M)) == 1 and len(re.findall(r"^Failure-Tuple:",text,re.M)) <= 1 and len(re.findall(r"^Observed-Failure:",text,re.M)) <= 1

def c0_state_is_exact(text):
    required=(
        "**Lifecycle state:** `Active — planning`",
        "**Current delivery stage:** `Local-Implemented`",
        "**Qualifiers:** `none`",
        "**Next exact step:** validate final independent reviews, then promote C0 to main by CAS",
        "**Work state:** `review`",
        "**Why this state now:** implementation and primary validation complete; independent delivery audits and C0 publication remain.",
        "**Exit condition:** all delivery reviews and guards green; C0 published and verified before atomic C1 formation.",
        "**Disposition:** `keep-active`",
        "**Disposition reason:** implementation locally complete; independent delivery gates and C0 publication remain.",
        "**Post-commit/push status:** `pending`",
        "**Next path/status action:** finish independent reviews, publish/verify C0, then form atomic C1",
    )
    section=re.search(r"^## Module Consolidation Gate\s*$(.*?)(?=^## |\Z)",text,re.M|re.S)
    checks=re.findall(r"^- \[([ x])\] ",section.group(1),re.M) if section else []
    return all(value in text for value in required) and len(checks)==5 and all(mark=="x" for mark in checks)

def c1_state_is_exact(text, base_text, base_oid):
    required=(
        "**Lifecycle state:** `Completed — conditional Production-Ready candidate`",
        "**Current delivery stage:** `Production-Ready`",
        "**Qualifiers:** `Provisional`",
        "**Next exact step:** external C1 remote verification + semantic active scan handoff",
        "**Work state:** `review`",
        "**Disposition:** `move-completed`",
        "**Disposition reason:** candidate C1 guards green; Production-Ready remains conditional on external handoff",
        "**Post-commit/push status:** `C0 verified; C1 external verification pending`",
        "**Next path/status action:** external C1 verification + active scan handoff",
    )
    promotion=re.search(rf"^\| Foundation UniNotas cutover \| `main@{base_oid}` \| `n/a — main-only authority` \| `n/a` \| `origin/main@{base_oid}` \| C1 conditional; external activation pending \|$", text, re.M)
    return (all(value in text for value in required) and promotion is not None
            and f"**C0 active implementation/genesis commit:** `{base_oid}`" in text
            and f"**C0 remote verification:** `fresh remote/origin/main/base HEAD all observed as {base_oid}`" in text
            and field_line(text, "Why this state now") == field_line(base_text, "Why this state now")
            and field_line(text, "Exit condition") == field_line(base_text, "Exit condition"))

def c1r_state_is_exact(text, base_text, failed_c1_oid):
    captured=re.search(r"\*\*C0 active implementation/genesis commit:\*\* `([0-9a-f]{40})`", base_text)
    c0_oid=captured.group(1) if captured else None
    required=("**Lifecycle state:** `Active — blocked recovery`", "**Current delivery stage:** `Local-Implemented`", "**Qualifiers:** `Blocked`", "**Next exact step:** reconcile observed C1 failure and rerun atomic closeout", "**Work state:** `blocked`", "**Why this state now:** published C1 failed external activation", "**Exit condition:** failure reconciled and exact closeout protocol green", "**Disposition:** `blocked`", "**Disposition reason:** published C1 failed external activation", "**Post-commit/push status:** `FAILED_C1 observed; C1R recovery pending`", "**Next path/status action:** publish/verify C1R then reconcile blocker", "Observed-Failure: external_verification_failed")
    promotion=re.search(rf"^\| Foundation UniNotas cutover \| `main@{c0_oid or ''}` \| `n/a — main-only authority` \| `n/a` \| `origin/main@{c0_oid or ''}` \| C1 external activation failed; C1R recovery in progress \|$", text, re.M)
    failure=re.search(r"^Failure-Tuple: failure_id=([A-Za-z0-9._-]{1,64}); failed_c1_oid=([0-9a-f]{40}); predicate=(parent_mismatch|ancestry_failure|head_origin_mismatch|actual_remote_mismatch|semantic_scan_mismatch); observed=([A-Za-z0-9._:-]{1,160}); recorded_at_utc=(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)$", text, re.M)
    return (c0_oid is not None and all(item in text for item in required) and promotion is not None
            and failure is not None and failure.group(2) == failed_c1_oid
            and field_line(text, "C0 active implementation/genesis commit") == field_line(base_text, "C0 active implementation/genesis commit")
            and field_line(text, "C0 remote verification") == field_line(base_text, "C0 remote verification"))

def validate(repo, base, candidate, mode, implementation_reviews=None, focused_review=None):
    recovery_failure=None
    candidate_type = git(repo, "cat-file", "-t", candidate)
    if candidate_type.returncode or candidate_type.stdout.strip() not in {"tree", "commit"}: return None, "candidate tree must resolve to a Git tree or commit"
    base_tree = git(repo, "rev-parse", f"{base}^{{tree}}")
    candidate_tree = git(repo, "rev-parse", f"{candidate}^{{tree}}")
    if base_tree.returncode or candidate_tree.returncode: return None, "base and candidate trees must resolve"
    changed = git(repo, "diff", "--no-renames", "--name-only", base_tree.stdout.strip(), candidate_tree.stdout.strip())
    paths = {line for line in changed.stdout.splitlines() if line}
    if paths != EXPECTED: return None, "final closeout changed a non-allowlisted path or backlink content"
    source, destination = (ACTIVE, COMPLETED) if mode == "closeout" else (COMPLETED, ACTIVE)
    base_todo, candidate_todo = blob(repo, base, source), blob(repo, candidate, destination)
    if base_todo is None or candidate_todo is None or blob(repo, candidate, source) is not None: return None, "mode and canonical TODO path disagree"
    if not typed_fields_unique(candidate_todo): return None, "closeout mutable state contains duplicate or unknown field"
    failure_markers=(len(re.findall(r"^Failure-Tuple:",candidate_todo,re.M)),len(re.findall(r"^Observed-Failure:",candidate_todo,re.M)))
    if mode=="closeout" and failure_markers!=(0,0): return None, "successful closeout cannot contain recovery-only failure markers"
    if mode=="recovery" and failure_markers!=(1,1): return None, "recovery requires exactly one failure tuple and observed-failure marker"
    if frozen(base_todo) != frozen(candidate_todo): return None, "closeout recovery may only restore lifecycle truth and observed failure evidence" if mode == "recovery" else "final closeout changed frozen contract content"
    for path in STATIC:
        before, after = blob(repo, base, path), blob(repo, candidate, path)
        if before is None or after is None or before.replace(source, destination) != after: return None, "final closeout changed frozen promotion scope or threshold cell"
    if mode == "closeout":
        if not c0_state_is_exact(base_todo): return None, "C0 source state is not delivery-ready"
        if not completed_prerequisites(base_todo): return None, "completed path requires all repository-verifiable criteria complete"
        if re.search(r"^Criterion:\s*validate_closeout_diff\s*$", base_todo, re.M): return None, "completion criterion cannot require its own enforcing guard result as input evidence"
        base_oid=git(repo, "rev-parse", base).stdout.strip()
        if set(OID.findall(candidate_todo)) - set(OID.findall(base_todo)) - {base_oid}: return None, "final closeout cannot persist facts that depend on the uncreated C1 OID"
        if not c1_state_is_exact(candidate_todo, base_todo, base_oid): return None, "final closeout used a non-contract stage or disposition transition"
    else:
        if "Observed-Failure: external_verification_failed" not in candidate_todo: return None, "failed external closeout verification requires corrective active-state recovery"
        failed_c1_oid=git(repo, "rev-parse", base).stdout.strip()
        if not c1r_state_is_exact(candidate_todo, base_todo, failed_c1_oid): return None, "recovery changed a byte-frozen field or used an invalid failure tuple"
        match=FAILURE_RE.search(candidate_todo)
        recovery_failure={"failure_id":match.group(1),"failed_c1_oid":match.group(2),"predicate":match.group(3),"observed":match.group(4),"recorded_at_utc":match.group(5)}
    proof = {"validator": "validate_closeout_diff.py", "base_commit": git(repo, "rev-parse", base).stdout.strip(), "base_tree": base_tree.stdout.strip(), "candidate_tree": candidate_tree.stdout.strip(), "exact_delta": sorted(paths), "outcome": "go"}
    if recovery_failure is not None: proof["failure_tuple"]=recovery_failure
    implementation_tree=base_tree.stdout.strip()
    if mode=="recovery":
        match=re.search(r"\*\*C0 active implementation/genesis commit:\*\* `([0-9a-f]{40})`", base_todo)
        if not match: return None, "recovery requires the exact C0 genesis binding"
        resolved=git(repo,"rev-parse",f"{match.group(1)}^{{tree}}")
        if resolved.returncode: return None, "recovery requires the exact C0 genesis binding"
        implementation_tree=resolved.stdout.strip()
    try: proof=complete_proof(proof,mode,implementation_reviews,focused_review,implementation_tree)
    except ValueError as error: return None,str(error)
    return proof, None

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--mode", choices=("closeout", "recovery"), default="closeout"); parser.add_argument("--repo", required=True); parser.add_argument("--base", required=True); parser.add_argument("--candidate-tree", required=True); parser.add_argument("--todo", required=True); parser.add_argument("--implementation-reviews", required=True); parser.add_argument("--focused-review", required=True); args = parser.parse_args()
    required = COMPLETED if args.mode == "closeout" else ACTIVE
    if args.todo != required: return fail("mode and canonical TODO path disagree")
    try: implementation_reviews,focused_review=load_json(args.implementation_reviews),load_json(args.focused_review)
    except ValueError as error: return fail(str(error))
    proof, error = validate(args.repo, args.base, args.candidate_tree, args.mode,implementation_reviews,focused_review)
    if error: return fail(error)
    print(json.dumps(proof, sort_keys=True)); return 0
if __name__ == "__main__": raise SystemExit(main())
