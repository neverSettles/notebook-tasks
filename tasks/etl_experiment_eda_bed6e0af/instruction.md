You are a Data Engineer building an ETL pipeline to validate and analyze agricultural experiment data. We have two raw CSV files: `/home/user/plot_metadata.csv` and `/home/user/yield_data.csv`. 

Create a Jupyter notebook at `/home/user/etl_experiment_eda.ipynb` to perform systematic Exploratory Data Analysis (EDA) and data cleaning.

Your notebook must accomplish the following steps in order:
1. Load both CSV files and merge them on `plot_id` using an inner join.
2. Clean the merged dataset by dropping rows with environmental anomalies. Specifically, remove any rows where `daily_temp` is greater than 50 or `daily_rainfall` is less than 0.
3. Compute summary statistics grouped by `fertilizer`. Calculate the mean of `yield_kg` and `daily_temp` for each fertilizer type. Save these exact results as a JSON file at `/home/user/summary_stats.json`. The JSON should be a dictionary where keys are the fertilizer names (e.g., "None", "F_A") and values are dictionaries with keys `"yield_kg"` and `"daily_temp"` containing the mean values as floats.
4. Generate a scatter plot with `daily_temp` on the x-axis and `yield_kg` on the y-axis. Save this plot as `/home/user/temp_vs_yield.png`.
5. Save the cleaned, merged dataset to `/home/user/clean_experiment_data.csv` (include headers, do not include the index).
6. **Validation Cells:** At the end of your notebook, add Python `assert` statements to validate the pipeline's correctness. Specifically, load `/home/user/clean_experiment_data.csv` and assert that:
   - The dataframe has exactly 8 rows.
   - The maximum `daily_temp` in the cleaned dataset is `<= 50`.
   - The minimum `daily_rainfall` in the cleaned dataset is `>= 0`.

The notebook must execute successfully from top to bottom with `jupyter nbconvert --to notebook --execute /home/user/etl_experiment_eda.ipynb`.