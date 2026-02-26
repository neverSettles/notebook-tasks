I have a messy Python script called `messy_ab_test.py` that analyzes an A/B test for our recent marketing campaign. It works, but I need to present this to stakeholders. 

Please convert this script into a well-structured Jupyter Notebook named `/home/user/ab_test_analysis.ipynb`. 

Here is what you need to do:
1. Read the provided `messy_ab_test.py` and `campaign_data.csv` in `/home/user/`.
2. Create a new notebook `/home/user/ab_test_analysis.ipynb`.
3. Break the script down into logical, sequential cells:
   - Cell 1: Import libraries
   - Cell 2: Data Loading (load `campaign_data.csv`)
   - Cell 3: Data Preprocessing & Summary (calculate conversion rates for each group)
   - Cell 4: Statistical Testing (perform the chi-square test)
   - Cell 5: Visualization (bar chart of conversion rates)
   - Cell 6: Export Results
4. Add descriptive Markdown cells *before* each code cell explaining what the next block of code does (e.g., "## 1. Import Libraries", "## 2. Data Loading").
5. The notebook must produce the following outputs when executed:
   - Save a bar chart of the conversion rates as `/home/user/conversion_plot.png`.
   - Save the grouped summary data (Group, Total Visitors, Converted, Conversion Rate) as `/home/user/summary_stats.csv`.
   
Make sure the notebook runs perfectly from start to finish using `jupyter nbconvert --to notebook --execute /home/user/ab_test_analysis.ipynb`.

**IMPORTANT: After creating the notebook, you must run it to generate the output files.** Execute the notebook using:
```bash
jupyter nbconvert --to notebook --execute /home/user/ab_test_analysis.ipynb
```
The tests check for output files that are only created when the notebook is executed. Creating the notebook alone is not sufficient.

**Expected Output Formats:**
- `summary_stats.csv`: Must have columns `group`, `Total_Visitors`, `Converted`, `Conversion_Rate`. Must contain exactly 2 rows: one for `control` and one for `treatment` (use these exact group names).
- `conversion_plot.png`: A valid PNG bar chart.
