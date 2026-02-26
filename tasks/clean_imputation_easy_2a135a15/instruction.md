I need you to create a well-structured Jupyter notebook at `/home/user/clean_imputation.ipynb` to clean up some missing financial data.

Please write a notebook that does the following:
1. Load the dataset `/home/user/financial_data.csv` using pandas.
2. Set the 'Date' column as the DataFrame index.
3. Impute missing values in the 'Revenue' column using forward fill (`ffill()`).
4. Impute missing values in the 'Expenses' column using the mean value of the 'Expenses' column.
5. Calculate the 'Profit' column as 'Revenue' minus 'Expenses'.
6. Save the cleaned DataFrame to `/home/user/cleaned_financial_data.csv` (keep the Date index).

The notebook must be perfectly executable with `jupyter nbconvert --to notebook --execute /home/user/clean_imputation.ipynb`.


**Additional Requirement - Outlier Detection and Visualization:**
After imputation and calculating Profit:
1. Add a cell that detects outliers in the 'Revenue' column using the IQR method (values outside Q1-1.5*IQR to Q3+1.5*IQR).
2. Save a box plot of Revenue and Expenses (side by side) to `/home/user/boxplot.png`.
3. Save a JSON report at `/home/user/outlier_report.json` with keys: `"n_revenue_outliers"` (int), `"revenue_mean"` (float), `"revenue_std"` (float).

**IMPORTANT: After creating the notebook, you must run it to generate the output files.** Execute the notebook using:
```bash
jupyter nbconvert --to notebook --execute /home/user/clean_imputation.ipynb
```
The tests check for output files that are only created when the notebook is executed. Creating the notebook alone is not sufficient.
