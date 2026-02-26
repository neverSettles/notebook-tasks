# test_final_state.py
import os
import csv
import json
import pytest

def test_notebook_exists():
    """Verify that the Jupyter notebook has been created."""
    notebook_path = '/home/user/clean_pipeline.ipynb'
    assert os.path.isfile(notebook_path), f"The notebook file {notebook_path} does not exist."

    # Optionally, verify it's a valid JSON (which notebooks are)
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
            assert "cells" in nb, "The notebook file does not contain 'cells' and may be malformed."
    except Exception as e:
        pytest.fail(f"Could not parse {notebook_path} as a valid Jupyter notebook JSON: {e}")

def test_output_csv_exists():
    """Verify that the output training data CSV exists."""
    output_path = '/home/user/ml_training_data.csv'
    assert os.path.isfile(output_path), f"The expected output file {output_path} does not exist."

def test_output_csv_content():
    """Verify the content, columns, and sorting of the exported CSV."""
    output_path = '/home/user/ml_training_data.csv'
    assert os.path.isfile(output_path), "Missing output CSV."

    expected_data = [
        {'store_id': '1', 'store_type': 'Retail', 'profit_label': '1', 'region': 'North', 'top_category': 'Electronics'},
        {'store_id': '2', 'store_type': 'Warehouse', 'profit_label': '0', 'region': 'South', 'top_category': 'Furniture'},
        {'store_id': '3', 'store_type': 'Retail', 'profit_label': '1', 'region': 'East', 'top_category': 'Clothing'},
        {'store_id': '4', 'store_type': 'Online', 'profit_label': '1', 'region': 'West', 'top_category': 'Electronics'},
        {'store_id': '5', 'store_type': 'Warehouse', 'profit_label': '0', 'region': 'North', 'top_category': 'Groceries'},
    ]

    with open(output_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        assert fieldnames is not None, "Output CSV is empty or has no headers."

        expected_columns = {'store_id', 'store_type', 'profit_label', 'region', 'top_category'}
        assert set(fieldnames) == expected_columns, f"CSV columns {set(fieldnames)} do not match expected {expected_columns}."

        rows = list(reader)
        assert len(rows) == len(expected_data), f"Expected {len(expected_data)} rows, found {len(rows)}."

        # Verify sorting
        store_ids = [int(row['store_id']) for row in rows]
        assert store_ids == sorted(store_ids), "The CSV is not sorted by store_id in ascending order."

        # Verify exact data
        for actual, expected in zip(rows, expected_data):
            for col in expected_columns:
                assert actual[col] == expected[col], f"Mismatch in row for store {expected['store_id']} at column {col}: expected '{expected[col]}', found '{actual[col]}'."


def test_train_test_split():
    """Verify train/test split files."""
    import csv
    for name in ["train.csv", "test.csv"]:
        path = f"/home/user/{name}"
        assert os.path.exists(path), f"{name} missing at {path}"
        with open(path) as f:
            rows = list(csv.DictReader(f))
        assert len(rows) > 0, f"{name} is empty"

def test_split_report():
    import json
    path = "/home/user/split_report.json"
    assert os.path.exists(path), f"Split report missing"
    with open(path) as f:
        data = json.load(f)
    assert data["train_size"] > data["test_size"], "Train should be larger than test"
    assert "n_features" in data, "Missing n_features"
    assert "correlation_max" in data, "Missing correlation_max"

def test_correlation_heatmap():
    assert os.path.exists("/home/user/correlation_heatmap.png"), "Correlation heatmap missing"

