# test_final_state.py
import os
import csv
import json
import pytest

def test_notebook_exists():
    notebook_path = "/home/user/clean_imputation.ipynb"
    assert os.path.isfile(notebook_path), f"The Jupyter notebook was not found at {notebook_path}."

    # Ensure it's valid JSON (a basic check for ipynb)
    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)
        assert "cells" in notebook, "The notebook file does not contain 'cells'."
    except json.JSONDecodeError:
        pytest.fail(f"The file at {notebook_path} is not a valid Jupyter Notebook (invalid JSON).")

def test_cleaned_data_exists():
    output_csv = "/home/user/cleaned_financial_data.csv"
    assert os.path.isfile(output_csv), f"The cleaned data file was not found at {output_csv}."

def test_cleaned_data_content():
    output_csv = "/home/user/cleaned_financial_data.csv"

    expected_data = {
        "2023-01-01": {"Revenue": 1000.0, "Expenses": 800.0, "Profit": 200.0},
        "2023-01-02": {"Revenue": 1000.0, "Expenses": 850.0, "Profit": 150.0},
        "2023-01-03": {"Revenue": 1200.0, "Expenses": 850.0, "Profit": 350.0},
        "2023-01-04": {"Revenue": 1300.0, "Expenses": 900.0, "Profit": 400.0},
        "2023-01-05": {"Revenue": 1300.0, "Expenses": 850.0, "Profit": 450.0},
    }

    with open(output_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        # Check that 'Date', 'Revenue', 'Expenses', 'Profit' exist
        assert fieldnames is not None, "CSV is empty"
        assert "Date" in fieldnames, "The output CSV must contain the 'Date' column."
        assert "Revenue" in fieldnames, "The output CSV must contain the 'Revenue' column."
        assert "Expenses" in fieldnames, "The output CSV must contain the 'Expenses' column."
        assert "Profit" in fieldnames, "The output CSV must contain the 'Profit' column."

        rows = list(reader)

    assert len(rows) == len(expected_data), f"Expected {len(expected_data)} rows in the cleaned CSV, but found {len(rows)}."

    for row in rows:
        date = row.get("Date")
        assert date in expected_data, f"Unexpected date '{date}' found in the cleaned CSV."

        expected_row = expected_data[date]

        try:
            revenue = float(row["Revenue"])
            expenses = float(row["Expenses"])
            profit = float(row["Profit"])
        except ValueError:
            pytest.fail(f"Non-numeric data found in row for date {date}: {row}")

        assert revenue == pytest.approx(expected_row["Revenue"], abs=0.01), \
            f"Incorrect Revenue for {date}. Expected {expected_row['Revenue']}, got {revenue}."

        assert expenses == pytest.approx(expected_row["Expenses"], abs=0.01), \
            f"Incorrect Expenses for {date}. Expected {expected_row['Expenses']}, got {expenses}. Did you use the mean correctly?"

        assert profit == pytest.approx(expected_row["Profit"], abs=0.01), \
            f"Incorrect Profit for {date}. Expected {expected_row['Profit']}, got {profit}."