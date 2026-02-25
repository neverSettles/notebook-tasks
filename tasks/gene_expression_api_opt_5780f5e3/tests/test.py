# test_final_state.py
import os
import csv
import time
import subprocess

def test_notebook_execution_time_and_output():
    notebook_path = '/home/user/fetch_data.ipynb'
    output_notebook_path = '/home/user/fetch_data_out.ipynb'
    output_csv_path = '/home/user/expression_data.csv'

    # Remove output CSV if it exists to ensure we are testing the new run
    if os.path.exists(output_csv_path):
        os.remove(output_csv_path)

    start_time = time.time()

    # Execute the notebook
    result = subprocess.run(
        [
            'jupyter', 'nbconvert', 
            '--to', 'notebook', 
            '--execute', notebook_path, 
            '--output', output_notebook_path
        ],
        capture_output=True,
        text=True
    )

    duration = time.time() - start_time

    # Ensure notebook executed successfully
    assert result.returncode == 0, f"Notebook execution failed: {result.stderr}"

    # Check duration (optimized version should be much faster than 10s, requirement is < 4s execution, 
    # but allowing up to 6.0s for nbconvert overhead to be safe)
    assert duration < 6.0, f"Notebook execution took {duration:.2f}s, which is too slow. Expected < 4s (with some nbconvert overhead). Did you use parallel execution?"

    # Check if CSV exists
    assert os.path.exists(output_csv_path), f"Output CSV not found at {output_csv_path}"

    # Read CSV and verify contents
    with open(output_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Check columns
    expected_columns = ['gene_id', 'expression_level', 'sample_id']
    assert fieldnames == expected_columns, f"Incorrect columns. Expected {expected_columns}, got {fieldnames}"

    # Check row count
    assert len(rows) == 200, f"Expected 200 rows in CSV, got {len(rows)}"

    # Check sorting by gene_id
    gene_ids = [row['gene_id'] for row in rows]
    expected_gene_ids = [f"GENE_{i:03d}" for i in range(200)]

    assert gene_ids == expected_gene_ids, "Data is not sorted correctly by 'gene_id' in ascending order."

    # Validate some data values
    assert rows[0]['sample_id'] == 'S1', f"Expected sample_id to be 'S1', got {rows[0]['sample_id']}"
    assert abs(float(rows[0]['expression_level']) - 10.6) < 0.01, f"Expected first row expression_level approx 10.6, got {rows[0]['expression_level']}"