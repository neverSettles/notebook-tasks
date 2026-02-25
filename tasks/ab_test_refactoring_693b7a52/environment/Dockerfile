FROM ubuntu:22.04

# Install Python and pip
RUN apt-get update && \
    apt-get install -y tmux python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install required Python packages
RUN pip3 install --no-cache-dir pytest pandas numpy scipy matplotlib jupyter nbconvert

# Create a non-root user
RUN useradd -m -s /bin/bash user

# Switch to the new user and set working directory
# Harbor Daytona compatibility: ensure agent/log paths are writable
RUN mkdir -p /installed-agent /logs/agent /logs/verifier /logs/artifacts && \
    chown -R user:user /installed-agent /logs

WORKDIR /home/user

# Create the input CSV file
RUN cat <<'EOF' > /home/user/campaign_data.csv
user_id,group,converted
1,control,0
2,treatment,1
3,control,0
4,treatment,0
5,control,1
6,treatment,1
7,control,0
8,treatment,1
9,control,0
10,treatment,0
11,control,0
12,treatment,1
13,control,0
14,treatment,0
15,control,0
16,treatment,1
17,control,1
18,treatment,0
19,control,0
20,treatment,1
EOF

# Create the messy python script
RUN cat <<'EOF' > /home/user/messy_ab_test.py
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
data = pd.read_csv('campaign_data.csv')
summary = data.groupby('group').agg(Total_Visitors=('user_id', 'count'), Converted=('converted', 'sum')).reset_index()
summary['Conversion_Rate'] = summary['Converted'] / summary['Total_Visitors']
contingency_table = pd.crosstab(data['group'], data['converted'])
chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"P-value: {p}")
plt.bar(summary['group'], summary['Conversion_Rate'], color=['blue', 'orange'])
plt.title('Conversion Rate by Group')
plt.ylabel('Conversion Rate')
plt.savefig('conversion_plot.png')
summary.to_csv('summary_stats.csv', index=False)
EOF
