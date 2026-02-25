I have a Jupyter notebook `/home/user/fetch_data.ipynb` that fetches gene expression data from a local mock API (simulating a real API). The notebook works and saves the data, but it is too slow because it fetches the 20 pages sequentially. Each request takes about 0.5 seconds, so the whole process takes over 10 seconds. 

Your task is to optimize the notebook to complete the data collection in under 3 seconds. You must use parallel execution (e.g., `concurrent.futures.ThreadPoolExecutor`) to fetch the pages concurrently.

Requirements:
1. Modify `/home/user/fetch_data.ipynb`.
2. Fetch all 20 pages (pages 1 to 20 inclusive) using the `get_expression_data(page)` function from the provided `mock_api` module.
3. Combine all retrieved records into a single pandas DataFrame.
4. Sort the DataFrame by the `gene_id` column in ascending order.
5. Save the final DataFrame to `/home/user/expression_data.csv` without the index.
6. The entire execution of the notebook using `jupyter nbconvert --to notebook --execute` must take less than 4 seconds.

The `mock_api.py` module and the slow `fetch_data.ipynb` are already in `/home/user`.