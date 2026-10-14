from pathlib import Path

from pygit2 import Index
from pygit2.enums import SortMode
from pytest import mark

from json import load

EXPECTED_OUTPUT_PATH = Path(__file__).resolve().parent / "expected_output.json"

with open(EXPECTED_OUTPUT_PATH, encoding="utf-8") as file:
    EXPECTED_OUTPUT = load(file)["buildings"]
    EXPECTED_LINES = { building["path"]: building['metrics']['lines'] for building in EXPECTED_OUTPUT }

def tree_paths(tree):
    """Every blob path in a tree"""
    index = Index()
    index.read_tree(tree)
    return {entry.path for entry in index}

# Commited files

def test_expected_lines_match_files_table(repo_files):
    commited = {f['path'] for f in repo_files if f['state'] in ["commit1", "commit2"]}
    assert set(EXPECTED_LINES) == commited
    
def test_head_contains_exactly_commited_paths(head_tree):
    paths = tree_paths(head_tree)
    assert len(paths) == 6
    assert paths == set(EXPECTED_LINES)
    
@mark.parametrize("path, lines", EXPECTED_LINES.items())
def test_commited_file_line_count(head_tree, path, lines):
    blob = head_tree[path]
    assert len(blob.data.splitlines()) == lines
    
# Commit count

def test_history_has_two_commits(sample_repo):
    walker = sample_repo.walk(
        sample_repo.head.target, SortMode.TOPOLOGICAL | SortMode.REVERSE
    )
    commits = list(walker)
    assert len(commits) == 2
    assert [c.message for c in commits] == ["First commit", "Second commit"]
    
# Excluded files

def test_staged_file_in_index_but_not_head(sample_repo, head_tree):
    assert "staged.py" in sample_repo.index
    assert "staged.py" not in tree_paths(head_tree)
    
@mark.parametrize("path", ["scratch.txt", "debug.log"])
def test_disk_only_files_not_in_index_or_head(sample_repo, head_tree, path):
    assert (Path(sample_repo.workdir) / path).is_file()
    assert path not in sample_repo.index
    assert path not in tree_paths(head_tree)
    
# Ignored vs untracked
def test_debug_log_is_ignored_not_just_untracked(sample_repo):
    assert sample_repo.path_is_ignored("debug.log")
    assert not sample_repo.path_is_ignored("scratch.txt")