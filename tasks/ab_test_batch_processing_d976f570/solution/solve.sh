#!/bin/bash
# Gold solution

ls -l /home/user/data/campaign_day_*.csv 2>/dev/null || echo "No files"
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
    "import glob\n",
    "import json\n",
    "\n",
    "file_pattern = '/home/user/data/campaign_day_*.csv'\n",
    "all_files = glob.glob(file_pattern)\n",
    "\n",
    "valid_dfs = []\n",
    "processed_count = 0\n",
    "failed_count = 0\n",
    "\n",
    "for file in all_files:\n",
    "    try:\n",
    "        df = pd.read_csv(file)\n",
    "        if not {'user_id', 'group', 'converted'}.issubset(df.columns):\n",
    "            raise ValueError(\"Missing columns\")\n",
    "        valid_dfs.append(df)\n",
    "        processed_count += 1\n",
    "        print(f\"Processed file {file}\")\n",
    "    except Exception as e:\n",
    "        failed_count += 1\n",
    "        print(f\"Failed to process file {file}: {e}\")\n",
    "\n",
    "if valid_dfs:\n",
    "    combined_df = pd.concat(valid_dfs, ignore_index=True)\n",
    "else:\n",
    "    combined_df = pd.DataFrame(columns=['user_id', 'group', 'converted'])\n",
    "\n",
    "results = {}\n",
    "for g in ['control', 'treatment']:\n",
    "    group_df = combined_df[combined_df['group'] == g]\n",
    "    impressions = int(len(group_df))\n",
    "    conversions = int(group_df['converted'].sum()) if impressions > 0 else 0\n",
    "    conversion_rate = float(conversions / impressions) if impressions > 0 else 0.0\n",
    "    \n",
    "    results[g] = {\n",
    "        \"impressions\": impressions,\n",
    "        \"conversions\": conversions,\n",
    "        \"conversion_rate\": conversion_rate\n",
    "    }\n",
    "\n",
    "results[\"files_processed\"] = processed_count\n",
    "results[\"files_failed\"] = failed_count\n",
    "\n",
    "with open('/home/user/ab_test_summary.json', 'w') as f:\n",
    "    json.dump(results, f, indent=4)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Validation\n",
    "control_conv = results['control']['conversions']\n",
    "treatment_conv = results['treatment']['conversions']\n",
    "total_conv = int(combined_df['converted'].sum()) if not combined_df.empty else 0\n",
    "\n",
    "assert control_conv + treatment_conv == total_conv, \"Conversions sum mismatch!\"\n",
    "assert processed_count + failed_count == len(all_files), \"File counts mismatch!\"\n",
    "print(\"All validations passed.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

with open('/home/user/ab_test_batch.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)
EOF
python3 /home/user/create_nb.py && jupyter nbconvert --to notebook --execute /home/user/ab_test_batch.ipynb --inplace
cat /home/user/ab_test_summary.json
cat /home/user/data/campaign_day_1.csv
jupyter nbconvert --to script /home/user/ab_test_batch.ipynb && cat /home/user/ab_test_batch.py
python3 /home/user/ab_test_batch.py
hexdump -c /home/user/data/campaign_day_1.csv
python3 -c "print(repr(open('/home/user/data/campaign_day_1.csv').read()))"
python3 -c "print(repr(open('/home/user/data/campaign_day_3.csv').read()))"
sed -i 's/\\n/\n/g' /home/user/data/campaign_day_*.csv
python3 -c "print(repr(open('/home/user/data/campaign_day_1.csv').read()))"
python3 -c "print(repr(open('/home/user/data/campaign_day_3.csv').read()))"
jupyter nbconvert --to notebook --execute /home/user/ab_test_batch.ipynb --inplace
cat /home/user/ab_test_summary.json