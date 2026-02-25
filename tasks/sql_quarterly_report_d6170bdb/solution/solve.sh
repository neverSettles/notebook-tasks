#!/bin/bash
# Gold solution

cat /home/user/raw_sales.csv | head -n 5
cat << 'EOF' > /home/user/make_nb.py
import nbformat as nbf

nb = nbf.v4.new_notebook()

code = """import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv('/home/user/raw_sales.csv')

# 2. Database Setup
conn = sqlite3.connect('/home/user/sales.db')
df.to_sql('sales', conn, if_exists='replace', index=False)

# 3. SQL Reporting
query = '''
SELECT region, SUM(revenue) as total_revenue
FROM sales
GROUP BY region
ORDER BY region ASC
'''
report_df = pd.read_sql(query, conn)

# 4. Export Data
report_df.to_csv('/home/user/revenue_report.csv', index=False)

# 5. Visualization
plt.figure(figsize=(8, 5))
plt.bar(report_df['region'], report_df['total_revenue'])
plt.title('Total Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Total Revenue')
plt.savefig('/home/user/revenue_plot.png')
"""

nb['cells'] = [nbf.v4.new_code_cell(code)]

with open('/home/user/quarterly_report.ipynb', 'w') as f:
    nbf.write(nb, f)
EOF
python3 /home/user/make_nb.py
jupyter nbconvert --to notebook --execute /home/user/quarterly_report.ipynb
cat -A /home/user/raw_sales.csv | head -n 5
sed -i 's/\\n /\n/g' /home/user/raw_sales.csv
cat -A /home/user/raw_sales.csv | head -n 5
jupyter nbconvert --to notebook --execute /home/user/quarterly_report.ipynb
mv /home/user/quarterly_report.nbconvert.ipynb /home/user/quarterly_report.ipynb