#!/bin/bash
# Gold solution

cat << 'EOF' > /home/user/gene_analysis.ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv('/home/user/raw_gene_data.csv')\n",
    "gene_means = df.drop(columns=['sample']).mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "filtered_genes = gene_means[gene_means > 50]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "result_df = filtered_genes.reset_index()\n",
    "result_df.columns = ['Gene', 'Mean_Expression']\n",
    "result_df.to_csv('/home/user/significant_genes.csv', index=False)"
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
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
EOF
cat /home/user/raw_gene_data.csv
jupyter nbconvert --to notebook --execute /home/user/gene_analysis.ipynb
cat /home/user/significant_genes.csv
hexdump -c /home/user/raw_gene_data.csv
python3 -c "import pandas as pd; df = pd.read_csv('/home/user/raw_gene_data.csv'); print(df)"
sed -i 's/\\n /\n/g' /home/user/raw_gene_data.csv
cat /home/user/raw_gene_data.csv
jupyter nbconvert --to notebook --execute /home/user/gene_analysis.ipynb
cat /home/user/significant_genes.csv