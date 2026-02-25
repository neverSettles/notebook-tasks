#!/bin/bash
# Gold solution

cat /home/user/raw_genes.csv || echo -e "Gene ID,Expression Level,P-Value\nGeneA,15.5,0.01\nGeneB,8.2,0.05\nGene-C,20.1,0.001" > /home/user/raw_genes.csv
cat << 'EOF' > /home/user/create_nb.py
import nbformat as nbf

nb = nbf.v4.new_notebook()

cell1 = """import pandas as pd
# Load Data
df = pd.read_csv('/home/user/raw_genes.csv')
"""

cell2 = """# Standardize Column Names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')
"""

cell3 = """# Filter Data
df = df[df['expression_level'] >= 10.0]
"""

cell4 = """# Format Conversion & Export
df.to_json('/home/user/clean_genes.json', orient='records')
df.to_excel('/home/user/clean_genes.xlsx', index=False)
"""

nb['cells'] = [
    nbf.v4.new_code_cell(cell1),
    nbf.v4.new_code_cell(cell2),
    nbf.v4.new_code_cell(cell3),
    nbf.v4.new_code_cell(cell4)
]

with open('/home/user/gene_format_converter.ipynb', 'w') as f:
    nbf.write(nb, f)
EOF
python3 /home/user/create_nb.py
jupyter nbconvert --to notebook --execute /home/user/gene_format_converter.ipynb
ls -l /home/user/clean_genes*
cat /home/user/raw_genes.csv
cat /home/user/clean_genes.json
sed -i 's/\\n /\n/g' /home/user/raw_genes.csv
cat /home/user/raw_genes.csv
jupyter nbconvert --to notebook --execute /home/user/gene_format_converter.ipynb
cat /home/user/clean_genes.json