# test_final_state.py
import os
import csv
import pytest

def test_notebook_exists():
    nb_path = '/home/user/etl_merge.ipynb'
    assert os.path.isfile(nb_path), f"The Jupyter notebook {nb_path} was not created."

def test_merged_customers_csv():
    csv_path = '/home/user/merged_customers.csv'
    assert os.path.isfile(csv_path), f"The output file {csv_path} was not created."

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames is not None, "The CSV file is empty or missing headers."

        # Verify headers
        expected_headers = ['customer_id', 'name', 'email', 'phone', 'total_spent']
        assert list(reader.fieldnames) == expected_headers, \
            f"CSV headers are incorrect. Expected {expected_headers}, got {reader.fieldnames}"

        rows = list(reader)

    assert len(rows) == 5, f"Expected 5 rows in the merged data (excluding header), found {len(rows)}"

    # Sort by customer_id to ensure order doesn't fail the test
    rows.sort(key=lambda x: int(x['customer_id']))

    # Expected rows definition
    expected = [
        {"customer_id": "1", "name": "Alice", "email": "alice@crm.com", "phone": "555-0101", "total_spent": 150.5},
        {"customer_id": "2", "name": "Bob", "email": "bob@crm.com", "phone": "555-0102", "total_spent": 200.0},
        {"customer_id": "3", "name": "Charlie", "email": "charlie_new@ecom.com", "phone": "555-0888", "total_spent": 350.75},
        {"customer_id": "4", "name": "David", "email": "david@crm.com", "phone": "555-0104", "total_spent": 0.0},
        {"customer_id": "5", "name": "Unknown", "email": "eve@ecom.com", "phone": "555-0105", "total_spent": 99.99}
    ]

    for i, exp in enumerate(expected):
        act = rows[i]
        cid = exp['customer_id']
        assert act['customer_id'] == cid, f"Expected customer_id {cid}, got {act['customer_id']}"
        assert act['name'] == exp['name'], f"Name for customer {cid} is incorrect. Expected {exp['name']}, got {act['name']}"
        assert act['email'] == exp['email'], f"Email for customer {cid} is incorrect. Expected {exp['email']}, got {act['email']}"
        assert act['phone'] == exp['phone'], f"Phone for customer {cid} is incorrect. Expected {exp['phone']}, got {act['phone']}"

        try:
            act_spent = float(act['total_spent'])
        except ValueError:
            pytest.fail(f"total_spent for customer {cid} could not be parsed as a float: {act['total_spent']}")

        assert act_spent == pytest.approx(exp['total_spent']), \
            f"Total spent for customer {cid} is incorrect. Expected {exp['total_spent']}, got {act_spent}"