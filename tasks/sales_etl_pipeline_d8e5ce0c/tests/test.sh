#!/bin/bash
# Harbor test wrapper script
# Runs pytest and writes reward to /logs/verifier/reward.txt

cd /tests

# Run pytest and capture exit code
python3 -m pytest -q test.py
exit_code=$?

# Write reward based on test result
mkdir -p /logs/verifier
if [ $exit_code -eq 0 ]; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
fi

exit $exit_code
