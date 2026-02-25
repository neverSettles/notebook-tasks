#!/bin/bash
# Gold solution

python3 -c '
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
    "import sqlite3\n",
    "\n",
    "df = pd.read_csv(\"/home/user/raw_sales.csv\")\n",
    "conn = sqlite3.connect(\":memory:\")\n",
    "df.to_sql(\"sales\", conn, index=False)\n",
    "\n",
    "query = \"\"\"\n",
    "SELECT \n",
    "    region, \n",
    "    SUM(amount) AS total_revenue,\n",
    "    RANK() OVER (ORDER BY SUM(amount) DESC) AS sales_rank\n",
    "FROM sales\n",
    "GROUP BY region\n",
    "\"\"\"\n",
    "result_df = pd.read_sql_query(query, conn)\n",
    "result_df.to_csv(\"/home/user/clean_sales.csv\", index=False)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

with open("/home/user/etl_pipeline.ipynb", "w") as f:
    json.dump(notebook, f)
'
jupyter nbconvert --to notebook --execute /home/user/etl_pipeline.ipynb
cat /home/user/clean_sales.csv
cat /home/user/raw_sales.csv
od -c /home/user/raw_sales.csv
sed -i 's/\\n/\n/g' /home/user/raw_sales.csv
cat /home/user/raw_sales.csv
jupyter nbconvert --to notebook --execute /home/user/etl_pipeline.ipynb
cat /home/user/clean_sales.csv