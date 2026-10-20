from analyzer import analyze_repo, write_repo_data


from pathlib import Path
from json import load

EXPECTED_OUTPUT_PATH = Path(__file__).resolve().parent / "expected_output.json"

with open(EXPECTED_OUTPUT_PATH, encoding="utf-8") as file:
    EXPECTED_FILE = load(file)
    EXPECTED_BUILDINGS = EXPECTED_FILE["buildings"]
    EXPECTED_PATHS = [building["path"] for building in EXPECTED_BUILDINGS]
    EXPECTED_LINES_COUNT = [building["metrics"]["lines"] for building in EXPECTED_BUILDINGS]

def test_analyzer_output_matches_expected_output(sample_repo):
    sample_path = Path(sample_repo.workdir)
    resulting_file = analyze_repo(sample_path)
    assert resulting_file == EXPECTED_FILE
    
    resulting_buildings = resulting_file["buildings"]
    assert resulting_buildings == EXPECTED_BUILDINGS
    
    resulting_paths = [building["path"] for building in resulting_buildings]
    assert resulting_paths == EXPECTED_PATHS
    
    resulting_line_count = [building["metrics"]["lines"] for building in resulting_buildings]
    assert resulting_line_count == EXPECTED_LINES_COUNT
    
def test_analyzer_outputs_to_correct_directory(sample_repo, tmp_path):
    sample_path = Path(sample_repo.workdir)
    data = analyze_repo(sample_path)
    output_path = tmp_path / "test_repo.json"
    write_repo_data(data, output_path)
    assert output_path.is_file()
    
def test_analyzer_output_paths_in_order(sample_repo):
    sample_path = Path(sample_repo.workdir)
    resulting_buildings = analyze_repo(sample_path)["buildings"]
    resulting_paths = [building["path"] for building in resulting_buildings]
    assert resulting_paths == EXPECTED_PATHS