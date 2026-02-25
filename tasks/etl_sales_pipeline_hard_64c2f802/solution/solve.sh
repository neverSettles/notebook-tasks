#!/bin/bash
# Gold solution

cat << 'EOF' > /home/user/create_nb.py
import nbformat as nbf

nb = nbf.v4.new_notebook()

code = """
import pandas as pd
import json

# 1. Extraction & Cleaning
df = pd.read_csv('/home/user/raw_sales.csv')
with open('/home/user/store_regions.json', 'r') as f:
    regions = json.load(f)

# Parse txn_date
df['txn_date'] = pd.to_datetime(df['txn_date'], format='mixed', dayfirst=False).dt.normalize()

# Clean revenue
df['revenue'] = df['revenue'].astype(str).str.replace(r'[$,]', '', regex=True).astype(float)

# Impute expenses
df['expenses'] = df.groupby('item_code')['expenses'].transform(lambda x: x.fillna(x.median()))
df['expenses'] = df['expenses'].fillna(0)

# 2. Transformation & Merging
df['profit'] = df['revenue'] - df['expenses']

# Map region_name
df['store_id'] = df['store_id'].astype(str)
df['region_name'] = df['store_id'].map(regions).fillna('Unknown')

# Filter
df = df[df['profit'] >= 0]

# 3. Aggregation & Loading
df.to_csv('/home/user/clean_data.csv', index=False)

# Aggregation for Excel
region_profit = df.groupby('region_name', as_index=False)['profit'].sum()
region_profit = region_profit.rename(columns={'profit': 'total_profit'})
region_profit = region_profit.sort_values('total_profit', ascending=False)

item_profit = df.groupby(['region_name', 'item_code'], as_index=False)['profit'].sum()
item_profit = item_profit.rename(columns={'profit': 'item_profit'})
# Sort by region_name alphabetically, then item_profit descending
item_profit = item_profit.sort_values(['region_name', 'item_profit'], ascending=[True, False])
top_items = item_profit.groupby('region_name').head(2)

with pd.ExcelWriter('/home/user/regional_summary.xlsx') as writer:
    region_profit.to_excel(writer, sheet_name='Region_Profit', index=False)
    top_items.to_excel(writer, sheet_name='Top_Items', index=False)
"""

nb.cells.append(nbf.v4.new_code_cell(code))

with open('/home/user/etl_pipeline.ipynb', 'w') as f:
    nbf.write(nb, f)
EOF
python3 /home/user/create_nb.py && jupyter nbconvert --to notebook --execute /home/user/etl_pipeline.ipynb
cat << 'EOF' > /home/user/create_nb.py
import nbformat as nbf

nb = nbf.v4.new_notebook()

code = """
import pandas as pd
import json

# 1. Extraction & Cleaning
df = pd.read_csv('/home/user/raw_sales.csv')
with open('/home/user/store_regions.json', 'r') as f:
    regions = json.load(f)

# Parse txn_date
df['txn_date'] = pd.to_datetime(df['txn_date']).dt.normalize()

# Clean revenue
df['revenue'] = df['revenue'].astype(str).str.replace(r'[$,]', '', regex=True).astype(float)

# Impute expenses
df['expenses'] = df.groupby('item_code')['expenses'].transform(lambda x: x.fillna(x.median()))
df['expenses'] = df['expenses'].fillna(0)

# 2. Transformation & Merging
df['profit'] = df['revenue'] - df['expenses']

# Map region_name
df['store_id'] = df['store_id'].astype(str)
df['region_name'] = df['store_id'].map(regions).fillna('Unknown')

# Filter
df = df[df['profit'] >= 0]

# 3. Aggregation & Loading
df.to_csv('/home/user/clean_data.csv', index=False)

# Aggregation for Excel
region_profit = df.groupby('region_name', as_index=False)['profit'].sum()
region_profit = region_profit.rename(columns={'profit': 'total_profit'})
region_profit = region_profit.sort_values('total_profit', ascending=False)

item_profit = df.groupby(['region_name', 'item_code'], as_index=False)['profit'].sum()
item_profit = item_profit.rename(columns={'profit': 'item_profit'})
# Sort by region_name alphabetically, then item_profit descending
item_profit = item_profit.sort_values(['region_name', 'item_profit'], ascending=[True, False])
top_items = item_profit.groupby('region_name').head(2)

with pd.ExcelWriter('/home/user/regional_summary.xlsx') as writer:
    region_profit.to_excel(writer, sheet_name='Region_Profit', index=False)
    top_items.to_excel(writer, sheet_name='Top_Items', index=False)
"""

nb.cells.append(nbf.v4.new_code_cell(code))

with open('/home/user/etl_pipeline.ipynb', 'w') as f:
    nbf.write(nb, f)
EOF
python3 /home/user/create_nb.py && jupyter nbconvert --to notebook --execute /home/user/etl_pipeline.ipynb
python3 -c "import pandas as pd; df = pd.read_csv('/home/user/raw_sales.csv'); print(df['txn_date'].head(10)); print(df['txn_date'].tail(10))"
head -n 5 /home/user/raw_sales.csv
sed -i -E 's/\$([0-9]+),([0-9]+)/\$\1\2/g' /home/user/raw_sales.csv && head -n 5 /home/user/raw_sales.csv
grep -E '\$[0-9]+,' /home/user/raw_sales.csv
cat << 'EOF' > /home/user/create_nb.py
import nbformat as nbf

nb = nbf.v4.new_notebook()

code = """
import pandas as pd
import json

# 1. Extraction & Cleaning
df = pd.read_csv('/home/user/raw_sales.csv')
with open('/home/user/store_regions.json', 'r') as f:
    regions = json.load(f)

# Parse txn_date
df['txn_date'] = pd.to_datetime(df['txn_date'], format='mixed', dayfirst=False).dt.normalize()

# Clean revenue
df['revenue'] = df['revenue'].astype(str).str.replace(r'[$,]', '', regex=True).astype(float)

# Impute expenses
df['expenses'] = df.groupby('item_code')['expenses'].transform(lambda x: x.fillna(x.median()))
df['expenses'] = df['expenses'].fillna(0)

# 2. Transformation & Merging
df['profit'] = df['revenue'] - df['expenses']

# Map region_name
df['store_id'] = df['store_id'].astype(str)
df['region_name'] = df['store_id'].map(regions).fillna('Unknown')

# Filter
df = df[df['profit'] >= 0]

# 3. Aggregation & Loading
df.to_csv('/home/user/clean_data.csv', index=False)

# Aggregation for Excel
region_profit = df.groupby('region_name', as_index=False)['profit'].sum()
region_profit = region_profit.rename(columns={'profit': 'total_profit'})
region_profit = region_profit.sort_values('total_profit', ascending=False)

item_profit = df.groupby(['region_name', 'item_code'], as_index=False)['profit'].sum()
item_profit = item_profit.rename(columns={'profit': 'item_profit'})
# Sort by region_name alphabetically, then item_profit descending
item_profit = item_profit.sort_values(['region_name', 'item_profit'], ascending=[True, False])
top_items = item_profit.groupby('region_name').head(2)

with pd.ExcelWriter('/home/user/regional_summary.xlsx') as writer:
    region_profit.to_excel(writer, sheet_name='Region_Profit', index=False)
    top_items.to_excel(writer, sheet_name='Top_Items', index=False)
"""

nb.cells.append(nbf.v4.new_code_cell(code))

with open('/home/user/etl_pipeline.ipynb', 'w') as f:
    nbf.write(nb, f)
EOF
python3 /home/user/create_nb.py && jupyter nbconvert --to notebook --execute /home/user/etl_pipeline.ipynb