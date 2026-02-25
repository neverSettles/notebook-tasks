#!/bin/bash
# Gold solution

cat << 'EOF' > /home/user/create_nb.py
import nbformat as nbf

nb = nbf.v4.new_notebook()

code_1 = """import pandas as pd
df_csv = pd.read_csv('/home/user/store_data.csv')
df_json = pd.read_json('/home/user/region_data.json')
df_excel = pd.read_excel('/home/user/product_data.xlsx')"""

code_2 = """merged = df_csv.merge(df_json, on='store_id', how='inner').merge(df_excel, on='store_id', how='inner')"""

code_3 = """cleaned = merged.sort_values(by='store_id', ascending=True)"""

code_4 = """cleaned.to_csv('/home/user/ml_training_data.csv', index=False)"""

nb.cells = [
    nbf.v4.new_code_cell(code_1),
    nbf.v4.new_code_cell(code_2),
    nbf.v4.new_code_cell(code_3),
    nbf.v4.new_code_cell(code_4)
]

with open('/home/user/clean_pipeline.ipynb', 'w') as f:
    nbf.write(nb, f)
EOF
python3 /home/user/create_nb.py
jupyter nbconvert --to notebook --execute /home/user/clean_pipeline.ipynb
cat /home/user/ml_training_data.csv
cat /home/user/store_data.csv /home/user/region_data.json
head -n 5 /home/user/store_data.csv
python3 -c "print(open('/home/user/store_data.csv').read())"
python3 -c "import pandas as pd; df = pd.read_csv('/home/user/store_data.csv'); print(df.columns); print(df)"
sed -i 's/\\n /\n/g' /home/user/store_data.csv && python3 -c "import pandas as pd; df = pd.read_csv('/home/user/store_data.csv'); print(df)"
jupyter nbconvert --to notebook --execute /home/user/clean_pipeline.ipynb
cat /home/user/ml_training_data.csv