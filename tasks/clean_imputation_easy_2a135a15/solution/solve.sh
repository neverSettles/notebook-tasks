#!/bin/bash
# Gold solution

python3 -c "
import nbformat as nbf
nb = nbf.v4.new_notebook()
code = '''import pandas as pd

df = pd.read_csv(\"/home/user/financial_data.csv\")
df[\"Date\"] = pd.to_datetime(df[\"Date\"])
df.set_index(\"Date\", inplace=True)
df[\"Revenue\"] = df[\"Revenue\"].ffill()
df[\"Expenses\"] = df[\"Expenses\"].fillna(df[\"Expenses\"].mean())
df[\"Profit\"] = df[\"Revenue\"] - df[\"Expenses\"]
df.to_csv(\"/home/user/cleaned_financial_data.csv\")'''
nb['cells'] = [nbf.v4.new_code_cell(code)]
nbf.write(nb, '/home/user/clean_imputation.ipynb')
"
jupyter nbconvert --to notebook --execute /home/user/clean_imputation.ipynb
cat /home/user/cleaned_financial_data.csv
cat /home/user/financial_data.csv
python3 -c 'import pandas as pd; df = pd.read_csv("/home/user/financial_data.csv"); print(df)'
sed -i 's/\\n/\n/g' /home/user/financial_data.csv
jupyter nbconvert --to notebook --execute /home/user/clean_imputation.ipynb
cat /home/user/cleaned_financial_data.csv