import json       # Imports the json module to read and parse JSON files
import os         # Imports the os module for interacting with the operating system

# Print the current working directory for debugging purposes
print(f"Current working directory: {os.getcwd()}")
# This helps confirm the script is running in the expected directory, useful for file path debugging

# Helper function to load JSON safely
def load_json_file(file_path):
    try:
        # Tries to open the specified JSON file using UTF-8 encoding
        with open(file_path, encoding='utf-8') as f:
            return json.load(f)  # Parses and returns the JSON data as a Python object
    except Exception as e:
        # If an error occurs (file not found, bad JSON syntax, etc.), print the error
        print(f"Error loading JSON file: {e}")
        exit(1)  # Exit the script with a non-zero exit code indicating failure

# Corrected path to the data folder in the root of the project
data_file_path = 'data/sdk_api_list.json'  # Relative path to the JSON file

# Load the data from the JSON file using the helper function
data = load_json_file(data_file_path)

# Print a formatted report based on the JSON data
print("=== SDK/API Report ===")
for item in data:
    # Print the name and version of the SDK/API, with fallback 'N/A' if missing
    print(f"{item.get('name', 'N/A')} (v{item.get('version', 'N/A')}) by {item.get('business_entity', 'N/A')}")
    
    # Print the purpose of the SDK/API
    print(f"Purpose: {item.get('purpose', 'N/A')}")
    
    # Print supported platforms and license type
    print(f"Platforms: {item.get('supported_platforms', 'N/A')} | License: {item.get('license', 'N/A')}")
    
    # Print a separator line for readability
    print("-" * 40)
