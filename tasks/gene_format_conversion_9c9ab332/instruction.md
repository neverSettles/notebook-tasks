You are acting as a bioinformatics assistant. We have a raw gene expression dataset in CSV format, but our pipelines require the data in JSON and Excel formats, and the dataset needs basic cleaning.

Write a Jupyter Notebook at `/home/user/gene_format_converter.ipynb` that performs the following steps in separate, well-documented cells:

1. **Load Data**: Read the dataset from `/home/user/raw_genes.csv`.
2. **Standardize Column Names**: Convert all column names to lowercase, replace spaces and hyphens with underscores. Specifically, the columns `Gene ID`, `Expression Level`, and `P-Value` should become `gene_id`, `expression_level`, and `p_value`.
3. **Filter Data**: Remove any rows where `expression_level` is strictly less than 10.0.
4. **Format Conversion & Export**: Save the cleaned and filtered DataFrame to two different formats:
   - A JSON file at `/home/user/clean_genes.json` (use `orient='records'`).
   - An Excel file at `/home/user/clean_genes.xlsx` (use `index=False`).

Make sure the notebook runs without errors using `jupyter nbconvert --to notebook --execute /home/user/gene_format_converter.ipynb`.