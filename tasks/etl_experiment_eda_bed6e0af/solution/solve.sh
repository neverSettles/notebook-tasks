#!/bin/bash
# Gold solution

cat << 'EOF' > /home/user/create_nb.py
import json

cells = [
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import pandas as pd\n",
            "import matplotlib.pyplot as plt\n",
            "import json\n",
            "\n",
            "plot_md = pd.read_csv('/home/user/plot_metadata.csv')\n",
            "yield_df = pd.read_csv('/home/user/yield_data.csv')\n",
            "df = pd.merge(plot_md, yield_df, on='plot_id', how='inner')\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "df_clean = df[(df['daily_temp'] <= 50) & (df['daily_rainfall'] >= 0)]\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "summary = df_clean.groupby('fertilizer')[['yield_kg', 'daily_temp']].mean().to_dict(orient='index')\n",
            "with open('/home/user/summary_stats.json', 'w') as f:\n",
            "    json.dump(summary, f)\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "plt.scatter(df_clean['daily_temp'], df_clean['yield_kg'])\n",
            "plt.xlabel('daily_temp')\n",
            "plt.ylabel('yield_kg')\n",
            "plt.savefig('/home/user/temp_vs_yield.png')\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "df_clean.to_csv('/home/user/clean_experiment_data.csv', index=False)\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "check_df = pd.read_csv('/home/user/clean_experiment_data.csv')\n",
            "assert len(check_df) == 8\n",
            "assert check_df['daily_temp'].max() <= 50\n",
            "assert check_df['daily_rainfall'].min() >= 0\n"
        ]
    }
]

notebook = {
    "cells": cells,
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 5
}

with open('/home/user/etl_experiment_eda.ipynb', 'w') as f:
    json.dump(notebook, f, indent=2)
EOF
python3 /home/user/create_nb.py
jupyter nbconvert --to notebook --execute /home/user/etl_experiment_eda.ipynb
cat /home/user/summary_stats.json
ls -l /home/user/temp_vs_yield.png
cat /home/user/clean_experiment_data.csv
cat /home/user/plot_metadata.csv
cat << 'EOF' > /home/user/create_nb.py
import json

cells = [
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import pandas as pd\n",
            "import matplotlib.pyplot as plt\n",
            "import json\n",
            "\n",
            "plot_md = pd.read_csv('/home/user/plot_metadata.csv', keep_default_na=False)\n",
            "yield_df = pd.read_csv('/home/user/yield_data.csv')\n",
            "df = pd.merge(plot_md, yield_df, on='plot_id', how='inner')\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "df_clean = df[(df['daily_temp'] <= 50) & (df['daily_rainfall'] >= 0)]\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "summary = df_clean.groupby('fertilizer')[['yield_kg', 'daily_temp']].mean().to_dict(orient='index')\n",
            "with open('/home/user/summary_stats.json', 'w') as f:\n",
            "    json.dump(summary, f)\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "plt.scatter(df_clean['daily_temp'], df_clean['yield_kg'])\n",
            "plt.xlabel('daily_temp')\n",
            "plt.ylabel('yield_kg')\n",
            "plt.savefig('/home/user/temp_vs_yield.png')\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "df_clean.to_csv('/home/user/clean_experiment_data.csv', index=False)\n"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "check_df = pd.read_csv('/home/user/clean_experiment_data.csv', keep_default_na=False)\n",
            "assert len(check_df) == 8\n",
            "assert check_df['daily_temp'].max() <= 50\n",
            "assert check_df['daily_rainfall'].min() >= 0\n"
        ]
    }
]

notebook = {
    "cells": cells,
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 5
}

with open('/home/user/etl_experiment_eda.ipynb', 'w') as f:
    json.dump(notebook, f, indent=2)
EOF
python3 /home/user/create_nb.py
jupyter nbconvert --to notebook --execute /home/user/etl_experiment_eda.ipynb
cat /home/user/summary_stats.json
cat /home/user/clean_experiment_data.csv