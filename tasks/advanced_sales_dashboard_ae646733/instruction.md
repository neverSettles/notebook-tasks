My colleague was working on a sales dashboard notebook, but they left the company. I need you to create a completely new Jupyter notebook at `/home/user/dashboard.ipynb` that processes the raw sales data and generates the required outputs. The data is messier now and involves multiple currencies.

You have two input files:
1. `/home/user/sales_data.csv` (Columns: `Date`, `OrderID`, `Product`, `Quantity`, `UnitPrice`, `Currency`)
2. `/home/user/exchange_rates.csv` (Columns: `Date`, `Currency`, `Rate_to_USD`)

Your notebook must perform the following operations:
1. **Data Cleaning**: 
   - Parse the `Date` columns in both files. The sales data might have mixed date formats. Convert them to `YYYY-MM-DD`.
   - Remove any rows from `sales_data.csv` where `Quantity <= 0` or `UnitPrice <= 0` (these are invalid or returns).
   - Drop rows with missing values in `Quantity` or `UnitPrice`.

2. **Currency Conversion**:
   - Merge the sales data with the exchange rates. 
   - Note: The exchange rates are only provided for weekdays or specific dates. You must forward-fill missing exchange rates for each currency. If a sales date is before the first available exchange rate for a currency, back-fill it.
   - Calculate a new column `USD_Revenue` = `Quantity * UnitPrice / Rate_to_USD`.

3. **Aggregation**:
   - Calculate total daily `USD_Revenue` for all products combined.
   - Calculate a rolling 7-day average of the daily `USD_Revenue`. (For the first 6 days, the rolling average should be calculated using `min_periods=1`).
   
4. **Outputs**:
   - Save the daily aggregated data to `/home/user/daily_sales.csv`. It must have exactly three columns: `Date`, `Daily_Revenue`, `Rolling_7d_Revenue`. The dates should be sorted chronologically. All float values should be rounded to 2 decimal places.
   - Save a JSON file `/home/user/metrics.json` containing:
     - `"Total_USD_Revenue"`: Total revenue across all valid rows (rounded to 2 decimal places).
     - `"Top_Product"`: The name of the product with the highest total `USD_Revenue`.
   - Create a plot of `Date` vs `Rolling_7d_Revenue` and save it as `/home/user/dashboard.png` using matplotlib or seaborn.

The notebook must be perfectly executable with `jupyter nbconvert --to notebook --execute /home/user/dashboard.ipynb`. Do not use external APIs.