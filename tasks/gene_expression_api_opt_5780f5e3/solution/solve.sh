#!/bin/bash
# Gold solution

cat /home/user/fetch_data.ipynb
cat << 'EOF' > /home/user/fetch_data.ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from mock_api import get_expression_data\n",
    "import time\n",
    "import concurrent.futures\n",
    "\n",
    "start_time = time.time()\n",
    "all_data = []\n",
    "\n",
    "def fetch(page):\n",
    "    return get_expression_data(page)\n",
    "\n",
    "with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:\n",
    "    results = executor.map(fetch, range(1, 21))\n",
    "    for data in results:\n",
    "        all_data.extend(data)\n",
    "\n",
    "df = pd.DataFrame(all_data)\n",
    "df = df.sort_values('gene_id')\n",
    "df.to_csv('/home/user/expression_data.csv', index=False)\n",
    "print(f'Time taken: {time.time() - start_time:.2f} seconds')"
   ]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
EOF
jupyter nbconvert --to notebook --execute /home/user/fetch_data.ipynb
python3 -m jupyter nbconvert --to notebook --execute /home/user/fetch_data.ipynb
pip install jupyter nbconvert pandas
python3 -m jupyter nbconvert --to notebook --execute /home/user/fetch_data.ipynb
cat /home/user/mock_api.py
cat << 'EOF' > /home/user/mock_api.py
import time
def get_expression_data(page):
    time.sleep(0.5)
    if page < 1 or page > 20:
        return []
    data = []
    for i in range(10):
        gene_num = (page - 1) * 10 + i
        data.append({
            "gene_id": f"GENE_{gene_num:03d}",
            "expression_level": round(10.5 + page * 0.1 + i * 0.05, 2),
            "sample_id": "S1"
        })
    return data
EOF
python3 -m jupyter nbconvert --to notebook --execute /home/user/fetch_data.ipynb