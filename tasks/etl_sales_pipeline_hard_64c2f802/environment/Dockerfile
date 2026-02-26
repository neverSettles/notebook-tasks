FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y tmux python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install pytest pandas openpyxl jupyter nbconvert

RUN useradd -m -d /home/user -s /bin/bash user

RUN printf 'txn_date,store_id,item_code,revenue,expenses\n2023-01-01,S1,A,$1,000.50,400.00\n01/02/2023,S2,B,$500.00,\n2023-01-03,S1,B,$600.00,300.00\n01/04/2023,S3,A,$800.00,900.00\n2023-01-05,S4,C,$1,200.00,\n2023-01-06,S2,C,$300.00,100.00\n01/07/2023,S3,B,$700.00,200.00\n2023-01-08,S1,C,$1,500.00,500.00\n01/09/2023,S5,A,$900.00,400.00\n' > /home/user/raw_sales.csv

RUN printf '{\n    "S1": "North",\n    "S2": "South",\n    "S3": "East",\n    "S4": "West"\n}\n' > /home/user/store_regions.json

RUN chown -R user:user /home/user

# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
