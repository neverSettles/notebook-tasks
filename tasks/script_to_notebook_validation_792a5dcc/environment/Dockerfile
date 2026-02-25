FROM ubuntu:22.04

# Avoid tzdata prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip sudo && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies required for the task
RUN pip3 install pytest pandas numpy jupyter nbconvert

# Create user 'user'
RUN useradd -m -s /bin/bash user

# Create the prototype script
RUN cat <<'EOF' > /home/user/prototype_sales_calc.py
import pandas as pd
import numpy as np

np.random.seed(42)
categories = ['Electronics', 'Clothing', 'Home']
data = {
    'item_id': range(1, 101),
    'category': np.random.choice(categories, 100),
    'price': np.random.uniform(10, 100, 100),
    'discount': np.random.uniform(0, 0.3, 100)
}
df = pd.DataFrame(data)
df['discounted_price'] = df['price'] * (1 - df['discount'])
summary = df.groupby('category')['discounted_price'].sum().reset_index()
summary.to_csv('/home/user/final_sales_summary.csv', index=False)
EOF

# Set ownership
RUN chown -R user:user /home/user

# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user