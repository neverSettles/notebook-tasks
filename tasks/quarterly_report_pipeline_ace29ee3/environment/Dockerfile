FROM ubuntu:22.04

RUN apt-get update && apt-get install -y tmux \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pytest pandas numpy jupyter nbconvert beautifulsoup4

RUN useradd -ms /bin/bash user

# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user

RUN printf 'id,date,feedback,agent_id\n1,2023-10-01,"<p>Great service by agent! Contact me at john.doe@email.com.</p>",101\n2,2023-10-15,"The product is <b>ok</b>. My phone is 555-123-4567. &lt;3",102\n3,2023-11-02,"<div><span>Awful experience</span></div>. refund requested.",101\n4,2023-11-20,"café was closed. Email: test@test.org!",103\n5,2023-12-05,"<script>alert('\''xss'\'')</script> No comment",102\n' > /home/user/raw_feedback.csv

RUN printf '[\n    {"agent_id": 101, "revenue": 5000},\n    {"agent_id": 102, "revenue": 3000},\n    {"agent_id": 103, "revenue": 1500}\n]\n' > /home/user/sales.json

