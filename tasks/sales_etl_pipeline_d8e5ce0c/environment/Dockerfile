FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y tmux python3 python3-pip && \
    pip3 install pytest jupyter nbconvert pandas && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash user

RUN printf 'Store_ID,Region,2023-01-01,2023-01-02,2023-02-01,2023-02-02\nS1,North,100.0,150.0,200.0,250.0\nS2,South,300.0,100.0,400.0,150.0\nS3,East,150.0,,250.0,300.0\n' > /home/user/raw_sales.csv

RUN chown -R user:user /home/user

# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
