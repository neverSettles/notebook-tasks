You are a Business Analyst preparing a quarterly performance report. Part of this report requires analyzing customer feedback, but the raw text data is messy. 

Your task is to create a Jupyter notebook at `/home/user/quarterly_feedback_cleaning.ipynb` that cleans this text data and saves the result. 

An input file named `/home/user/raw_feedback.csv` will be available with two columns: `id` and `feedback`.

In your notebook, perform the following steps:
1. Load the `raw_feedback.csv` dataset using pandas.
2. Create a new column called `cleaned_feedback` by applying the following text cleaning steps to the `feedback` column (in this order):
   - Convert all text to lowercase.
   - Strip all HTML tags (e.g., `<p>`, `</div>`, `<b>`) using regular expressions.
   - Normalize Unicode characters to remove accents (e.g., "café" becomes "cafe"). Use `unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')`.
   - Remove all punctuation (using `string.punctuation`).
   - Remove the following predefined stopwords: `["the", "is", "a", "an", "and", "but", "or", "to", "this", "it", "in", "of"]`. (Tokens should be separated by whitespace).
3. Add a validation cell with `assert` statements to verify the processing works correctly. Specifically, assert that the cleaned text for `id == 2` is exactly `"product risque love"`.
4. Save the resulting dataframe (keeping both the `id` and `cleaned_feedback` columns) to `/home/user/cleaned_feedback.csv`.

Ensure your notebook executes sequentially without errors using `jupyter nbconvert --to notebook --execute /home/user/quarterly_feedback_cleaning.ipynb`. Do not use external libraries like `nltk` or `spacy` that require internet downloads; rely on standard Python libraries like `re`, `string`, `unicodedata`, and `pandas`.

**IMPORTANT: After creating the notebook, you must run it to generate the output files.** Execute the notebook using:
```bash
jupyter nbconvert --to notebook --execute /home/user/quarterly_feedback_cleaning.ipynb
```
The tests check for output files that are only created when the notebook is executed. Creating the notebook alone is not sufficient.
