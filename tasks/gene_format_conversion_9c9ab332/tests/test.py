# test_final_state.py
import os
import json
import zipfile

def test_notebook_exists():
    path = '/home/user/gene_format_converter.ipynb'
    assert os.path.exists(path), f"Jupyter Notebook {path} was not created."
    assert os.path.getsize(path) > 0, f"Jupyter Notebook {path} is empty."

def test_json_output():
    json_path = '/home/user/clean_genes.json'
    assert os.path.exists(json_path), f"JSON output file {json_path} was not found."

    with open(json_path, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            assert False, f"File {json_path} is not valid JSON."

    assert isinstance(data, list), f"JSON output should be a list of records, got {type(data)}."
    assert len(data) == 3, f"Expected 3 records in JSON after filtering, got {len(data)}."

    expected_genes = {'GENE_2', 'GENE_4', 'GENE_5'}
    found_genes = set()
    for row in data:
        assert 'gene_id' in row, "Column 'gene_id' missing from JSON records."
        assert 'expression_level' in row, "Column 'expression_level' missing from JSON records."
        assert 'p_value' in row, "Column 'p_value' missing from JSON records."
        found_genes.add(row['gene_id'])

        # Verify expression level filtering
        assert float(row['expression_level']) >= 10.0, f"Found record with expression_level < 10.0: {row}"

    assert found_genes == expected_genes, f"Expected gene IDs {expected_genes}, but found {found_genes}."

def test_excel_output():
    excel_path = '/home/user/clean_genes.xlsx'
    assert os.path.exists(excel_path), f"Excel output file {excel_path} was not found."
    assert os.path.getsize(excel_path) > 0, f"Excel file {excel_path} is empty."

    # An Excel (.xlsx) file is a ZIP archive
    assert zipfile.is_zipfile(excel_path), f"File {excel_path} does not appear to be a valid .xlsx (ZIP) file."

    with zipfile.ZipFile(excel_path, 'r') as zf:
        # Check for typical Excel structure files inside the zip
        namelist = zf.namelist()
        assert 'xl/worksheets/sheet1.xml' in namelist or 'xl/workbook.xml' in namelist, \
            f"File {excel_path} does not contain standard Excel workbook structures."


def test_normalized_csv():
    """Verify normalized expression data."""
    import csv
    path = "/home/user/normalized_expression.csv"
    assert os.path.exists(path), f"Normalized CSV missing at {path}"
    with open(path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert len(rows) > 0, "Normalized CSV is empty"
    # Check values are in 0-1 range
    for row in rows:
        for key, val in row.items():
            if key != 'gene_id' and key != 'Gene':
                v = float(val)
                assert 0 <= v <= 1.001, f"Value {v} not in 0-1 range for {key}"

def test_expression_summary():
    import json
    path = "/home/user/expression_summary.json"
    assert os.path.exists(path), f"Summary JSON missing at {path}"
    with open(path) as f:
        data = json.load(f)
    assert "total_genes" in data, "Missing total_genes"
    assert "total_samples" in data, "Missing total_samples"
    assert "mean_expression" in data, "Missing mean_expression"
    assert "highly_expressed_genes" in data, "Missing highly_expressed_genes"
    assert isinstance(data["highly_expressed_genes"], list), "highly_expressed_genes must be a list"

