I am a bioinformatician and I have some messy code for analyzing gene expression data. I need you to create a clean, well-documented Jupyter notebook that performs the analysis steps clearly.

There is a raw dataset located at `/home/user/raw_gene_data.csv`. 

Please create a Jupyter notebook at `/home/user/gene_analysis.ipynb` that does the following:

**Cell 1: Data Loading & Calculation**
- Import pandas.
- Load `/home/user/raw_gene_data.csv`.
- Calculate the mean expression for each gene (all columns except the `sample` column).

**Cell 2: Filtering**
- Filter the calculated means to keep ONLY the genes with a mean expression strictly greater than 50.

**Cell 3: Report Generation**
- Create a DataFrame from the filtered results with exactly two columns: `Gene` and `Mean_Expression`.
- Save this DataFrame to a CSV file at `/home/user/significant_genes.csv` without the index (`index=False`).

The notebook must be executable from start to finish without errors.