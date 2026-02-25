# test_final_state.py
import os
import csv
import zipfile
import xml.etree.ElementTree as ET
import pytest

def test_etl_pipeline_notebook_exists():
    assert os.path.isfile("/home/user/etl_pipeline.ipynb"), "Notebook file /home/user/etl_pipeline.ipynb is missing."

def test_clean_data_csv():
    clean_csv_path = "/home/user/clean_data.csv"
    assert os.path.isfile(clean_csv_path), f"Output file missing: {clean_csv_path}"

    with open(clean_csv_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) > 0, "clean_data.csv is empty"

    expected_cols = {'txn_date', 'store_id', 'item_code', 'revenue', 'expenses', 'profit', 'region_name'}
    actual_cols = set(reader.fieldnames)
    assert expected_cols.issubset(actual_cols), f"clean_data.csv is missing columns. Expected {expected_cols}, got {actual_cols}"

    for row in rows:
        profit = float(row['profit'])
        assert profit >= 0, f"Found negative profit in clean_data.csv: {profit} for store {row['store_id']}"

        # Check date format (YYYY-MM-DD)
        txn_date = row['txn_date']
        assert len(txn_date) == 10 and txn_date[4] == '-' and txn_date[7] == '-', \
            f"Invalid date format in clean_data.csv: {txn_date}. Expected YYYY-MM-DD"

        # Check some specific derivations
        if row['store_id'] == 'S2' and row['item_code'] == 'B':
            assert abs(float(row['revenue']) - 500.0) < 0.01
            assert abs(float(row['expenses']) - 250.0) < 0.01, "Median imputation for item B failed"
            assert abs(float(row['profit']) - 250.0) < 0.01
            assert row['region_name'] == 'South'

        if row['store_id'] == 'S5':
            assert row['region_name'] == 'Unknown', "store_id S5 should be mapped to Unknown region"

    # Ensure S3, A transaction (profit -100) is filtered out
    s3_a = [r for r in rows if r['store_id'] == 'S3' and r['item_code'] == 'A']
    assert len(s3_a) == 0, "Negative profit row (S3, A) was not filtered out."

def test_regional_summary_xlsx():
    excel_path = "/home/user/regional_summary.xlsx"
    assert os.path.isfile(excel_path), f"Output file missing: {excel_path}"
    assert os.path.getsize(excel_path) > 0, f"{excel_path} is empty"

    try:
        with zipfile.ZipFile(excel_path, 'r') as z:
            # Check for valid Excel sheets
            workbook_xml = z.read('xl/workbook.xml')
            root = ET.fromstring(workbook_xml)
            # Find all sheet names ignoring namespace prefixes
            sheet_names = [elem.attrib['name'] for elem in root.iter() if 'name' in elem.attrib and elem.tag.endswith('sheet')]

            assert "Region_Profit" in sheet_names, "Sheet 'Region_Profit' is missing from regional_summary.xlsx"
            assert "Top_Items" in sheet_names, "Sheet 'Top_Items' is missing from regional_summary.xlsx"

            # Read sharedStrings to check if expected data is present
            if 'xl/sharedStrings.xml' in z.namelist():
                shared_strings = z.read('xl/sharedStrings.xml').decode('utf-8')
                expected_strings = ["North", "South", "East", "West", "Unknown"]
                for es in expected_strings:
                    assert es in shared_strings, f"Expected region '{es}' not found in Excel shared strings."
    except zipfile.BadZipFile:
        pytest.fail(f"{excel_path} is not a valid Excel/zip file.")