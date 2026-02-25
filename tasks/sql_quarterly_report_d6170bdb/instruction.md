You are an AI assistant helping a Business Analyst prepare a quarterly performance report.

Please create a Jupyter notebook at `/home/user/quarterly_report.ipynb` that performs the following steps. Make sure to execute the notebook once you create it (e.g., using `jupyter nbconvert --to notebook --execute /home/user/quarterly_report.ipynb`).

1. **Load Data**: Read the dataset from `/home/user/raw_sales.csv`. 
2. **Database Setup**: Use the `sqlite3` library to create a SQLite database file at `/home/user/sales.db` and load the pandas DataFrame into a table named `sales`.
3. **SQL Reporting**: Write and execute a SQL query using `pandas.read_sql` against the `sales` table to calculate the total revenue grouped by `region`. Order the results alphabetically by `region`.
4. **Export Data**: Save the resulting DataFrame from the query to `/home/user/revenue_report.csv` without the index. The columns must be exactly `region` and `total_revenue`.
5. **Visualization**: Create a simple bar chart of the total revenue by region using matplotlib or seaborn. Save the plot as `/home/user/revenue_plot.png`.

The input file `/home/user/raw_sales.csv` is already provided in the environment.