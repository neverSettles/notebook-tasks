As a marketing analyst, I need a robust Jupyter notebook to process daily A/B test results. We have several daily CSV logs, but sometimes the data extraction fails and produces corrupt files. 

Please create a Jupyter notebook at `/home/user/ab_test_batch.ipynb` that does the following:

1. **Batch Processing & Error Handling:** 
   - Iterate through all files matching `/home/user/data/campaign_day_*.csv`.
   - Read each file using pandas. 
   - Implement error handling (e.g., `try...except`) to catch and skip files that cannot be parsed as CSVs (e.g., due to parsing errors or missing columns). 
   - Print a progress message for each file (e.g., "Processed file X" or "Failed to process file Y").

2. **Data Aggregation:**
   - Combine the valid data. The valid CSVs will have columns: `user_id`, `group` (either 'control' or 'treatment'), and `converted` (1 or 0).
   - Calculate the total impressions (number of rows), total conversions (sum of `converted`), and the conversion rate (conversions / impressions) for BOTH the `control` and `treatment` groups across all valid files.

3. **Validation Cells (Testing):**
   - Add a separate cell at the end of the notebook with `assert` statements to validate your results. 
   - Assert that the sum of conversions in the control group plus the treatment group exactly equals the total sum of the `converted` column from the raw combined valid dataframe.
   - Assert that the number of successfully processed files plus the number of failed files equals the total number of matched files.

4. **Output Generation:**
   - Save the final aggregated results as a JSON file at `/home/user/ab_test_summary.json`.
   - The JSON MUST have exactly this structure:
     ```json
     {
         "control": {
             "impressions": <int>,
             "conversions": <int>,
             "conversion_rate": <float>
         },
         "treatment": {
             "impressions": <int>,
             "conversions": <int>,
             "conversion_rate": <float>
         },
         "files_processed": <int>,
         "files_failed": <int>
     }
     ```

Do not use any external APIs or require internet access. The notebook must execute cleanly from top to bottom.