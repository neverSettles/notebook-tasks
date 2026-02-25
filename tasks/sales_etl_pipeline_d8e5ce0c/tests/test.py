# test_final_state.py

import os
import csv
import json

def read_csv_as_dicts(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def test_notebook_exists():
    assert os.path.exists("/home/user/etl_pipeline.ipynb"), "The Jupyter notebook /home/user/etl_pipeline.ipynb was not created."

    # Check if it is a valid json (Jupyter notebook format)
    with open("/home/user/etl_pipeline.ipynb", 'r', encoding='utf-8') as f:
        try:
            nb = json.load(f)
            assert "cells" in nb, "The file does not appear to be a valid Jupyter notebook."
        except json.JSONDecodeError:
            assert False, "The Jupyter notebook is not valid JSON."

def test_checkpoint_1_long():
    filepath = "/home/user/checkpoint_1_long.csv"
    assert os.path.exists(filepath), f"{filepath} is missing."

    data = read_csv_as_dicts(filepath)
    assert len(data) == 12, f"Expected 12 rows in {filepath}, found {len(data)}."

    expected_rows = {
        ("S1", "North", "2023-01-01", "100.0"),
        ("S2", "South", "2023-01-01", "300.0"),
        ("S3", "East", "2023-01-01", "150.0"),
        ("S1", "North", "2023-01-02", "150.0"),
        ("S2", "South", "2023-01-02", "100.0"),
        ("S3", "East", "2023-01-02", "0.0"),
        ("S1", "North", "2023-02-01", "200.0"),
        ("S2", "South", "2023-02-01", "400.0"),
        ("S3", "East", "2023-02-01", "250.0"),
        ("S1", "North", "2023-02-02", "250.0"),
        ("S2", "South", "2023-02-02", "150.0"),
        ("S3", "East", "2023-02-02", "300.0"),
    }

    actual_rows = set()
    for row in data:
        sales = float(row.get("Sales", 0.0))
        actual_rows.add((row.get("Store_ID"), row.get("Region"), row.get("Date"), f"{sales:.1f}"))

    assert actual_rows == expected_rows, f"Data in {filepath} does not match expected output."

def test_checkpoint_2_agg():
    filepath = "/home/user/checkpoint_2_agg.csv"
    assert os.path.exists(filepath), f"{filepath} is missing."

    data = read_csv_as_dicts(filepath)
    assert len(data) == 6, f"Expected 6 rows in {filepath}, found {len(data)}."

    expected_rows = {
        ("S1", "2023-01", "250.0"),
        ("S1", "2023-02", "450.0"),
        ("S2", "2023-01", "400.0"),
        ("S2", "2023-02", "550.0"),
        ("S3", "2023-01", "150.0"),
        ("S3", "2023-02", "550.0"),
    }

    actual_rows = set()
    for row in data:
        sales = float(row.get("Total_Sales", 0.0))
        actual_rows.add((row.get("Store_ID"), row.get("Month"), f"{sales:.1f}"))

    assert actual_rows == expected_rows, f"Data in {filepath} does not match expected output."

def test_final_report():
    filepath = "/home/user/final_report.csv"
    assert os.path.exists(filepath), f"{filepath} is missing."

    data = read_csv_as_dicts(filepath)
    assert len(data) == 3, f"Expected 3 rows in {filepath}, found {len(data)}."

    expected_rows = {
        ("S1", "250.0", "450.0"),
        ("S2", "400.0", "550.0"),
        ("S3", "150.0", "550.0"),
    }

    actual_rows = set()
    for row in data:
        val1 = float(row.get("2023-01", 0.0))
        val2 = float(row.get("2023-02", 0.0))
        actual_rows.add((row.get("Store_ID"), f"{val1:.1f}", f"{val2:.1f}"))

    assert actual_rows == expected_rows, f"Data in {filepath} does not match expected output."