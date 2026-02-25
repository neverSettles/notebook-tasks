# test_final_state.py
import os
import json
import subprocess
import csv

def test_notebook_exists_and_structure():
    """Test that the Jupyter Notebook exists and has the required structure."""
    notebook_path = '/home/user/ab_test_analysis.ipynb'
    assert os.path.isfile(notebook_path), f"Expected notebook {notebook_path} is missing."

    with open(notebook_path, 'r', encoding='utf-8') as f:
        try:
            nb_data = json.load(f)
        except json.JSONDecodeError:
            assert False, f"{notebook_path} is not a valid JSON file."

    cells = nb_data.get('cells', [])
    code_cells = [c for c in cells if c.get('cell_type') == 'code']
    markdown_cells = [c for c in cells if c.get('cell_type') == 'markdown']

    assert len(code_cells) >= 6, f"Expected at least 6 code cells, found {len(code_cells)}."
    assert len(markdown_cells) >= 1, f"Expected at least 1 markdown cell, found {len(markdown_cells)}."

def test_notebook_execution():
    """Test that the notebook executes successfully."""
    notebook_path = '/home/user/ab_test_analysis.ipynb'
    assert os.path.isfile(notebook_path), f"Expected notebook {notebook_path} is missing."

    # Remove output files if they exist to ensure the notebook generates them
    for out_file in ['/home/user/conversion_plot.png', '/home/user/summary_stats.csv']:
        if os.path.exists(out_file):
            os.remove(out_file)

    result = subprocess.run(
        ['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook_path],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Notebook execution failed. stderr:\n{result.stderr}"

def test_output_files():
    """Test that the correct output files are generated with expected content."""
    png_path = '/home/user/conversion_plot.png'
    csv_path = '/home/user/summary_stats.csv'

    assert os.path.isfile(png_path), f"Expected plot image {png_path} is missing."
    with open(png_path, 'rb') as f:
        header = f.read(8)
        assert header.startswith(b'\x89PNG\r\n\x1a\n'), f"File {png_path} is not a valid PNG."

    assert os.path.isfile(csv_path), f"Expected summary CSV {csv_path} is missing."
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 2, f"Expected 2 rows of data in {csv_path}, found {len(rows)}."

    # Check control group
    control = next((r for r in rows if r.get('group') == 'control'), None)
    assert control is not None, "Missing 'control' group in summary stats."
    assert float(control.get('Conversion_Rate', 0)) == 0.2, f"Expected control conversion rate 0.2, got {control.get('Conversion_Rate')}"

    # Check treatment group
    treatment = next((r for r in rows if r.get('group') == 'treatment'), None)
    assert treatment is not None, "Missing 'treatment' group in summary stats."
    assert float(treatment.get('Conversion_Rate', 0)) == 0.6, f"Expected treatment conversion rate 0.6, got {treatment.get('Conversion_Rate')}"