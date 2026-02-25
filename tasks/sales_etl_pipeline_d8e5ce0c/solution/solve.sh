#!/bin/bash
# Gold solution

cat << 'EOF' > /home/user/create_nb.py
import nbformat as nbf

nb = nbf.v4.new_notebook()

code1 = """import pandas as pd
df = pd.read_csv('/home/user/raw_sales.csv')"""

code2 = """df_long = pd.melt(df, id_vars=['Store_ID', 'Region'], var_name='Date', value_name='Sales')
df_long['Sales'] = df_long['Sales'].fillna(0)
df_long.to_csv('/home/user/checkpoint_1_long.csv', index=False)"""

code3 = """df_long['Date'] = pd.to_datetime(df_long['Date'])
df_long['Month'] = df_long['Date'].dt.strftime('%Y-%m')
df_agg = df_long.groupby(['Store_ID', 'Month'], as_index=False)['Sales'].sum()
df_agg.rename(columns={'Sales': 'Total_Sales'}, inplace=True)
df_agg.to_csv('/home/user/checkpoint_2_agg.csv', index=False)"""

code4 = """df_pivot = df_agg.pivot(index='Store_ID', columns='Month', values='Total_Sales')
df_pivot.to_csv('/home/user/final_report.csv')"""

nb['cells'] = [
    nbf.v4.new_code_cell(code1),
    nbf.v4.new_code_cell(code2),
    nbf.v4.new_code_cell(code3),
    nbf.v4.new_code_cell(code4)
]

with open('/home/user/etl_pipeline.ipynb', 'w') as f:
    nbf.write(nb, f)
EOF
python3 /home/user/create_nb.py
jupyter nbconvert --to notebook --execute /home/user/etl_pipeline.ipynb
pip install jupyter pandas nbformat
python3 /home/user/create_nb.py && jupyter nbconvert --to notebook --execute /home/user/etl_pipeline.ipynb