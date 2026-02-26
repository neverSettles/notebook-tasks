FROM ubuntu:22.04

# Avoid tzdata prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install Python, pip, and required packages
RUN apt-get update && apt-get install -y tmux \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install pytest, pandas, and jupyter for the task
RUN pip3 install matplotlib numpy pytest pandas jupyter

# Create user 'user'
RUN useradd -m -d /home/user -s /bin/bash user

# Create the raw_gene_data.csv file
RUN echo "sample,gene_A,gene_B,gene_C,gene_D\n\
S1,10,40,80,55\n\
S2,15,50,90,65\n\
S3,20,60,100,75" > /home/user/raw_gene_data.csv

# Set ownership
RUN chown user:user /home/user/raw_gene_data.csv

# Set user and working directory
# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
