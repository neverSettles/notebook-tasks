FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y tmux python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install python packages required for the task
RUN pip3 install --no-cache-dir pytest pandas jupyter matplotlib

# Create user
RUN useradd -m -s /bin/bash user

# Generate initial input data
RUN printf 'import pandas as pd\n\nmeta = pd.DataFrame({\n    '\''plot_id'\'': [f'\''P{i:03d}'\'' for i in range(1, 11)],\n    '\''group'\'': ['\''Control'\'', '\''Treatment'\'', '\''Treatment'\'', '\''Control'\'', '\''Treatment'\'', '\''Control'\'', '\''Treatment'\'', '\''Treatment'\'', '\''Control'\'', '\''Treatment'\''],\n    '\''fertilizer'\'': ['\''None'\'', '\''F_A'\'', '\''F_B'\'', '\''None'\'', '\''F_A'\'', '\''None'\'', '\''F_B'\'', '\''F_A'\'', '\''None'\'', '\''F_B'\'']\n})\nmeta.to_csv('\''/home/user/plot_metadata.csv'\'', index=False)\n\ndata = pd.DataFrame({\n    '\''plot_id'\'': [f'\''P{i:03d}'\'' for i in range(1, 11)],\n    '\''daily_temp'\'': [22.5, 23.1, 60.0, 21.8, 24.5, 22.0, 23.8, 24.2, 21.5, 25.0],\n    '\''daily_rainfall'\'': [10.5, 12.0, 11.5, -5.0, 14.0, 10.0, 13.5, 14.2, 9.5, 15.0],\n    '\''yield_kg'\'': [150.0, 180.5, 20.0, 145.0, 185.0, 148.0, 190.0, 182.0, 140.0, 195.0]\n})\ndata.to_csv('\''/home/user/yield_data.csv'\'', index=False)\n' > /tmp/setup_data.py

RUN python3 /tmp/setup_data.py && \
    rm /tmp/setup_data.py && \
    chown -R user:user /home/user

WORKDIR /home/user
# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

