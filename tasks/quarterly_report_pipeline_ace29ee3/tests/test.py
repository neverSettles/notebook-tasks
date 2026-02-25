# test_final_state.py

import os
import json
import csv
import pytest

def test_notebook_exists():
    assert os.path.exists('/home/user/quarterly_report.ipynb'), "The Jupyter notebook /home/user/quarterly_report.ipynb was not found."

def test_final_report_exists():
    assert os.path.exists('/home/user/final_report.csv'), "The output file /home/user/final_report.csv was not found."

def test_final_report_content():
    report_path = '/home/user/final_report.csv'

    with open(report_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 5, f"Expected 5 rows in the final report, found {len(rows)}."

    # Sort rows by 'id' to ensure predictable checking
    rows.sort(key=lambda x: int(x['id']))

    # Verify columns
    expected_columns = {'id', 'date', 'feedback', 'agent_id', 'revenue'}
    actual_columns = set(rows[0].keys())
    assert expected_columns.issubset(actual_columns), f"Expected columns {expected_columns}, but found {actual_columns}."

    # Row 1 text cleaning
    assert "Great service by agent! Contact me at [EMAIL]." == rows[0]['feedback'], "Row 1 text cleaning failed (HTML tags, email, or whitespace)."
    assert int(rows[0]['revenue']) == 5000, "Row 1 merge failed (revenue mismatch)."

    # Row 2 text cleaning
    assert "The product is ok. My phone is [PHONE]. <3" == rows[1]['feedback'], "Row 2 text cleaning failed (HTML tags, entities, or phone)."
    assert int(rows[1]['revenue']) == 3000, "Row 2 merge failed (revenue mismatch)."

    # Row 3 text cleaning
    assert "Awful experience. refund requested." == rows[2]['feedback'], "Row 3 text cleaning failed (Nested tags or whitespace)."
    assert int(rows[2]['revenue']) == 5000, "Row 3 merge failed (revenue mismatch)."

    # Row 4 text cleaning
    assert "café was closed. Email: [EMAIL]!" == rows[3]['feedback'], "Row 4 text cleaning failed (Unicode, email, or whitespace)."
    assert int(rows[3]['revenue']) == 1500, "Row 4 merge failed (revenue mismatch)."

    # Row 5 text cleaning
    assert "alert('xss') No comment" == rows[4]['feedback'], "Row 5 text cleaning failed (Script tag content preservation or whitespace)."
    assert int(rows[4]['revenue']) == 3000, "Row 5 merge failed (revenue mismatch)."