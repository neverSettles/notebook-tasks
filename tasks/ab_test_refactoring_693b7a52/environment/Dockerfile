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
RUN printf 'user_id,group,converted\n1,control,0\n2,treatment,1\n3,control,0\n4,treatment,0\n5,control,1\n6,treatment,1\n7,control,0\n8,treatment,1\n9,control,0\n10,treatment,0\n11,control,0\n12,treatment,1\n13,control,0\n14,treatment,0\n15,control,0\n16,treatment,1\n17,control,1\n18,treatment,0\n19,control,0\n20,treatment,1\n' > /home/user/campaign_data.csv

# Create the messy python script
RUN printf 'import pandas as pd\nimport numpy as np\nfrom scipy.stats import chi2_contingency\nimport matplotlib.pyplot as plt\ndata = pd.read_csv('\''campaign_data.csv'\'')\nsummary = data.groupby('\''group'\'').agg(Total_Visitors=('\''user_id'\'', '\''count'\''), Converted=('\''converted'\'', '\''sum'\'')).reset_index()\nsummary['\''Conversion_Rate'\''] = summary['\''Converted'\''] / summary['\''Total_Visitors'\'']\ncontingency_table = pd.crosstab(data['\''group'\''], data['\''converted'\''])\nchi2, p, dof, expected = chi2_contingency(contingency_table)\nprint(f"P-value: {p}")\nplt.bar(summary['\''group'\''], summary['\''Conversion_Rate'\''], color=['\''blue'\'', '\''orange'\''])\nplt.title('\''Conversion Rate by Group'\'')\nplt.ylabel('\''Conversion Rate'\'')\nplt.savefig('\''conversion_plot.png'\'')\nsummary.to_csv('\''summary_stats.csv'\'', index=False)\n' > /home/user/messy_ab_test.py
