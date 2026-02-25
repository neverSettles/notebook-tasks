#!/bin/bash
# Gold solution

cat /home/user/messy_ab_test.py
cat /home/user/messy_ab_test.py
cat /home/user/campaign_data.csv
cat << 'EOF' > /home/user/generate_nb.py
import nbformat as nbf

nb = nbf.v4.new_notebook()

cells = []

# Cell 1: Import libraries
cells.append(nbf.v4.new_markdown_cell("## 1. Import Libraries\nIn this section, we import the necessary libraries for data manipulation, statistical testing, and visualization."))
cells.append(nbf.v4.new_code_cell("import pandas as pd\nimport numpy as np\nfrom scipy.stats import chi2_contingency\nimport matplotlib.pyplot as plt"))

# Cell 2: Data Loading
cells.append(nbf.v4.new_markdown_cell("## 2. Data Loading\nHere we load the A/B test campaign data from a CSV file."))
cells.append(nbf.v4.new_code_cell("df = pd.read_csv('campaign_data.csv')\ndf.head()"))

# Cell 3: Data Preprocessing & Summary
cells.append(nbf.v4.new_markdown_cell("## 3. Data Preprocessing & Summary\nWe calculate the total visitors, total conversions, and conversion rates for each group."))
cells.append(nbf.v4.new_code_cell("""summary = df.groupby('group').agg(
    Total_Visitors=('user_id', 'count'),
    Converted=('converted', 'sum')
).reset_index()
summary['Conversion_Rate'] = summary['Converted'] / summary['Total_Visitors']
summary"""))

# Cell 4: Statistical Testing
cells.append(nbf.v4.new_markdown_cell("## 4. Statistical Testing\nWe perform a chi-square test to determine if the difference in conversion rates is statistically significant."))
cells.append(nbf.v4.new_code_cell("""contingency_table = pd.crosstab(df['group'], df['converted'])
chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}")"""))

# Cell 5: Visualization
cells.append(nbf.v4.new_markdown_cell("## 5. Visualization\nWe create a bar chart of the conversion rates for the control and treatment groups and save it as an image."))
cells.append(nbf.v4.new_code_cell("""plt.bar(summary['group'], summary['Conversion_Rate'], color=['blue', 'orange'])
plt.title('Conversion Rate by Group')
plt.xlabel('Group')
plt.ylabel('Conversion Rate')
plt.savefig('/home/user/conversion_plot.png')
plt.show()"""))

# Cell 6: Export Results
cells.append(nbf.v4.new_markdown_cell("## 6. Export Results\nFinally, we export the grouped summary statistics to a CSV file."))
cells.append(nbf.v4.new_code_cell("""summary.to_csv('/home/user/summary_stats.csv', index=False)"""))

nb['cells'] = cells

with open('/home/user/ab_test_analysis.ipynb', 'w') as f:
    nbf.write(nb, f)

EOF
python3 /home/user/generate_nb.py
jupyter nbconvert --to notebook --execute /home/user/ab_test_analysis.ipynb --output /home/user/ab_test_analysis.ipynb
ls -l /home/user/
cat /home/user/summary_stats.csv