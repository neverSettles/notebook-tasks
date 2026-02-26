# test_final_state.py

import os
import csv
import subprocess
import math

def test_notebook_execution_and_output():
    notebook_path = "/home/user/etl_pipeline.ipynb"
    output_path = "/home/user/clean_sales.csv"

    # Verify notebook exists
    assert os.path.exists(notebook_path), f"Notebook not found at {notebook_path}"

    # Execute the notebook
    try:
        subprocess.run(
            ["jupyter", "nbconvert", "--to", "notebook", "--execute", notebook_path],
            check=True,
            capture_output=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        assert False, f"Notebook execution failed.\nStdout: {e.stdout}\nStderr: {e.stderr}"

    # Verify output CSV exists
    assert os.path.exists(output_path), f"Output file not found at {output_path}"

    with open(output_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        # Check columns
        expected_columns = ["region", "total_revenue", "sales_rank"]
        assert fieldnames == expected_columns, f"Expected columns {expected_columns}, but got {fieldnames}"

        rows = list(reader)

    # Check number of rows
    assert len(rows) == 4, f"Expected 4 rows, got {len(rows)}"

    # Parse rows into a dictionary for easier validation
    results = {}
    for row in rows:
        region = row["region"]
        results[region] = {
            "total_revenue": float(row["total_revenue"]),
            "sales_rank": int(row["sales_rank"])
        }

    # Expected results
    expected_data = {
        "West": {"total_revenue": 500.0, "sales_rank": 1},
        "East": {"total_revenue": 350.0, "sales_rank": 2},
        "South": {"total_revenue": 300.0, "sales_rank": 3},
        "North": {"total_revenue": 250.75, "sales_rank": 4},
    }

    for region, expected in expected_data.items():
        assert region in results, f"Region '{region}' not found in the output CSV."
        actual_revenue = results[region]["total_revenue"]
        expected_revenue = expected["total_revenue"]
        assert math.isclose(actual_revenue, expected_revenue, rel_tol=1e-5), \
            f"Expected revenue for {region} to be {expected_revenue}, got {actual_revenue}"

        actual_rank = results[region]["sales_rank"]
        expected_rank = expected["sales_rank"]
        assert actual_rank == expected_rank, \
            f"Expected rank for {region} to be {expected_rank}, got {actual_rank}"


def test_running_totals():
    """Verify running totals CSV."""
    import csv
    path = "/home/user/running_totals.csv"
    assert os.path.exists(path), f"Running totals CSV missing"
    with open(path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert len(rows) > 0, "Running totals CSV is empty"
    assert 'running_total' in reader.fieldnames, "Missing running_total column"
    assert 'region' in reader.fieldnames, "Missing region column"

def test_revenue_chart():
    assert os.path.exists("/home/user/revenue_chart.png"), "Revenue chart missing"

