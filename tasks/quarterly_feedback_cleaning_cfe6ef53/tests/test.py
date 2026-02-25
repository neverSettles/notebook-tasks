# test_final_state.py

import os
import subprocess
import pandas as pd
import pytest
import re
import string
import unicodedata

def test_notebook_exists():
    notebook_path = '/home/user/quarterly_feedback_cleaning.ipynb'
    assert os.path.exists(notebook_path), f"The notebook {notebook_path} does not exist."
    assert os.path.isfile(notebook_path), f"{notebook_path} is not a file."

def test_notebook_executes_successfully():
    notebook_path = '/home/user/quarterly_feedback_cleaning.ipynb'
    assert os.path.exists(notebook_path), "Notebook missing, cannot execute."

    # Execute the notebook
    result = subprocess.run(
        ['jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', notebook_path],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Notebook execution failed.\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"

def test_output_csv_exists_and_format():
    output_csv = '/home/user/cleaned_feedback.csv'
    assert os.path.exists(output_csv), f"The expected output file {output_csv} does not exist."

    df = pd.read_csv(output_csv)
    assert 'id' in df.columns, "'id' column missing in output CSV."
    assert 'cleaned_feedback' in df.columns, "'cleaned_feedback' column missing in output CSV."
    assert len(df) == 4, "Output CSV should have exactly 4 rows."

def test_output_csv_correctness():
    output_csv = '/home/user/cleaned_feedback.csv'
    assert os.path.exists(output_csv), "Output CSV missing."

    df = pd.read_csv(output_csv)

    # We apply the described logic to determine expected values based on prompt instructions
    stopwords = ["the", "is", "a", "an", "and", "but", "or", "to", "this", "it", "in", "of"]

    def clean_text(text):
        if not isinstance(text, str):
            return text
        # Lowercase
        text = text.lower()
        # Strip HTML
        text = re.sub(r'<[^>]+>', '', text)
        # Normalize Unicode
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Remove stopwords
        tokens = [word for word in text.split() if word not in stopwords]
        return ' '.join(tokens)

    # Original data
    raw_feedback = [
        '<p>The service is great!</p>',
        'The product is risqué but I <b>love</b> it.',
        '<div>Stop! Don\'t do this in a café.</div>',
        'An amazing experience, and I will return to it.'
    ]

    expected_cleaned = [clean_text(t) for t in raw_feedback]

    actual_cleaned = df['cleaned_feedback'].fillna('').tolist()

    for i, (actual, expected) in enumerate(zip(actual_cleaned, expected_cleaned)):
        # Allowing a manual override for id 2 if the user strictly followed the bad assert in prompt
        if i == 1 and actual == "product risque love":
            continue
        assert actual == expected, f"Row {i+1} mismatch. Expected '{expected}', got '{actual}'"