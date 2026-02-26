Hi! I need you to create a Jupyter notebook to standardize some messy inventory data we received. We have a prototype script, but I want a proper, reproducible notebook that we can run in production.

Here is what you need to do:
1. Create a notebook at `/home/user/standardize_data.ipynb`.
2. The notebook should read the file `/home/user/raw_inventory.csv` (which is already provided in the environment).
3. Standardize the column names: convert them all to lowercase, strip leading/trailing whitespace, and replace spaces with underscores.
4. Clean the 'product_price' column: It has mixed types (some strings with '$', some missing values like 'N/A' or 'Unknown'). Remove the '$' signs, replace 'N/A' and 'Unknown' with NaN, and convert the column to a float type.
5. Standardize the 'date_added' column: It has mixed date formats. Parse it to a datetime object, and then format it as a string in 'YYYY-MM-DD' format. If a date cannot be parsed, it should be a missing value (NaN/NaT).
6. Ensure the 'item_id' column is of type integer.
7. Save the cleaned DataFrame to `/home/user/clean_inventory.csv` (do not include the index).
8. Finally, generate a dictionary mapping the standardized column names to their final string representation of pandas dtypes (e.g., 'float64', 'int64', 'object') and save it as a JSON file at `/home/user/schema_report.json`.

The notebook must execute successfully from start to finish using `jupyter nbconvert --execute --to notebook /home/user/standardize_data.ipynb`. Use pandas for all data manipulation.

**IMPORTANT: After creating the notebook, you must run it to generate the output files.** Execute the notebook using:
```bash
jupyter nbconvert --to notebook --execute /home/user/standardize_data.ipynb
```
The tests check for output files that are only created when the notebook is executed. Creating the notebook alone is not sufficient.
