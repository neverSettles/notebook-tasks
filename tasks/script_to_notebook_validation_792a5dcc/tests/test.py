# test_final_state.py
import os
import json
import csv
import re

def test_notebook_exists():
    assert os.path.exists('/home/user/production_sales_analysis.ipynb'), "The production Jupyter Notebook was not found at /home/user/production_sales_analysis.ipynb"

def test_output_csv_exists_and_valid():
    csv_path = '/home/user/final_sales_summary.csv'
    assert os.path.exists(csv_path), f"The output CSV {csv_path} was not found"

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        assert headers is not None, "CSV is empty or missing headers"
        assert 'category' in headers, "CSV missing 'category' column"
        assert 'discounted_price' in headers, "CSV missing 'discounted_price' column"

        rows = list(reader)
        assert len(rows) == 3, f"Expected 3 categories in the summary CSV, but found {len(rows)}"

        for row in rows:
            try:
                val = float(row['discounted_price'])
                assert val >= 0, f"Discounted price for {row['category']} should be non-negative"
            except ValueError:
                assert False, f"Could not parse discounted_price '{row['discounted_price']}' as a float"

def test_notebook_structure_and_validation():
    notebook_path = '/home/user/production_sales_analysis.ipynb'
    with open(notebook_path, 'r', encoding='utf-8') as f:
        try:
            nb = json.load(f)
        except json.JSONDecodeError:
            assert False, "The Jupyter Notebook is not a valid JSON file."

    cells = nb.get('cells', [])
    markdown_cells = [c for c in cells if c.get('cell_type') == 'markdown']
    code_cells = [c for c in cells if c.get('cell_type') == 'code']

    assert len(markdown_cells) >= 3, f"Expected at least 3 markdown cells (Title, Data Gen, Validation), found {len(markdown_cells)}"

    combined_code = "\n".join(["".join(c.get('source', [])) for c in code_cells])

    # Validation 1: total rows in raw data is 100
    assert re.search(r'assert\s+.*100', combined_code), "Missing assertion checking that the total number of rows is exactly 100"

    # Validation 2: minimum discounted_price is >= 0
    assert "assert" in combined_code and ">=" in combined_code and "0" in combined_code, "Missing assertion checking that the minimum discounted_price is >= 0"

    # Validation 3: sum of grouped discounted_price == sum of raw discounted_price
    assert "assert" in combined_code and ("isclose" in combined_code or "round" in combined_code or "==" in combined_code), "Missing assertion checking the sum of discounted_price between summary and raw df"