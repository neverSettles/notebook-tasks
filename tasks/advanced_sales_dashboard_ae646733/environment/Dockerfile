FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir pytest pandas numpy jupyter matplotlib seaborn

RUN useradd -m -s /bin/bash user

# Create initial data files
RUN cat <<EOF > /home/user/sales_data.csv
Date,OrderID,Product,Quantity,UnitPrice,Currency
2023-01-01,1,A,10,100.0,EUR
01-02-2023,2,B,-5,50.0,USD
2023-01-03,3,A,15,100.0,EUR
2023-01-04,4,C,20,20.0,GBP
2023-01-05,5,B,0,50.0,USD
2023-01-05,6,A,10,100.0,EUR
2023-01-06,7,C,5,-10.0,USD
EOF

RUN cat <<EOF > /home/user/exchange_rates.csv
Date,Currency,Rate_to_USD
2022-12-31,EUR,0.95
2023-01-02,EUR,0.90
2023-01-04,GBP,0.80
2022-12-31,USD,1.0
EOF

RUN chown -R user:user /home/user

# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
