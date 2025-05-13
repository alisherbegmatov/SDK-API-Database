import csv
import json
import os

# Print current working directory for debugging purposes
print(f"Current working directory: {os.getcwd()}")

# Helper function to load JSON safely
def load_json_file(file_path):
    try:
        with open(file_path, encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        exit(1)

def sync_versions():
    json_data = load_json_file('data/sdk_api_list.json')  # Corrected path

    with open('data/sdk_api_versions.csv', 'w', newline='') as vf:
        writer = csv.writer(vf)
        writer.writerow(['name', 'version'])
        for entry in json_data:
            writer.writerow([entry.get('name', 'N/A'), entry.get('version', 'N/A')])

def sync_metadata():
    json_data = load_json_file('data/sdk_api_list.json')  # Corrected path

    with open('data/sdk_api_metadata.csv', 'w', newline='') as mf:
        writer = csv.writer(mf)
        writer.writerow(['name', 'supported_platforms', 'license'])
        for entry in json_data:
            writer.writerow([
                entry.get('name', 'N/A'),
                entry.get('supported_platforms', 'N/A'),
                entry.get('license', 'N/A')
            ])

if __name__ == "__main__":
    sync_versions()
    sync_metadata()
    print("Database sync complete.")
