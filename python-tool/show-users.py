#!/usr/bin/env python3

# this script is used to share how many users there are in the HPC who are running jobs
# author: fyuewen@gmail.com
import subprocess

# Run the squeue command
output = subprocess.check_output(['squeue']).decode('utf-8')

# Split the output by lines and skip the header
lines = output.strip().split('\n')[1:]

# Create a dictionary to store the count of each user
user_count = {}

# Iterate through each line of output
for line in lines:
    # Split the line into columns
    columns = line.split()

    # Get the user name
    user_name = columns[4]

    # Update the user count dictionary
    user_count[user_name] = user_count.get(user_name, 0) + 1

# Sort the user count dictionary by count of jobs in descending order
sorted_user_count = dict(sorted(user_count.items(), key=lambda item: item[1], reverse=True))

# Print the user name and count
for user_name, count in sorted_user_count.items():
    print(f"{user_name}: {count}")

