import pathlib
import subprocess
import tempfile
import unittest


SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "enumerate_change_paths.py"


class EnumerateChangePathsTests(unittest.TestCase):
    def repo(self):
        temp = tempfile.TemporaryDirectory(); self.addCleanup(temp.cleanup)
        repo = pathlib.Path(temp.name)
        self.git(repo, "init", "-q")
        self.git(repo, "config", "user.email", "test@example.invalid")
        self.git(repo, "config", "user.name", "Test")
        (repo / "base.txt").write_text("base")
        self.git(repo, "add", "."); self.git(repo, "commit", "-qm", "base")
        return repo

    def git(self, repo, *args):
        return subprocess.run(["git", "-C", str(repo), *args], text=True, capture_output=True, check=True)

    def enumerate(self, repo, mode, baseline="HEAD", candidate=None):
        command = ["python3", str(SCRIPT), "--mode", mode, "--repo", str(repo), "--baseline", baseline]
        if candidate: command.extend(("--candidate-tree", candidate))
        return subprocess.run(command, text=True, capture_output=True)

    def test_changeset_pos_01_untracked_nonignored_file(self):
        repo = self.repo(); (repo / "z.txt").write_text("new"); (repo / ".gitignore").write_text("ignored.txt\n"); (repo / "ignored.txt").write_text("ignored")
        result = self.enumerate(repo, "delivery")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual([".gitignore", "z.txt"], result.stdout.splitlines())

    def test_changeset_pos_02_staged_delete_and_add_pair(self):
        repo = self.repo(); baseline = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        (repo / "base.txt").unlink(); (repo / "added.txt").write_text("added"); self.git(repo, "add", "-A")
        result = self.enumerate(repo, "delivery", baseline)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(["added.txt", "base.txt"], result.stdout.splitlines())

    def test_changeset_pos_03_git_recognized_rename_is_two_canonical_paths(self):
        repo = self.repo(); baseline = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        self.git(repo, "mv", "base.txt", "renamed.txt")
        status = self.git(repo, "diff", "--cached", "--name-status", "--find-renames").stdout
        self.assertTrue(status.startswith("R"), status)
        result = self.enumerate(repo, "delivery", baseline)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(["base.txt", "renamed.txt"], result.stdout.splitlines())

    def test_changeset_pos_04_ignored_file_is_excluded(self):
        repo = self.repo(); (repo / ".gitignore").write_text("ignored.txt\n"); self.git(repo, "add", ".gitignore"); self.git(repo, "commit", "-qm", "ignore")
        (repo / "ignored.txt").write_text("ignored")
        result = self.enumerate(repo, "delivery")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual([], result.stdout.splitlines())

    def test_changeset_pos_05_source_created_after_delivery_baseline_then_moved(self):
        repo = self.repo(); delivery_base = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        source = repo / "todos/active/process/TODO-uninotas-canonical-foundation-transition.md"; source.parent.mkdir(parents=True); source.write_text("active")
        self.git(repo, "add", "."); self.git(repo, "commit", "-qm", "active")
        lifecycle_base = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        destination = repo / "todos/completed/process/TODO-uninotas-canonical-foundation-transition.md"; destination.parent.mkdir(parents=True); self.git(repo, "mv", str(source.relative_to(repo)), str(destination.relative_to(repo))); self.git(repo, "commit", "-qm", "close")
        candidate = self.git(repo, "rev-parse", "HEAD^{tree}").stdout.strip()
        delivery = self.enumerate(repo, "delivery", delivery_base, candidate)
        lifecycle = self.enumerate(repo, "lifecycle", lifecycle_base, candidate)
        self.assertEqual(0, delivery.returncode, delivery.stderr); self.assertEqual(0, lifecycle.returncode, lifecycle.stderr)
        self.assertEqual(["todos/completed/process/TODO-uninotas-canonical-foundation-transition.md"], delivery.stdout.splitlines())
        self.assertEqual(["todos/active/process/TODO-uninotas-canonical-foundation-transition.md", "todos/completed/process/TODO-uninotas-canonical-foundation-transition.md"], lifecycle.stdout.splitlines())

    def test_changeset_pos_06_candidate_tree_ignores_different_worktree(self):
        repo = self.repo(); baseline = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        (repo / "indexed.txt").write_text("indexed"); self.git(repo, "add", "indexed.txt"); candidate = self.git(repo, "write-tree").stdout.strip()
        (repo / "worktree-only.txt").write_text("different")
        result = self.enumerate(repo, "delivery", baseline, candidate)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(["indexed.txt"], result.stdout.splitlines())

    def test_lifecycle_requires_ancestor_and_active_source(self):
        repo = self.repo(); baseline = self.git(repo, "rev-parse", "HEAD").stdout.strip()
        result = self.enumerate(repo, "lifecycle", baseline)
        self.assertEqual(2, result.returncode); self.assertIn("lifecycle baseline must contain active source path", result.stderr)
        source = repo / "todos/active/process/TODO-uninotas-canonical-foundation-transition.md"; source.parent.mkdir(parents=True); source.write_text("active")
        self.git(repo, "add", "."); self.git(repo, "commit", "-qm", "active")
        result = self.enumerate(repo, "lifecycle", "HEAD", baseline)
        self.assertEqual(2, result.returncode); self.assertIn("baseline must be an ancestor", result.stderr)
