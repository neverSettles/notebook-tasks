I need you to create a well-structured Jupyter notebook at `/home/user/clean_imputation.ipynb` to clean up some missing financial data.

Please write a notebook that does the following:
1. Load the dataset `/home/user/financial_data.csv` using pandas.
2. Set the 'Date' column as the DataFrame index.
3. Impute missing values in the 'Revenue' column using forward fill (`ffill()`).
4. Impute missing values in the 'Expenses' column using the mean value of the 'Expenses' column.
5. Calculate the 'Profit' column as 'Revenue' minus 'Expenses'.
6. Save the cleaned DataFrame to `/home/user/cleaned_financial_data.csv` (keep the Date index).

The notebook must be perfectly executable with `jupyter nbconvert --to notebook --execute /home/user/clean_imputation.ipynb`.