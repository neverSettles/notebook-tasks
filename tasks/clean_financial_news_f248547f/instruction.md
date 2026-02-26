I need you to create a Jupyter notebook to clean some financial news data. 

Please create a notebook at `/home/user/clean_analysis.ipynb`. The notebook should read `/home/user/financial_news.csv`.

Here is what the notebook needs to do:
1. **Cell 1**: Import pandas and re. Define a custom stopword list: `['the', 'a', 'an', 'in', 'on', 'at', 'for', 'to', 'of', 'and', 'is', 'are']`.
2. **Cell 2**: Load the data from `/home/user/financial_news.csv` into a pandas DataFrame.
3. **Cell 3**: Create a new column called `cleaned_headline`. To create this, process the `headline` column as follows:
   - Convert all text to lowercase.
   - Remove all punctuation (keep only lowercase letters `a-z`, digits `0-9`, and spaces).
   - Split the text by spaces, and remove any words that exactly match the custom stopword list.
   - Join the remaining words back together with a single space.
4. **Cell 4**: Keep only the `date`, `cleaned_headline`, and `price` columns. Save the resulting DataFrame to `/home/user/cleaned_news.csv` (do not include the index).

Make sure the notebook can be executed sequentially from start to finish without errors.

**IMPORTANT: After creating the notebook, you must run it to generate the output files.** Execute the notebook using:
```bash
jupyter nbconvert --to notebook --execute /home/user/clean_analysis.ipynb
```
The tests check for output files that are only created when the notebook is executed. Creating the notebook alone is not sufficient.
