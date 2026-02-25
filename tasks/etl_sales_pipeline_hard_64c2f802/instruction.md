You are a Data Engineer building an ETL pipeline. 

I have two raw data files:
1. `/home/user/raw_sales.csv`: Contains transactional data with columns `txn_date`, `store_id`, `item_code`, `revenue`, and `expenses`. 
   - `revenue` is stored as strings with currency symbols and commas (e.g., `"$1,234.56"`).
   - `expenses` has some missing values (NaN).
   - `txn_date` contains mixed date formats (e.g., `2023-01-15` and `01/15/2023`).
2. `/home/user/store_regions.json`: A JSON file mapping `store_id` (string) to `region_name` (string).

Please create a Jupyter Notebook named `/home/user/etl_pipeline.ipynb` that performs the following multi-step ETL process:

1. **Extraction & Cleaning**:
   - Load the CSV and JSON files.
   - Parse `txn_date` into a standard pandas datetime format (`YYYY-MM-DD`).
   - Clean the `revenue` column, converting it to a numeric float.
   - Impute missing values in `expenses` with the median `expenses` for that specific `item_code`. If an item has no valid expenses at all, fill with 0.
   
2. **Transformation & Merging**:
   - Calculate a new column `profit` = `revenue - expenses`.
   - Map `store_id` to `region_name` using the JSON data. For any `store_id` not found in the JSON, set `region_name` to `"Unknown"`.
   - Filter the dataset to **exclude** any transactions where `profit < 0` (keep only zero or positive profit rows).

3. **Aggregation & Loading (Outputs)**:
   - Save the fully cleaned, merged, and filtered dataset to `/home/user/clean_data.csv` (do not include the pandas index).
   - Create an Excel file `/home/user/regional_summary.xlsx` containing two sheets:
     - Sheet 1 named `"Region_Profit"`: Total profit per region, sorted by total profit in descending order. Columns must be `region_name`, `total_profit`.
     - Sheet 2 named `"Top_Items"`: For each region, find the top 2 `item_code`s by total profit. Sort by `region_name` alphabetically, then by profit descending. Columns must be `region_name`, `item_code`, `item_profit`.

The notebook must be fully executable from top to bottom without errors using `jupyter nbconvert --to notebook --execute /home/user/etl_pipeline.ipynb`. Do not use external APIs.