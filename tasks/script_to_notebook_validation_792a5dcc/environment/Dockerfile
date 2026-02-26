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
RUN printf 'import pandas as pd\nimport numpy as np\n\nnp.random.seed(42)\ncategories = ['\''Electronics'\'', '\''Clothing'\'', '\''Home'\'']\ndata = {\n    '\''item_id'\'': range(1, 101),\n    '\''category'\'': np.random.choice(categories, 100),\n    '\''price'\'': np.random.uniform(10, 100, 100),\n    '\''discount'\'': np.random.uniform(0, 0.3, 100)\n}\ndf = pd.DataFrame(data)\ndf['\''discounted_price'\''] = df['\''price'\''] * (1 - df['\''discount'\''])\nsummary = df.groupby('\''category'\'')['\''discounted_price'\''].sum().reset_index()\nsummary.to_csv('\''/home/user/final_sales_summary.csv'\'', index=False)\n' > /home/user/prototype_sales_calc.py

# Set ownership
RUN chown -R user:user /home/user

# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user