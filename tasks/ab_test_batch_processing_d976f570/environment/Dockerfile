FROM ubuntu:22.04

# Avoid tzdata interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install python packages
RUN pip3 install scipy matplotlib pytest pandas jupyter

# Create user
RUN useradd -m -s /bin/bash user

# Create data directory and files
RUN mkdir -p /home/user/data

RUN echo "user_id,group,converted\n1,control,0\n2,treatment,1\n3,control,1\n4,treatment,0" > /home/user/data/campaign_day_1.csv
RUN echo "user_id,group,converted\n5,control,0\n6,control,0\n7,treatment,1\n8,treatment,1" > /home/user/data/campaign_day_2.csv
RUN echo "<html><body>502 Bad Gateway</body></html>" > /home/user/data/campaign_day_3.csv

# Change ownership
RUN chown -R user:user /home/user

# Switch to user
# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
