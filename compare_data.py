import sys
import requests
import json

# Retrieve values from the source endpoint
def get_source(src_endpoint, src_key):
    try:
        resp = requests.get(src_endpoint)
        resp.raise_for_status()

        data = resp.json()

        # Extract the values corresponding to src_key from each item
        src_values = [item[src_key] for item in data]
        return src_values
    except requests.exceptions.RequestException as e:
        print(f"Error - Unable to fetch data from the source endpoint: {e}")
        sys.exit(1)
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error - Invalid JSON data or key error in the source endpoint: {e}")
        sys.exit(1)

# Compare values from the source with values from a compared endpoint
def compare(src_values, compared_endpoint, compared_key):
    try:
        resp = requests.get(compared_endpoint)
        resp.raise_for_status()

        data = resp.json()

        # Extract the values corresponding to compared_key from each item
        src_values = [item[compared_key] for item in data]
        
        not_matched = set()
        # Iterate over compared values and check if each value is present in source values
        for x in compared_values:
            if x not in src_values and x not in not_matched:
                not_matched.add(x)

        print(list(not_matched))
    except requests.exceptions.RequestException as e:
        print(f"Error - Unable to fetch data from the compared endpoint: {e}")
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error - Invalid JSON data or key error in the compared endpoint: {e}")
        sys.exit(1)

"""
Retrieve command-line arguments and call the functions with the provided arguments
sys.argv[1:4] = [source endpoint, source key, endpoint to be compared, key to be compared]
"""
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python compare_data.py <source_endpoint> <source_key> <compared_endpoint> <compared_key>")
        sys.exit(1)

    src = get_source(sys.argv[1], sys.argv[2])
    compare(src, sys.argv[3], sys.argv[4])