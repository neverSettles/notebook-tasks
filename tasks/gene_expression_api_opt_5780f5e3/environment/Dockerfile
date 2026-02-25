FROM ubuntu:22.04

RUN apt-get update && apt-get install -y tmux python3 python3-pip && \
    pip3 install pytest pandas jupyter && \
    useradd -m -s /bin/bash user

# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user

RUN cat <<'EOF' > /home/user/mock_api.py
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

RUN cat <<'EOF' > /home/user/fetch_data.ipynb
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from mock_api import get_expression_data\n",
    "import time\n",
    "\n",
    "start_time = time.time()\n",
    "all_data = []\n",
    "for page in range(1, 21):\n",
    "    data = get_expression_data(page)\n",
    "    all_data.extend(data)\n",
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

