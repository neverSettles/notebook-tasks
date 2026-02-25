#!/bin/bash
# Gold solution

cat << 'EOF' > /home/user/make_nb.py
import json

cells = [
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import pandas as pd\n",
            "import json\n",
            "import numpy as np\n",
            "\n",
            "df = pd.read_csv('/home/user/raw_inventory.csv')\n",
            "df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')\n",
            "\n",
            "df['product_price'] = df['product_price'].astype(str).str.replace('$', '', regex=False).replace(['N/A', 'Unknown', 'nan'], [np.nan, np.nan, np.nan])\n",
            "df['product_price'] = pd.to_numeric(df['product_price'], errors='coerce')\n",
            "\n",
            "df['date_added'] = pd.to_datetime(df['date_added'], format='mixed', errors='coerce').dt.strftime('%Y-%m-%d')\n",
            "\n",
            "df['item_id'] = df['item_id'].astype(int)\n",
            "\n",
            "df.to_csv('/home/user/clean_inventory.csv', index=False)\n",
            "\n",
            "schema = {col: str(dtype) for col, dtype in df.dtypes.items()}\n",
            "with open('/home/user/schema_report.json', 'w') as f:\n",
            "    json.dump(schema, f)\n"
        ]
    }
]

notebook = {
    "cells": cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

with open('/home/user/standardize_data.ipynb', 'w') as f:
    json.dump(notebook, f)
EOF
python3 /home/user/make_nb.py
jupyter nbconvert --execute --to notebook --inplace /home/user/standardize_data.ipynb
cat /home/user/schema_report.json
cat /home/user/clean_inventory.csv