FROM ubuntu:22.04

# Avoid tzdata interactive prompt
ENV DEBIAN_FRONTEND=noninteractive

# Install Python, pip, and clean up
RUN apt-get update && apt-get install -y tmux \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install required Python packages
RUN pip3 install --no-cache-dir pandas jupyter nbconvert pytest

# Create 'user' with home directory
RUN useradd -m -s /bin/bash user

# Generate the initial raw_feedback.csv file
RUN python3 -c "import pandas as pd; \
data = { \
    'id': [1, 2, 3, 4], \
    'feedback': [ \
        '<p>The service is great!</p>', \
        'The product is risqué but I <b>love</b> it.', \
        '<div>Stop! Don\'t do this in a café.</div>', \
        'An amazing experience, and I will return to it.' \
    ] \
}; \
pd.DataFrame(data).to_csv('/home/user/raw_feedback.csv', index=False)" \
    && chown user:user /home/user/raw_feedback.csv

# Set user and workdir
# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
