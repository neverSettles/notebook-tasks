You are a Quantitative Analyst processing financial time series data. You have an existing Python script (`/home/user/process_finance.py`) that reads a wide-format CSV of stock prices, melts it into a long format, calculates the average price per ticker, and saves the results.

Your task is to convert this script into a clean, structured Jupyter notebook named `/home/user/finance_analysis.ipynb`.

Requirements for the notebook:
1. Create exactly 3 code cells:
   - Cell 1: Import pandas and load the data (`stocks.csv`).
   - Cell 2: Melt the DataFrame from wide to long format (Date, Ticker, Price).
   - Cell 3: Group by Ticker, calculate the mean 'Price', and save to `/home/user/avg_prices.csv` (without the index).

Execute the notebook to ensure it generates `avg_prices.csv` successfully. Ensure your notebook is valid JSON and runs without errors using `jupyter nbconvert --to notebook --execute /home/user/finance_analysis.ipynb`.