#!/usr/bin/env python3
"""Canonical sorted path-set enumerator for delivery and C0→C1 lifecycle views."""
import argparse
import os
import subprocess
import sys

def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], text=True, capture_output=True, check=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("delivery", "lifecycle"), required=True)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--candidate-tree")
    args = parser.parse_args()
    candidate = args.candidate_tree
    ancestry_target = candidate or "HEAD"
    if candidate:
        object_type = git(args.repo, "cat-file", "-t", candidate)
        if object_type.returncode: return fail("candidate tree must resolve to a Git object")
        if object_type.stdout.strip() == "tree": ancestry_target = "HEAD"
        elif object_type.stdout.strip() != "commit": return fail("candidate tree must be a tree or commit")
    ancestor = git(args.repo, "merge-base", "--is-ancestor", args.baseline, ancestry_target)
    if ancestor.returncode:
        return fail("baseline must be an ancestor of candidate tree")
    if args.mode == "lifecycle":
        source = "todos/active/process/TODO-uninotas-canonical-foundation-transition.md"
        exists = git(args.repo, "cat-file", "-e", f"{args.baseline}:{source}")
        if exists.returncode: return fail("lifecycle baseline must contain active source path")
    diff_args = ("diff", "--no-renames", "--name-only", args.baseline, *( (candidate,) if candidate else () ))
    changed = git(args.repo, *diff_args)
    if changed.returncode: return fail(changed.stderr.strip())
    paths = {line for line in changed.stdout.splitlines() if line}
    if args.mode == "delivery" and not args.candidate_tree:
        untracked = git(args.repo, "ls-files", "--others", "--exclude-standard")
        if untracked.returncode: return fail(untracked.stderr.strip())
        paths.update(line for line in untracked.stdout.splitlines() if line)
    if paths: print("\n".join(sorted(paths, key=os.fsencode)))
    return 0

def fail(message):
    print(f"enumerate_change_paths: {message}", file=sys.stderr)
    return 2

if __name__ == "__main__": raise SystemExit(main())
