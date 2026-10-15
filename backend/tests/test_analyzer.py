from analyzer import analyze_repo, write_repo_data


from pathlib import Path
from json import load

EXPECTED_OUTPUT_PATH = Path(__file__).resolve().parent / "expected_output.json"

with open(EXPECTED_OUTPUT_PATH, encoding="utf-8") as file:
    EXPECTED_FILE = load(file)
    EXPECTED_BUILDINGS = EXPECTED_FILE['buildings']
    EXPECTED_LINES = { building["path"]: building['metrics']['lines'] for building in EXPECTED_BUILDINGS }

def test_analyzer_output_matches_expected_output(sample_repo):
    sample_path = Path(sample_repo.workdir)
    assert analyze_repo(sample_path) == EXPECTED_FILE
    
def test_analyzer_outputs_to_correct_directory(sample_repo, tmp_path):
    sample_path = Path(sample_repo.workdir)
    data = analyze_repo(sample_path)
    output_path = tmp_path / "test_repo.json"
    write_repo_data(data, output_path)
    assert output_path.is_file()
    
def test_analyzer_output_paths_in_order(sample_repo):
    expected_paths = { "buildings": [path for path in EXPECTED_LINES.keys()] }
    sample_path = Path(sample_repo.workdir)
    assert analyze_repo(sample_path) == expected_paths