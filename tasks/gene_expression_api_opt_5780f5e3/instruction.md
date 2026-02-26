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

**IMPORTANT: After creating the notebook, you must run it to generate the output files.** Execute the notebook using:
```bash
jupyter nbconvert --to notebook --execute /home/user/fetch_data.ipynb
```
The tests check for output files that are only created when the notebook is executed. Creating the notebook alone is not sufficient.

**Output CSV Requirements:**
- The output CSV columns must be: `gene_id`, `expression_level`, `sample_id` (in this exact order).
- Sort by `gene_id` ascending.
- The file should contain exactly 200 rows of data.
