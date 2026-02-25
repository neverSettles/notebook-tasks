# test_final_state.py
import os
import json
import csv
import math

def test_notebook_exists():
    """Verify that the jupyter notebook was created."""
    path = "/home/user/dashboard.ipynb"
    assert os.path.isfile(path), f"Notebook file is missing: {path}"

def test_dashboard_png_exists():
    """Verify that the dashboard plot was created and is not empty."""
    path = "/home/user/dashboard.png"
    assert os.path.isfile(path), f"Plot image is missing: {path}"
    assert os.path.getsize(path) > 0, f"Plot image is empty: {path}"

def test_metrics_json():
    """Verify the metrics.json file contains correct aggregated data."""
    path = "/home/user/metrics.json"
    assert os.path.isfile(path), f"Metrics JSON file is missing: {path}"

    with open(path, 'r', encoding='utf-8') as f:
        try:
            metrics = json.load(f)
        except json.JSONDecodeError:
            assert False, f"Failed to parse JSON from {path}"

    assert "Total_USD_Revenue" in metrics, "Missing 'Total_USD_Revenue' key in metrics.json"
    assert "Top_Product" in metrics, "Missing 'Top_Product' key in metrics.json"

    expected_revenue = 4330.41
    actual_revenue = float(metrics["Total_USD_Revenue"])
    assert abs(actual_revenue - expected_revenue) < 1.0, \
        f"Expected Total_USD_Revenue ~{expected_revenue}, but got {actual_revenue}"

    expected_top_product = "A"
    actual_top_product = str(metrics["Top_Product"]).strip()
    assert actual_top_product == expected_top_product, \
        f"Expected Top_Product '{expected_top_product}', but got '{actual_top_product}'"

def test_daily_sales_csv():
    """Verify the daily_sales.csv file structure and values."""
    path = "/home/user/daily_sales.csv"
    assert os.path.isfile(path), f"Daily sales CSV is missing: {path}"

    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        assert fieldnames is not None, "daily_sales.csv is empty or has no header"

        expected_columns = ['Date', 'Daily_Revenue', 'Rolling_7d_Revenue']
        assert list(fieldnames) == expected_columns, \
            f"Expected columns {expected_columns}, but got {fieldnames}"

        rows = list(reader)

    assert len(rows) == 4, f"Expected 4 valid daily sales rows, but got {len(rows)}"

    # Check that dates are sorted chronologically
    dates = [row['Date'] for row in rows]
    sorted_dates = sorted(dates)
    assert dates == sorted_dates, "The 'Date' column is not sorted chronologically"

    # Check the last row's rolling average
    last_row = rows[-1]
    try:
        last_rolling = float(last_row['Rolling_7d_Revenue'])
    except ValueError:
        assert False, f"Invalid float value for Rolling_7d_Revenue in the last row: {last_row['Rolling_7d_Revenue']}"

    expected_last_rolling = 1082.60
    assert abs(last_rolling - expected_last_rolling) < 1.0, \
        f"Expected final Rolling_7d_Revenue ~{expected_last_rolling}, but got {last_rolling}"