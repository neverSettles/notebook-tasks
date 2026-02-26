You are a Data Engineer building an ETL pipeline. I have a raw dataset located at `/home/user/raw_sales.csv`.

Create a Jupyter Notebook at `/home/user/etl_pipeline.ipynb` that performs the following steps:
1. Import `pandas` and `sqlite3`.
2. Load `/home/user/raw_sales.csv` into a pandas DataFrame.
3. Create an in-memory SQLite database (`sqlite3.connect(':memory:')`) and write the DataFrame to a table named `sales`.
4. Execute a SQL query that calculates the total revenue (sum of `amount`) per `region`, and assigns a rank to each region based on their total revenue (highest revenue = rank 1). Use the `RANK()` window function.
5. Save the result of this query to `/home/user/clean_sales.csv` without the pandas index. 
The output CSV must contain exactly three columns named: `region`, `total_revenue`, and `sales_rank`.

Ensure your notebook executes cleanly from top to bottom. Automated tests will run your notebook using `jupyter nbconvert --to notebook --execute /home/user/etl_pipeline.ipynb` and check the contents of `/home/user/clean_sales.csv`.


**Additional Requirement - Advanced SQL Analysis:**
After the basic ETL pipeline:
1. Add a SQL query that calculates a running total of revenue per region (using `SUM() OVER (PARTITION BY region ORDER BY amount)`).
2. Save the running total results to `/home/user/running_totals.csv` with columns: `region`, `amount`, `running_total`.
3. Generate a bar chart comparing total revenue per region and save to `/home/user/revenue_chart.png`.

**IMPORTANT: After creating the notebook, you must run it to generate the output files.** Execute the notebook using:
```bash
jupyter nbconvert --to notebook --execute /home/user/etl_pipeline.ipynb
```
The tests check for output files that are only created when the notebook is executed. Creating the notebook alone is not sufficient.
