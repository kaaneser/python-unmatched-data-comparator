# Python Unmatched Data Comparator 🐍

This repository contains source code that retrieves data from a source endpoint, compares it with data from a compared endpoint, and prints the unmatched values.

## Prerequisites

Before running the code, make sure you have the following prerequisites

- Python 3 installed
- requests module installed (you can install it using `pip install requests`)

## Usage

To run the code, follow these steps:

1. Clone the repository
2. Open a command-line interface
3. Navigate to the cloned repo's directory
4. Run the following command:
   ```
   python compare_data.py <source_endpoint> <source_key> <compared_endpoint> <compared_key>

   Replace the data with the related information.
   For example:
   python compare_data.py https://api.example.com/source-data src_items https://api.example.com/compared-data compared_items
   ```
5. The code will retrieve the data from the source and compared endpoint, compare them and print the unmatched values.

## To-Do's 🏁

1. Implement error handling for invalid URLs or non-JSON responses. ✔️
2. Add logging functionality
3. Implement unit tests
4. Enhance the code to handle pagination or large datasets incorparating pagination parameters in the API requests
5. Add support for authentication if endpoints require authentication or api keys.
6. Improve code modularity
7. Implement caching mechanism to store and reuse retrieved data
8. Create CLI for easier interaction