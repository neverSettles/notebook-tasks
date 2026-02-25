#!/bin/bash
# Gold solution

python3 -c "import json
notebook = {
 'cells': [
  {
   'cell_type': 'code',
   'execution_count': None,
   'metadata': {},
   'outputs': [],
   'source': [
    'import pandas as pd\n',
    'import re\n',
    '\n',
    'stopwords = [\'the\', \'a\', \'an\', \'in\', \'on\', \'at\', \'for\', \'to\', \'of\', \'and\', \'is\', \'are\']'
   ]
  },
  {
   'cell_type': 'code',
   'execution_count': None,
   'metadata': {},
   'outputs': [],
   'source': [
    'df = pd.read_csv(\'/home/user/financial_news.csv\')'
   ]
  },
  {
   'cell_type': 'code',
   'execution_count': None,
   'metadata': {},
   'outputs': [],
   'source': [
    'def clean_text(text):\n',
    '    text = str(text).lower()\n',
    '    text = re.sub(r\'[^a-z0-9\\s]\', \'\', text)\n',
    '    words = text.split()\n',
    '    words = [w for w in words if w not in stopwords]\n',
    '    return \' \'.join(words)\n',
    '\n',
    'df[\'cleaned_headline\'] = df[\'headline\'].apply(clean_text)'
   ]
  },
  {
   'cell_type': 'code',
   'execution_count': None,
   'metadata': {},
   'outputs': [],
   'source': [
    'df = df[[\'date\', \'cleaned_headline\', \'price\']]\n',
    'df.to_csv(\'/home/user/cleaned_news.csv\', index=False)'
   ]
  }
 ],
 'metadata': {
  'language_info': {
   'name': 'python'
  }
 },
 'nbformat': 4,
 'nbformat_minor': 4
}
with open('/home/user/clean_analysis.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)
"
jupyter nbconvert --to notebook --execute /home/user/clean_analysis.ipynb
cat /home/user/cleaned_news.csv