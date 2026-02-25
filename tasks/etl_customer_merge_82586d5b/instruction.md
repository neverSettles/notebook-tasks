You need to build a data merging step for our ETL pipeline in a Jupyter notebook. We have customer records coming from two different systems: a CRM and an E-commerce platform. Because customers update their info in both places, we have data conflicts that need to be resolved based on which record was updated most recently.

Create a notebook at `/home/user/etl_merge.ipynb` that does the following:

1. **Load Data**: 
   - Load `/home/user/crm_data.csv` and `/home/user/ecom_data.csv`. 

2. **Merge & Resolve Conflicts**:
   - Perform an outer join on the `customer_id` column.
   - Both datasets have `email` and `phone` columns. 
   - Both datasets have a timestamp column: `crm_last_updated` and `ecom_last_updated`.
   - For `email` and `phone`, resolve conflicts by selecting the value from the system with the most recent timestamp (`crm_last_updated` vs `ecom_last_updated`). If a record only exists in one system, use that system's values.
   - If timestamps are exactly equal, prefer the CRM data.
   - Keep the `total_spent` column from the e-commerce data (fill missing with 0.0).
   - Keep the `name` column from the CRM data (fill missing with "Unknown").
   - Drop the old overlapping columns and the timestamp columns. The final columns should be exactly: `customer_id`, `name`, `email`, `phone`, `total_spent`.

3. **Validation Cells**:
   - Add a cell at the end of the notebook with `assert` statements to validate the exact output. 
   - Assert that the final DataFrame has exactly 5 rows.
   - Assert that `customer_id` 3 has the email `bob_new@ecom.com` (because ecom was updated more recently).
   - Assert that `customer_id` 4 has `total_spent` equal to 0.0 (since it only exists in CRM).

4. **Save Output**:
   - Save the cleaned, merged dataframe to `/home/user/merged_customers.csv` (without the index).

Your notebook must run from top to bottom without errors using `jupyter nbconvert --to notebook --execute /home/user/etl_merge.ipynb`.