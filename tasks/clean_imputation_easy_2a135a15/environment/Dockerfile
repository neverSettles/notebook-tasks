FROM ubuntu:22.04

# Install Python and pip
RUN apt-get update && \
    apt-get install -y tmux python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install required Python packages
RUN pip3 install --no-cache-dir pandas jupyter matplotlib pytest

# Create a non-root user
RUN useradd -m -s /bin/bash user

# Create the initial financial dataset
RUN echo "Date,Revenue,Expenses,Profit\n\
2023-01-01,1000,800,\n\
2023-01-02,,850,\n\
2023-01-03,1200,,\n\
2023-01-04,1300,900,\n\
2023-01-05,,," > /home/user/financial_data.csv

# Ensure correct ownership
RUN chown -R user:user /home/user

# Switch to the non-root user
# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
