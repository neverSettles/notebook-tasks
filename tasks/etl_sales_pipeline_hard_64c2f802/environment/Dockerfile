FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y tmux python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install pytest pandas openpyxl jupyter nbconvert

RUN useradd -m -d /home/user -s /bin/bash user

RUN cat <<'EOF' > /home/user/raw_sales.csv
txn_date,store_id,item_code,revenue,expenses
2023-01-01,S1,A,$1,000.50,400.00
01/02/2023,S2,B,$500.00,
2023-01-03,S1,B,$600.00,300.00
01/04/2023,S3,A,$800.00,900.00
2023-01-05,S4,C,$1,200.00,
2023-01-06,S2,C,$300.00,100.00
01/07/2023,S3,B,$700.00,200.00
2023-01-08,S1,C,$1,500.00,500.00
01/09/2023,S5,A,$900.00,400.00
EOF

RUN cat <<'EOF' > /home/user/store_regions.json
{
    "S1": "North",
    "S2": "South",
    "S3": "East",
    "S4": "West"
}
EOF

RUN chown -R user:user /home/user

# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
