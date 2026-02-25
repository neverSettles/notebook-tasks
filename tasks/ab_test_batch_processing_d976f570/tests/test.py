# test_final_state.py

import os
import json
import pytest

NOTEBOOK_PATH = "/home/user/ab_test_batch.ipynb"
OUTPUT_JSON_PATH = "/home/user/ab_test_summary.json"

def test_notebook_exists():
    assert os.path.isfile(NOTEBOOK_PATH), f"Notebook file not found at {NOTEBOOK_PATH}"

def test_output_json_exists():
    assert os.path.isfile(OUTPUT_JSON_PATH), f"Output JSON file not found at {OUTPUT_JSON_PATH}"

def test_output_json_contents():
    with open(OUTPUT_JSON_PATH, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            pytest.fail("Output file is not valid JSON")

    # Check structure
    expected_keys = {"control", "treatment", "files_processed", "files_failed"}
    assert set(data.keys()) == expected_keys, f"JSON keys do not match expected structure. Found: {list(data.keys())}"

    assert "impressions" in data["control"], "Missing 'impressions' in control data"
    assert "conversions" in data["control"], "Missing 'conversions' in control data"
    assert "conversion_rate" in data["control"], "Missing 'conversion_rate' in control data"

    assert "impressions" in data["treatment"], "Missing 'impressions' in treatment data"
    assert "conversions" in data["treatment"], "Missing 'conversions' in treatment data"
    assert "conversion_rate" in data["treatment"], "Missing 'conversion_rate' in treatment data"

    # Check values
    assert data["files_processed"] == 2, f"Expected 2 files processed, got {data['files_processed']}"
    assert data["files_failed"] == 1, f"Expected 1 file failed, got {data['files_failed']}"

    # Control
    assert data["control"]["impressions"] == 4, f"Expected 4 control impressions, got {data['control']['impressions']}"
    assert data["control"]["conversions"] == 1, f"Expected 1 control conversion, got {data['control']['conversions']}"
    assert pytest.approx(data["control"]["conversion_rate"], 0.01) == 0.25, f"Expected control conversion rate approx 0.25, got {data['control']['conversion_rate']}"

    # Treatment
    assert data["treatment"]["impressions"] == 4, f"Expected 4 treatment impressions, got {data['treatment']['impressions']}"
    assert data["treatment"]["conversions"] == 3, f"Expected 3 treatment conversions, got {data['treatment']['conversions']}"
    assert pytest.approx(data["treatment"]["conversion_rate"], 0.01) == 0.75, f"Expected treatment conversion rate approx 0.75, got {data['treatment']['conversion_rate']}"