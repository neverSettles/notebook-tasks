# test_final_state.py

import os
import csv
import json
import pytest

def test_notebook_exists():
    path = "/home/user/etl_experiment_eda.ipynb"
    assert os.path.exists(path), f"Notebook file missing: {path}"
    assert os.path.isfile(path), f"{path} is not a file."

def test_clean_experiment_data():
    path = "/home/user/clean_experiment_data.csv"
    assert os.path.exists(path), f"Cleaned data file missing: {path}"

    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 8, f"Expected exactly 8 rows in cleaned data, but got {len(rows)}"

    try:
        daily_temps = [float(row['daily_temp']) for row in rows]
        daily_rainfalls = [float(row['daily_rainfall']) for row in rows]
    except KeyError as e:
        pytest.fail(f"Missing expected column in cleaned CSV: {e}")
    except ValueError as e:
        pytest.fail(f"Could not parse numeric value in cleaned CSV: {e}")

    max_temp = max(daily_temps)
    assert max_temp <= 50.0, f"Anomalies with temp > 50 were not filtered. Max temp found: {max_temp}"

    min_rainfall = min(daily_rainfalls)
    assert min_rainfall >= 0.0, f"Anomalies with rainfall < 0 were not filtered. Min rainfall found: {min_rainfall}"

def test_summary_stats():
    path = "/home/user/summary_stats.json"
    assert os.path.exists(path), f"Summary statistics JSON missing: {path}"

    with open(path, 'r', encoding='utf-8') as f:
        try:
            stats = json.load(f)
        except json.JSONDecodeError:
            pytest.fail(f"{path} does not contain valid JSON.")

    for key in ["None", "F_A", "F_B"]:
        assert key in stats, f"Missing fertilizer key '{key}' in JSON summary."

    assert abs(stats["None"].get("yield_kg", 0) - 146.0) < 1e-5, f"Incorrect 'None' yield_kg in summary."
    assert abs(stats["None"].get("daily_temp", 0) - 22.0) < 1e-5, f"Incorrect 'None' daily_temp in summary."
    assert abs(stats["F_A"].get("yield_kg", 0) - 182.5) < 1e-5, f"Incorrect 'F_A' yield_kg in summary."
    assert abs(stats["F_B"].get("daily_temp", 0) - 24.4) < 1e-5, f"Incorrect 'F_B' daily_temp in summary."

def test_plot_exists():
    path = "/home/user/temp_vs_yield.png"
    assert os.path.exists(path), f"Plot file missing: {path}"
    assert os.path.isfile(path), f"{path} is not a file."
    assert os.path.getsize(path) > 0, f"{path} is empty."