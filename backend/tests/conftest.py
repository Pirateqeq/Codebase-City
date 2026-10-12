from pytest import fixture
from pygit2 import init_repository, Signature, Repository, Commit

FILES = (
    {
        "path": ".gitignore",
        "state": "commit1",
        "content": "*.log"
    },
    { 
        "path": "README.md",
        "state": "commit1",
        "content": "one\ntwo\nthree\n"
    },
    {
        "path": "src/main.py",
        "state": "commit1",
        "content": "one\ntwo\nthree\nfour\nfive\n"
    },
    {
        "path": "src/empty.py",
        "state": "commit1",
        "content": ""
    },
    {
        "path": "notes.txt",
        "state": "commit2",
        "content": "one\ntwo"
    },
    {
        "path": "windows.txt",
        "state": "commit2",
        "content": "one\r\ntwo\r\n"
    },
    {
        "path": "scratch.txt",
        "state": "untracked",
        "content": "Lorem ipsum dolor sit amet."
    },
    {
        "path": "staged.py",
        "state": "staged",
        "content": "Lorem ipsum dolor sit amet."
    },
    {
        "path": "debug.log",
        "state": "ignored",
        "content": "Lorem ipsum dolor sit amet."
    }
)

@fixture
def repo_files():
    """The FILES table"""
    return FILES


@fixture
def sample_repo(tmp_path):
    """Build a temp repo with pygit2"""
    repo_path = tmp_path / "test_repo"
    repo_path.mkdir()
    repo = init_repository(str(repo_path))
    repo.config["core.autocrlf"] = False
    index = repo.index
    sig = Signature("Test", "text@example.com", 0, 0)
    
    def write_file(file):
        file_path = repo_path / file["path"]
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(file["content"], encoding="utf-8", newline="")

    def commit(message):
        index.write()
        tree = index.write_tree()
        parents = [] if repo.head_is_unborn else [repo.head.target]
        repo.create_commit("HEAD", sig, sig, message, tree, parents)
    
    # Commits in order
    for state, message in ( ("commit1", "First commit"), ("commit2", "Second commit")):
        for file in FILES:
            if file["state"] == state:
                write_file(file)
                index.add(file["path"])
        commit(message)
        
    # Staged but not commited
    for file in FILES:
        if file["state"] == "staged":
            write_file(file)
            index.add(file["path"])
    index.write()
    
    # On disk only
    for file in FILES:
        if file["state"] in {"untracked", "ignored"}:
            write_file(file)
            
    repo.free()
    reopened = Repository(str(repo_path))
    yield reopened
    reopened.free()
    
@fixture
def head_tree(sample_repo):
    """The file tree of the commit HEAD oiubts to."""
    return sample_repo.head.peel(Commit).tree
