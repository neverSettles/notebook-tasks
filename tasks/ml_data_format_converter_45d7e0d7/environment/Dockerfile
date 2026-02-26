FROM ubuntu:22.04

# Avoid tzdata prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and necessary packages
RUN apt-get update && \
    apt-get install -y tmux python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install required Python libraries
RUN pip3 install --no-cache-dir pandas openpyxl jupyter matplotlib numpy scikit-learn seaborn pytest

# Create user 'user'
RUN useradd -m -s /bin/bash user

# Create initial data files
RUN echo "store_id,store_type,profit_label\n\
1,Retail,1\n\
2,Warehouse,0\n\
3,Retail,1\n\
4,Online,1\n\
5,Warehouse,0" > /home/user/store_data.csv && \
    echo '[\
{"store_id": 1, "region": "North"}, \
{"store_id": 2, "region": "South"}, \
{"store_id": 3, "region": "East"}, \
{"store_id": 4, "region": "West"}, \
{"store_id": 5, "region": "North"}\
]' > /home/user/region_data.json

# Generate Excel file using Python
RUN python3 -c "import pandas as pd; pd.DataFrame({'store_id': [1, 2, 3, 4, 5], 'top_category': ['Electronics', 'Furniture', 'Clothing', 'Electronics', 'Groceries']}).to_excel('/home/user/product_data.xlsx', index=False)"

# Ensure proper ownership
RUN chown -R user:user /home/user

# Switch to the user
# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user
