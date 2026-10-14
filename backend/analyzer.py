# Analyzer module
# Inputs - Git repo path.
# Outputs - JSON file at output path using write_repo_data() with user defined name / output path.
# JSON file - contains buildings which are dictionaries with their path and metrics as keys.
from pathlib import Path

# Writes json file from python dictionary of git repo analysis.
# (with ouput_path.open() as file : json.dump(data, file))
def write_repo_data(data: dict, output_path: Path) -> None:
    return

# Reads git repo and creates the expected output in python dict to write to disk.

def analyze_repo(repo_path: Path) -> dict:
    return {}