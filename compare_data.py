import sys
import requests

# Retrieve values from the source endpoint
def get_source(src_endpoint, src_key):
    resp = requests.get(src_endpoint)

    if resp.status_code == 200:
        data = resp.json()

        # Extract the values corresponding to src_key from each item
        src_values = [item[src_key] for item in data]
        return src_values
    else:
        print(f"Err: {resp.status_code}")

# Compare values from the source with values from a compared endpoint
def compare(src_values, compared_endpoint, compared_key):
    resp = requests.get(compared_endpoint)

    if resp.status_code == 200:
        data = resp.json()

        # Extract the values corresponding to compared_key from each item
        compared_values = [item[compared_key] for item in data]

        not_matched = set()
        # Iterate over compared_values and check if each value is present in src_values
        for x in compared_values:
            if x not in src_values and x not in not_matched:
                not_matched.add(x)
        
        print(list(not_matched))
    else:
        print(f"Err: {resp.status_code}")

"""
Retrieve command-line arguments and call the functions with the provided arguments
sys.argv[1:4] = [source endpoint, source key, endpoint to be compared, key to be compared]
"""
src = get_source(sys.argv[1], sys.argv[2])
compare(src, sys.argv[3], sys.argv[4])