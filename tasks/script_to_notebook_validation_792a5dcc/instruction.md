As a Team Lead, I need you to clean up a prototype Python script and convert it into a production-ready Jupyter Notebook with proper documentation and validation checks.

You will find a Python script at `/home/user/prototype_sales_calc.py`. This script generates simulated sales data, applies discounts, calculates a summary by category, and outputs a CSV.

Please convert this script into a properly structured Jupyter Notebook named `/home/user/production_sales_analysis.ipynb`.

The notebook must meet the following requirements:
1. It must be executable from top to bottom (`jupyter nbconvert --to notebook --execute /home/user/production_sales_analysis.ipynb`).
2. Include Markdown cells:
   - A title cell at the top (e.g., `# Sales Analysis Production`).
   - A Markdown cell explaining the data generation step.
   - A Markdown cell before the validation step.
3. Code Structure:
   - Cell(s) for imports and data generation/loading.
   - Cell(s) for the core computation (`discounted_price` and grouping).
4. Validation (Crucial!): Add a new code cell dedicated to testing the correctness of the results using `assert` statements. You must assert:
   - The total number of rows in the raw data `df` is exactly 100.
   - The minimum `discounted_price` in `df` is greater than or equal to 0.
   - The sum of `discounted_price` in the grouped `summary` dataframe is exactly equal to the sum of `discounted_price` in the raw `df` dataframe (use `np.isclose` or `round` to handle floating point precision).
5. Output: The final code cell must export the `summary` dataframe to `/home/user/final_sales_summary.csv` (without the index), exactly as the original script did.

Do not alter the random seed (`np.random.seed(42)`) or the data generation logic from the original script, as the output values must remain deterministic.

**IMPORTANT: After creating the notebook, you must run it to generate the output files.** Execute the notebook using:
```bash
jupyter nbconvert --to notebook --execute /home/user/production_sales_analysis.ipynb
```
The tests check for output files that are only created when the notebook is executed. Creating the notebook alone is not sufficient.
