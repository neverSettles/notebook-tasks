FROM ubuntu:22.04

# Install basic requirements
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies including pytest
RUN pip3 install pytest pandas jupyter matplotlib seaborn nbconvert

# Create user
RUN useradd -m -s /bin/bash user

# Create initial data file
RUN echo "transaction_id,date,region,revenue\n\
1,2023-01-15,North,100.50\n\
2,2023-02-20,South,200.00\n\
3,2023-03-05,North,150.25\n\
4,2023-03-12,East,300.00\n\
5,2023-03-22,South,50.00" > /home/user/raw_sales.csv

# Ensure permissions
RUN chown -R user:user /home/user

# Switch to user
# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
