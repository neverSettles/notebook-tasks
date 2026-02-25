#!/bin/bash
# Gold solution

cat /home/user/process_finance.py
cat << 'EOF' > /home/user/create_nb.py
import nbformat as nbf

nb = nbf.v4.new_notebook()

cell1 = nbf.v4.new_code_cell("""import pandas as pd
df = pd.read_csv('/home/user/stocks.csv')""")

cell2 = nbf.v4.new_code_cell("""melted = df.melt(id_vars=['Date'], var_name='Ticker', value_name='Price')""")

cell3 = nbf.v4.new_code_cell("""avg_prices = melted.groupby('Ticker')['Price'].mean().reset_index()
avg_prices.to_csv('/home/user/avg_prices.csv', index=False)""")

nb['cells'] = [cell1, cell2, cell3]

with open('/home/user/finance_analysis.ipynb', 'w') as f:
    nbf.write(nb, f)
EOF
python3 /home/user/create_nb.py
jupyter nbconvert --to notebook --execute --inplace /home/user/finance_analysis.ipynb
cat /home/user/avg_prices.csv
cat stocks.csv
pwd
python3 process_finance.py
echo -e "Date,AAPL,GOOG,MSFT\n2023-01-01,150.0,90.0,240.0\n2023-01-02,152.0,92.0,242.0\n2023-01-03,151.0,91.0,241.0\n2023-01-04,155.0,95.0,245.0\n2023-01-05,158.0,98.0,250.0" > /home/user/stocks.csv
jupyter nbconvert --to notebook --execute --inplace /home/user/finance_analysis.ipynb
python3 -c "import pandas as pd; df = pd.read_csv('/home/user/stocks.csv'); print(df.columns)"
printf "Date,AAPL,GOOG,MSFT\n2023-01-01,150.0,90.0,240.0\n2023-01-02,152.0,92.0,242.0\n2023-01-03,151.0,91.0,241.0\n2023-01-04,155.0,95.0,245.0\n2023-01-05,158.0,98.0,250.0\n" > /home/user/stocks.csv
jupyter nbconvert --to notebook --execute --inplace /home/user/finance_analysis.ipynb
cat /home/user/avg_prices.csv