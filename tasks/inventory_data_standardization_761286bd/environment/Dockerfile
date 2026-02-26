FROM ubuntu:22.04

# Avoid tzdata interactive prompt during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Python, pip, and clean up
RUN apt-get update && apt-get install -y tmux \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install required Python packages for the task and testing
RUN pip3 install --no-cache-dir pytest pandas jupyter

# Create user 'user'
RUN useradd -m -s /bin/bash user

# Create the raw input data file
RUN printf 'Item ID, Product Name ,Product Price, Date Added\n101,Widget A,$12.50,12/31/2022\n102,Widget B,15.00,2023-01-15\n103,Widget C,N/A,15-Jan-2023\n104,Widget D,$9.99,Unknown\n105,Widget E,Unknown,03/05/23\n' > /home/user/raw_inventory.csv

# Ensure correct permissions
RUN chown -R user:user /home/user

# Switch to user
# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
