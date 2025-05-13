import json
import os

# Print the current working directory for debugging purposes
print(f"Current working directory: {os.getcwd()}")

# Helper function to load JSON safely
def load_json_file(file_path):
    try:
        with open(file_path, encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        exit(1)

# Corrected path to the data folder in the root of the project
data_file_path = 'data/sdk_api_list.json'  # Adjusted path to the 'data' folder in the root
data = load_json_file(data_file_path)

# Print the report
print("=== SDK/API Report ===")
for item in data:
    print(f"{item.get('name', 'N/A')} (v{item.get('version', 'N/A')}) by {item.get('business_entity', 'N/A')}")
    print(f"Purpose: {item.get('purpose', 'N/A')}")
    print(f"Platforms: {item.get('supported_platforms', 'N/A')} | License: {item.get('license', 'N/A')}")
    print("-" * 40)
