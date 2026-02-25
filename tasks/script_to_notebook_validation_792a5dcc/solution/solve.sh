#!/bin/bash
# Gold oracle solution

cat << 'EOF' > create_notebook.py
import nbformat as nbf

nb = nbf.v4.new_notebook()

nb['cells'] = [
    nbf.v4.new_markdown_cell('# Sales Analysis Production'),
    nbf.v4.new_markdown_cell('## Data Generation\nGenerates random sales data for 100 items.'),
    nbf.v4.new_code_cell('''import pandas as pd
import numpy as np

np.random.seed(42)
categories = ['Electronics', 'Clothing', 'Home']
data = {
    'item_id': range(1, 101),
    'category': np.random.choice(categories, 100),
    'price': np.random.uniform(10, 100, 100),
    'discount': np.random.uniform(0, 0.3, 100)
}
df = pd.DataFrame(data)'''),
    nbf.v4.new_code_cell('''df['discounted_price'] = df['price'] * (1 - df['discount'])
summary = df.groupby('category')['discounted_price'].sum().reset_index()'''),
    nbf.v4.new_markdown_cell('## Validation\nCheck data consistency and validity using assertions.'),
    nbf.v4.new_code_cell('''assert len(df) == 100, "Row count is not 100"
assert df['discounted_price'].min() >= 0, "Found negative discounted price"
assert np.isclose(summary['discounted_price'].sum(), df['discounted_price'].sum()), "Total discounted sums do not match"'''),
    nbf.v4.new_code_cell('''summary.to_csv('/home/user/final_sales_summary.csv', index=False)''')
]

with open('/home/user/production_sales_analysis.ipynb', 'w') as f:
    nbf.write(nb, f)
EOF
python3 create_notebook.py && jupyter nbconvert --to notebook --execute --inplace /home/user/production_sales_analysis.ipynb
