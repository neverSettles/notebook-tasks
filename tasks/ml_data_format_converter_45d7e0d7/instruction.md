You are an ML Engineer preparing training data for a classification model. The raw data is scattered across different file formats. Your task is to create a clean, well-documented Jupyter notebook at `/home/user/clean_pipeline.ipynb` that batch loads, merges, and converts these files into a single CSV for model training.

The environment contains three raw data files:
1. `/home/user/store_data.csv` (contains `store_id`, `store_type`, `profit_label`)
2. `/home/user/region_data.json` (contains `store_id`, `region`)
3. `/home/user/product_data.xlsx` (contains `store_id`, `top_category`)

Your notebook must do the following in separate, clearly defined cells:
1. **Data Loading:** Load all three files using Pandas.
2. **Data Merging:** Merge the three DataFrames on `store_id` using an inner join.
3. **Data Cleaning:** Sort the merged DataFrame by `store_id` in ascending order.
4. **Export:** Save the final merged DataFrame to `/home/user/ml_training_data.csv` without the index.

The notebook must execute successfully with `jupyter nbconvert --to notebook --execute /home/user/clean_pipeline.ipynb`.