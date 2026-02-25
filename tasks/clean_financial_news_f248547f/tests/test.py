# test_final_state.py

import os
import csv
import json
import pytest

def test_notebook_exists():
    """Verify that the Jupyter notebook was created."""
    notebook_path = "/home/user/clean_analysis.ipynb"
    assert os.path.exists(notebook_path), f"Notebook not found at {notebook_path}"

def test_notebook_is_valid_json():
    """Verify that the notebook is a valid JSON (Jupyter notebook format)."""
    notebook_path = "/home/user/clean_analysis.ipynb"
    if os.path.exists(notebook_path):
        with open(notebook_path, "r", encoding="utf-8") as f:
            try:
                json.load(f)
            except json.JSONDecodeError:
                pytest.fail(f"Notebook {notebook_path} is not a valid JSON file.")

def test_output_csv_exists():
    """Verify that the output CSV file was created."""
    output_csv = "/home/user/cleaned_news.csv"
    assert os.path.exists(output_csv), f"Output CSV not found at {output_csv}"

def test_output_csv_contents():
    """Verify the columns and data inside the cleaned output CSV."""
    output_csv = "/home/user/cleaned_news.csv"
    if not os.path.exists(output_csv):
        pytest.skip("Output CSV does not exist; skipping content checks.")

    with open(output_csv, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            headers = next(reader)
        except StopIteration:
            pytest.fail(f"Output CSV {output_csv} is empty.")

        expected_columns = ["date", "cleaned_headline", "price"]
        assert headers == expected_columns, f"Incorrect columns in output. Expected {expected_columns}, got {headers}"

        actual_headlines = []
        for row in reader:
            if len(row) >= 2:
                actual_headlines.append(row[1])

        expected_headlines = [
            "company xyz announces new product",
            "terrible day markets",
            "economic boom horizon",
            "investors looking safe havens"
        ]

        assert actual_headlines == expected_headlines, (
            f"Headlines not cleaned correctly.\nExpected: {expected_headlines}\nGot: {actual_headlines}"
        )