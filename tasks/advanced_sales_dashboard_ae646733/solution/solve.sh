#!/bin/bash
# Gold solution

cat << 'EOF' > create_nb.py
import nbformat as nbf

nb = nbf.v4.new_notebook()

code = """
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt

# 1. Load data
sales = pd.read_csv('/home/user/sales_data.csv')
rates = pd.read_csv('/home/user/exchange_rates.csv')

# Parse Date
sales['Date'] = pd.to_datetime(sales['Date'], format='mixed').dt.strftime('%Y-%m-%d')
rates['Date'] = pd.to_datetime(rates['Date'], format='mixed').dt.strftime('%Y-%m-%d')

# Clean sales
sales = sales.dropna(subset=['Quantity', 'UnitPrice'])
sales = sales[(sales['Quantity'] > 0) & (sales['UnitPrice'] > 0)]

# 2. Currency Conversion
# Create a complete date range for rates
sales['Date'] = pd.to_datetime(sales['Date'])
rates['Date'] = pd.to_datetime(rates['Date'])

min_date = min(sales['Date'].min(), rates['Date'].min())
max_date = max(sales['Date'].max(), rates['Date'].max())
all_dates = pd.date_range(min_date, max_date)

currencies = sales['Currency'].unique()
full_rates = pd.MultiIndex.from_product([all_dates, currencies], names=['Date', 'Currency']).to_frame(index=False)
full_rates = full_rates.merge(rates, on=['Date', 'Currency'], how='left')

# Sort by Date before ffill/bfill
full_rates = full_rates.sort_values('Date')
full_rates['Rate_to_USD'] = full_rates.groupby('Currency')['Rate_to_USD'].transform(lambda x: x.ffill().bfill())

sales = sales.merge(full_rates, on=['Date', 'Currency'], how='left')

sales['USD_Revenue'] = sales['Quantity'] * sales['UnitPrice'] / sales['Rate_to_USD']

# 3. Aggregation
daily = sales.groupby('Date')['USD_Revenue'].sum().reset_index()
daily = daily.rename(columns={'USD_Revenue': 'Daily_Revenue'})
daily = daily.sort_values('Date')
daily['Rolling_7d_Revenue'] = daily['Daily_Revenue'].rolling(window=7, min_periods=1).mean()

# 4. Outputs
daily['Date'] = daily['Date'].dt.strftime('%Y-%m-%d')
daily['Daily_Revenue'] = daily['Daily_Revenue'].round(2)
daily['Rolling_7d_Revenue'] = daily['Rolling_7d_Revenue'].round(2)
daily.to_csv('/home/user/daily_sales.csv', index=False)

total_revenue = round(sales['USD_Revenue'].sum(), 2)
top_product = sales.groupby('Product')['USD_Revenue'].sum().idxmax()

with open('/home/user/metrics.json', 'w') as f:
    json.dump({"Total_USD_Revenue": total_revenue, "Top_Product": top_product}, f)

plt.figure(figsize=(10, 6))
plt.plot(pd.to_datetime(daily['Date']), daily['Rolling_7d_Revenue'])
plt.title('Rolling 7-day USD Revenue')
plt.xlabel('Date')
plt.ylabel('Revenue (USD)')
plt.savefig('/home/user/dashboard.png')
"""

nb.cells.append(nbf.v4.new_code_cell(code))

with open('/home/user/dashboard.ipynb', 'w') as f:
    nbf.write(nb, f)
EOF
python3 create_nb.py
jupyter nbconvert --to notebook --execute /home/user/dashboard.ipynb --inplace
ls -l /home/user/daily_sales.csv /home/user/metrics.json /home/user/dashboard.png