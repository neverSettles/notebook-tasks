# test_final_state.py

import os
import csv
import json
import pytest

def test_notebook_exists_and_valid():
    """Check that the Jupyter notebook exists and is valid JSON with code cells."""
    notebook_path = "/home/user/gene_analysis.ipynb"
    assert os.path.exists(notebook_path), f"The Jupyter notebook {notebook_path} does not exist."
    assert os.path.isfile(notebook_path), f"The path {notebook_path} is not a file."

    with open(notebook_path, "r", encoding="utf-8") as f:
        try:
            nb_data = json.load(f)
        except json.JSONDecodeError:
            pytest.fail("The Jupyter notebook is not a valid JSON file.")

    assert "cells" in nb_data, "The notebook does not contain any cells."

    # Check that there is at least one code cell
    code_cells = [cell for cell in nb_data["cells"] if cell.get("cell_type") == "code"]
    assert len(code_cells) > 0, "The notebook does not contain any code cells."

def test_output_csv_exists_and_correct():
    """Check that the output CSV exists and contains the correct significant genes data."""
    output_csv = "/home/user/significant_genes.csv"
    assert os.path.exists(output_csv), f"Output CSV {output_csv} not found."
    assert os.path.isfile(output_csv), f"The path {output_csv} is not a file."

    with open(output_csv, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            pytest.fail("Output CSV is empty.")

        assert header == ["Gene", "Mean_Expression"], f"Incorrect columns: {header}. Expected ['Gene', 'Mean_Expression']."

        rows = list(reader)
        assert len(rows) == 2, f"Expected 2 rows of data, found {len(rows)}."

        expected_genes = {"gene_C": 90.0, "gene_D": 65.0}
        found_genes = set()

        for row in rows:
            assert len(row) == 2, f"Expected 2 columns in row, found {len(row)}: {row}"
            gene = row[0]
            try:
                mean_val = float(row[1])
            except ValueError:
                pytest.fail(f"Mean_Expression for {gene} is not a valid float: {row[1]}")

            assert gene in expected_genes, f"Unexpected gene found in results: {gene}"

            expected_val = expected_genes[gene]
            assert abs(mean_val - expected_val) <= 1e-5, f"Incorrect mean expression for {gene}: expected {expected_val}, got {mean_val}"

            found_genes.add(gene)

        assert found_genes == set(expected_genes.keys()), f"Missing expected genes. Found {found_genes}, expected {set(expected_genes.keys())}."