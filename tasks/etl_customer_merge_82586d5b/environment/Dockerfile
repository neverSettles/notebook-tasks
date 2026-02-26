FROM ubuntu:22.04

# Avoid tzdata interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y tmux python3 python3-pip sudo && \
    pip3 install pytest pandas jupyter nbconvert && \
    rm -rf /var/lib/apt/lists/*

# Create user
RUN useradd -m -s /bin/bash user && \
    echo "user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Set up data files
RUN printf 'customer_id,name,email,phone,crm_last_updated\n1,Alice,alice@crm.com,555-0101,2023-01-10T10:00:00\n2,Bob,bob@crm.com,555-0102,2023-01-12T10:00:00\n3,Charlie,charlie@crm.com,555-0103,2023-01-05T10:00:00\n4,David,david@crm.com,555-0104,2023-01-15T10:00:00\n' > /home/user/crm_data.csv

RUN printf 'customer_id,email,phone,ecom_last_updated,total_spent\n1,alice@crm.com,555-0101,2023-01-01T10:00:00,150.50\n2,bob@ecom.com,555-0999,2023-01-11T10:00:00,200.00\n3,charlie_new@ecom.com,555-0888,2023-01-20T10:00:00,350.75\n5,eve@ecom.com,555-0105,2023-01-18T10:00:00,99.99\n' > /home/user/ecom_data.csv

RUN chown -R user:user /home/user

# Switch to user
# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
