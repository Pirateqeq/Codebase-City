# Analyzer module
# Inputs - Git repo path.
# Outputs - JSON file at output path using write_repo_data() with user defined name / output path.
# JSON file - contains buildings which are dictionaries with their path and metrics as keys.
from pathlib import Path
from pygit2 import Repository, Tree, Commit
from json import dump

# Writes json file from python dictionary of git repo analysis.
# (with ouput_path.open() as file : json.dump(data, file))
def write_repo_data(data: dict, output_path: Path) -> None:
    with output_path.open("w", encoding="utf-8") as file:
        dump(data, file, indent=4)
    return

# Reads git repo and creates the expected output in python dict to write to disk.
def analyze_repo(repo_path: Path) -> dict:
    repo = Repository(repo_path)
    latest_tree = repo.head.peel(Commit).tree
    
    buildings = []
    add_tree_entries(latest_tree, buildings)
    return { "buildings": buildings }

def add_tree_entries(tree: Tree, buildings: list, current_path: Path = Path()):
    for entry in tree:
        entry_path = current_path / entry.name
        if entry.type_str == "blob":
            buildings.append( { "path": entry_path.as_posix(), "metrics": { "lines": len(entry.data.splitlines()) } } )
        elif entry.type_str == "tree":
            add_tree_entries(entry, buildings, entry_path)