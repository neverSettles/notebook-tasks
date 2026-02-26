FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y tmux python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install matplotlib pytest pandas jupyter

RUN useradd -m -s /bin/bash user

RUN echo "transaction_id,region,amount,date\n\
1,North,100.50,2023-01-01\n\
2,South,250.00,2023-01-02\n\
3,North,150.25,2023-01-03\n\
4,East,300.00,2023-01-04\n\
5,South,50.00,2023-01-05\n\
6,West,500.00,2023-01-06\n\
7,East,50.00,2023-01-07" > /home/user/raw_sales.csv && \
    chown user:user /home/user/raw_sales.csv

# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
