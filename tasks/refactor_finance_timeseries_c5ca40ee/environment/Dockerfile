FROM ubuntu:22.04

RUN apt-get update && apt-get install -y tmux \
    python3 \
    python3-pip \
    sudo \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir matplotlib pytest pandas jupyter

RUN useradd -m -d /home/user -s /bin/bash user

RUN echo "Date,AAPL,GOOG,MSFT\n\
2023-01-01,150.0,90.0,240.0\n\
2023-01-02,152.0,92.0,242.0\n\
2023-01-03,151.0,91.0,241.0\n\
2023-01-04,155.0,95.0,245.0\n\
2023-01-05,158.0,98.0,250.0" > /home/user/stocks.csv

RUN echo "import pandas as pd\n\
\n\
df = pd.read_csv('stocks.csv')\n\
melted = df.melt(id_vars=['Date'], var_name='Ticker', value_name='Price')\n\
avg_prices = melted.groupby('Ticker')['Price'].mean().reset_index()\n\
avg_prices.to_csv('/home/user/avg_prices.csv', index=False)" > /home/user/process_finance.py

RUN chown -R user:user /home/user

WORKDIR /home/user
# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

