You are a Business Analyst creating a cron-ready Jupyter notebook to automate a quarterly performance report.

Your task is to create a Jupyter notebook at `/home/user/quarterly_report.ipynb` that processes customer feedback and merges it with sales data. Since this notebook will run automatically, it must include robust text cleaning and explicit validation steps.

The notebook must perform the following steps in order:

1. **Load Data**: 
   - Load `/home/user/raw_feedback.csv` (columns: `id`, `date`, `feedback`, `agent_id`).
   - Load `/home/user/sales.json` (a list of dictionaries containing `agent_id` and `revenue`).

2. **Text Cleaning**:
   Process the `feedback` column to handle several edge cases:
   - **HTML Tags**: Remove all HTML tags, including nested tags (e.g., `<div><p>text</p></div>` should become `text`). Ensure content between tags is preserved, except for `<script>` tags where you should remove the tags but you can leave the content. (Just standard regex or BeautifulSoup tag removal is fine).
   - **HTML Entities**: Decode HTML entities (e.g., `&amp;` becomes `&`, `&lt;` becomes `<`).
   - **Unicode Normalization**: Normalize all unicode characters to NFKC form.
   - **PII Redaction**: 
     - Replace all email addresses with the exact string `[EMAIL]`.
     - Replace all phone numbers matching the format `XXX-XXX-XXXX` with the exact string `[PHONE]`.
   - **Whitespace**: Strip leading/trailing whitespace and replace multiple consecutive spaces with a single space.

3. **Data Merging**:
   - Merge the cleaned feedback dataframe with the sales dataframe on `agent_id` (inner join).

4. **Validation (Crucial for automation)**:
   Add a cell at the end of the notebook containing `assert` statements to validate the pipeline:
   - Assert that no HTML tags remain in the `feedback` column (using a regex like `<[^>]+>`).
   - Assert that no emails remain in the `feedback` column.
   - Assert that no phone numbers of the format `XXX-XXX-XXXX` remain in the `feedback` column.
   - Assert that the final dataframe has exactly 5 rows.

5. **Export**:
   - Save the final merged dataframe to `/home/user/final_report.csv` without the index.

Requirements:
- Only use standard data science libraries (pandas, numpy, re, html, unicodedata).
- The notebook must be executable from start to finish via `jupyter nbconvert --to notebook --execute /home/user/quarterly_report.ipynb` without raising any assertion errors.