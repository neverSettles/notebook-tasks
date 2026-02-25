I need you to build a Jupyter notebook that acts as an ETL pipeline to transform some messy sales data. 
Please create a notebook at `/home/user/etl_pipeline.ipynb`.

The raw data is located at `/home/user/raw_sales.csv`. It contains daily sales in a wide format with dates as columns.

The notebook should have distinct cells for each step of the pipeline and output specific checkpoint files so we can audit the transformations.

Here are the requirements:
1. Load the raw data from `/home/user/raw_sales.csv`.
2. **Step 1 (Melt)**: Reshape the data from wide to long format. The identifier variables should be `Store_ID` and `Region`. The variable column should be named `Date` and the value column should be named `Sales`. Fill any missing `Sales` values with 0. Save this intermediate dataframe to `/home/user/checkpoint_1_long.csv` (without the index).
3. **Step 2 (Clean & Aggregate)**: Convert the `Date` column to datetime. Extract the year-month string (format: 'YYYY-MM') into a new column called `Month`. Then, aggregate the total sales by `Store_ID` and `Month`. Save this aggregated dataframe to `/home/user/checkpoint_2_agg.csv` (without the index). The columns should be exactly `Store_ID`, `Month`, and `Total_Sales`.
4. **Step 3 (Pivot)**: Pivot the aggregated data back into a clean wide format for a final report. The index should be `Store_ID`, the columns should be the unique `Month` values, and the values should be the `Total_Sales`. Save this final dataframe to `/home/user/final_report.csv` (keeping the index).

Make sure the notebook runs perfectly from start to finish with `jupyter nbconvert --to notebook --execute /home/user/etl_pipeline.ipynb`.