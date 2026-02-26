FROM ubuntu:22.04

RUN apt-get update && apt-get install -y tmux python3 python3-pip && \
    pip3 install pytest pandas jupyter && \
    useradd -m -s /bin/bash user

# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user

RUN printf 'import time\n\ndef get_expression_data(page):\n    time.sleep(0.5)\n    if page < 1 or page > 20:\n        return []\n    data = []\n    for i in range(10):\n        gene_num = (page - 1) * 10 + i\n        data.append({\n            "gene_id": f"GENE_{gene_num:03d}",\n            "expression_level": round(10.5 + page * 0.1 + i * 0.05, 2),\n            "sample_id": "S1"\n        })\n    return data\n' > /home/user/mock_api.py

RUN printf '{\n "cells": [\n  {\n   "cell_type": "code",\n   "execution_count": 1,\n   "metadata": {},\n   "outputs": [],\n   "source": [\n    "import pandas as pd\n",\n    "from mock_api import get_expression_data\n",\n    "import time\n",\n    "\n",\n    "start_time = time.time()\n",\n    "all_data = []\n",\n    "for page in range(1, 21):\n",\n    "    data = get_expression_data(page)\n",\n    "    all_data.extend(data)\n",\n    "\n",\n    "df = pd.DataFrame(all_data)\n",\n    "df = df.sort_values('\''gene_id'\'')\n",\n    "df.to_csv('\''/home/user/expression_data.csv'\'', index=False)\n",\n    "print(f'\''Time taken: {time.time() - start_time:.2f} seconds'\'')"\n   ]\n  }\n ],\n "metadata": {},\n "nbformat": 4,\n "nbformat_minor": 5\n}\n' > /home/user/fetch_data.ipynb

