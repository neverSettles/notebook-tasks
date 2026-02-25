FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y tmux python3 python3-pip && \
    pip3 install pytest jupyter nbconvert pandas && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash user

RUN cat <<'EOF' > /home/user/raw_sales.csv
Store_ID,Region,2023-01-01,2023-01-02,2023-02-01,2023-02-02
S1,North,100.0,150.0,200.0,250.0
S2,South,300.0,100.0,400.0,150.0
S3,East,150.0,,250.0,300.0
EOF

RUN chown -R user:user /home/user

# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
