# test_final_state.py
import os
import json
import csv

def test_notebook_exists_and_valid():
    """
    Validates that the Jupyter notebook exists, is valid JSON, 
    and contains exactly 3 code cells.
    """
    nb_path = '/home/user/finance_analysis.ipynb'
    assert os.path.exists(nb_path), f"Notebook {nb_path} not found."

    try:
        with open(nb_path, 'r') as f:
            nb = json.load(f)
    except json.JSONDecodeError:
        assert False, f"Notebook {nb_path} is not a valid JSON file."

    code_cells = [c for c in nb.get('cells', []) if c.get('cell_type') == 'code']
    assert len(code_cells) == 3, f"Expected exactly 3 code cells, found {len(code_cells)}."

def test_output_csv_correct():
    """
    Validates that avg_prices.csv exists and contains the correct average prices.
    """
    csv_path = '/home/user/avg_prices.csv'
    assert os.path.exists(csv_path), f"Output file {csv_path} not found. Did you execute the notebook?"

    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            assert False, "Output CSV is empty."

        assert header == ['Ticker', 'Price'], f"Unexpected columns in avg_prices.csv: {header}"

        expected_prices = {'AAPL': 153.2, 'GOOG': 93.2, 'MSFT': 243.6}
        actual_prices = {}

        for row in reader:
            if len(row) == 2:
                try:
                    actual_prices[row[0]] = float(row[1])
                except ValueError:
                    assert False, f"Could not parse price to float in row: {row}"

        for ticker, expected_price in expected_prices.items():
            assert ticker in actual_prices, f"Ticker {ticker} missing from output."
            actual = actual_prices[ticker]
            assert abs(actual - expected_price) < 1e-4, \
                f"Incorrect price for {ticker}: {actual} (expected {expected_price})"