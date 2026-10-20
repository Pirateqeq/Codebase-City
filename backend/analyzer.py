# Analyzer module
# Inputs - Git repo path.
# Outputs - JSON file at output path using write_repo_data() with user defined name / output path.
# JSON file - contains buildings which are dictionaries with their path and metrics as keys.
from pathlib import Path
from pygit2 import Repository, Tree, Commit
from pygit2.errors import GitError
from json import dump
import sys

# Writes json file from python dictionary of git repo analysis.
# (with ouput_path.open() as file : json.dump(data, file))
def write_repo_data(data: dict, output_path: Path) -> None:
    with output_path.open("w", encoding="utf-8") as file:
        dump(data, file, indent=4)

# Reads git repo and creates the expected output in python dict to write to disk.
# Will return an empty buildings list on repo with no commits
def analyze_repo(repo_path: Path) -> dict:
    repo = Repository(repo_path)
    if repo.head_is_unborn:
        return { "buildings": [] }
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
            
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(prog="Git Repo analyzer", suggest_on_error=True)
    parser.add_argument("repo_path", type=str, help="Git path")
    parser.add_argument("file_name", type=str, help="File name")
    parser.add_argument("output_folder", type=str, nargs="?", default="", help="Optional output folder")
    
    args = parser.parse_args()
    if not args.file_name.endswith(".json"):
        args.file_name += ".json"
    
    if args.output_folder:
        output_path = Path(args.output_folder) / args.file_name
    else:
        output_path = Path(args.file_name)
        

    try:
        data = analyze_repo(Path(args.repo_path))
        write_repo_data(data, output_path)
    except GitError as e:
        print(e)
        sys.exit(1)
    except PermissionError as e:
        print(e)
        sys.exit(2)
    except FileNotFoundError as e:
        print(e)
        sys.exit(3)
    
    