# test_final_state.py
import os
import sqlite3
import csv
import math

def test_notebook_exists():
    path = "/home/user/quarterly_report.ipynb"
    assert os.path.exists(path), f"Notebook file {path} is missing."
    assert os.path.isfile(path), f"Path {path} is not a file."

def test_db_exists_and_valid():
    db_path = "/home/user/sales.db"
    assert os.path.exists(db_path), f"SQLite database {db_path} is missing."

    # Try connecting and querying to ensure it's valid
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sales';")
        table = cursor.fetchone()
        assert table is not None, "Table 'sales' does not exist in the database."

        cursor.execute("SELECT COUNT(*) FROM sales;")
        count = cursor.fetchone()[0]
        assert count > 0, "Table 'sales' is empty."
    except sqlite3.Error as e:
        assert False, f"Failed to connect or query SQLite database: {e}"
    finally:
        conn.close()

def test_report_exists_and_correct():
    report_path = "/home/user/revenue_report.csv"
    assert os.path.exists(report_path), f"Report CSV {report_path} is missing."

    expected_data = {
        "East": 300.0,
        "North": 250.75,
        "South": 250.0
    }

    with open(report_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        assert fieldnames is not None, "CSV file is empty or missing headers."
        assert "region" in fieldnames, "CSV missing 'region' column."
        assert "total_revenue" in fieldnames, "CSV missing 'total_revenue' column."

        rows = list(reader)
        assert len(rows) == len(expected_data), f"Expected {len(expected_data)} rows in report, found {len(rows)}."

        for row in rows:
            region = row["region"]
            assert region in expected_data, f"Unexpected region '{region}' in report."

            try:
                revenue = float(row["total_revenue"])
            except ValueError:
                assert False, f"Invalid total_revenue value '{row['total_revenue']}' for region '{region}'."

            expected_revenue = expected_data[region]
            assert math.isclose(revenue, expected_revenue, rel_tol=1e-5), \
                f"Expected revenue {expected_revenue} for region {region}, but got {revenue}."

def test_plot_exists():
    plot_path = "/home/user/revenue_plot.png"
    assert os.path.exists(plot_path), f"Plot PNG {plot_path} is missing."
    assert os.path.isfile(plot_path), f"Path {plot_path} is not a file."
    assert os.path.getsize(plot_path) > 0, f"Plot PNG {plot_path} is empty."