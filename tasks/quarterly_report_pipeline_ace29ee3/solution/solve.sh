#!/bin/bash
# Gold solution

ls -l /home/user/
cat << 'EOF' > /home/user/create_nb.py
import json

notebook = {
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import json\n",
    "import re\n",
    "import html\n",
    "import unicodedata\n",
    "\n",
    "df_feedback = pd.read_csv('/home/user/raw_feedback.csv')\n",
    "with open('/home/user/sales.json', 'r') as f:\n",
    "    sales_data = json.load(f)\n",
    "df_sales = pd.DataFrame(sales_data)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_text(text):\n",
    "    if pd.isna(text): return text\n",
    "    text = str(text)\n",
    "    text = html.unescape(text)\n",
    "    text = unicodedata.normalize('NFKC', text)\n",
    "    text = re.sub(r'<[^>]+>', '', text)\n",
    "    text = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}', '[EMAIL]', text)\n",
    "    text = re.sub(r'\\d{3}-\\d{3}-\\d{4}', '[PHONE]', text)\n",
    "    text = re.sub(r'\\s+', ' ', text).strip()\n",
    "    return text\n",
    "\n",
    "df_feedback['feedback'] = df_feedback['feedback'].apply(clean_text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_merged = pd.merge(df_feedback, df_sales, on='agent_id', how='inner')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "assert not df_merged['feedback'].str.contains(r'<[^>]+>', regex=True).any()\n",
    "assert not df_merged['feedback'].str.contains(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}', regex=True).any()\n",
    "assert not df_merged['feedback'].str.contains(r'\\d{3}-\\d{3}-\\d{4}', regex=True).any()\n",
    "assert len(df_merged) == 5\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_merged.to_csv('/home/user/final_report.csv', index=False)\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

with open('/home/user/quarterly_report.ipynb', 'w') as f:
    json.dump(notebook, f)
EOF
python3 /home/user/create_nb.py
jupyter nbconvert --to notebook --execute /home/user/quarterly_report.ipynb
cat /home/user/final_report.csv