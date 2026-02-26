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


**Additional Requirement - Differential Expression Analysis:**
After the basic restructuring:
1. Calculate the log2 fold-change between the maximum and minimum expression values for each gene.
2. Save the top 5 genes by absolute fold-change to `/home/user/top_genes.csv` with columns: `gene_id`, `fold_change`, `max_expression`, `min_expression`.
3. Generate a bar chart of these top 5 genes and save to `/home/user/top_genes_plot.png`.

**IMPORTANT: After creating the notebook, you must run it to generate the output files.** Execute the notebook using:
```bash
jupyter nbconvert --to notebook --execute /home/user/gene_analysis.ipynb
```
The tests check for output files that are only created when the notebook is executed. Creating the notebook alone is not sufficient.
