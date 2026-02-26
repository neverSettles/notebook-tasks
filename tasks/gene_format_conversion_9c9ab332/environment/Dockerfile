FROM ubuntu:22.04

# Avoid tzdata interactive prompt
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y tmux \
    python3 \
    python3-pip \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Install required Python packages
RUN pip3 install --no-cache-dir matplotlib numpy pytest jupyter nbconvert pandas openpyxl

# Create user
RUN useradd -m -s /bin/bash user

# Create the input dataset
RUN echo "Gene ID,Expression Level,P-Value\n\
GENE_1,5.5,0.01\n\
GENE_2,15.2,0.04\n\
GENE_3,8.0,0.10\n\
GENE_4,102.3,0.001\n\
GENE_5,10.0,0.05" > /home/user/raw_genes.csv

# Ensure correct ownership
RUN chown user:user /home/user/raw_genes.csv

# Switch to the new user
# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
