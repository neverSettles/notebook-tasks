FROM ubuntu:22.04

# Avoid tzdata interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y tmux \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install required Python packages for the task and testing
RUN pip3 install --no-cache-dir pytest pandas jupyter notebook

# Create user 'user'
RUN useradd -m -d /home/user -s /bin/bash user

# Create the input CSV file
RUN printf 'date,headline,price\n2023-01-01,The Company XYZ Announces New Product!,100.50\n2023-01-02,A terrible day for the markets.,98.20\n2023-01-03,Is an economic boom on the horizon?,102.00\n2023-01-04,Investors are looking at safe havens.,101.10\n' > /home/user/financial_news.csv

# Ensure correct permissions
RUN chown -R user:user /home/user

# Set working directory and user
WORKDIR /home/user
# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

