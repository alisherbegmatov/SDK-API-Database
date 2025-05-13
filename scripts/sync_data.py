import csv
import json

def sync_versions():
    with open('../data/sdk_api_list.json') as jf:
        json_data = json.load(jf)

    with open('../data/sdk_api_versions.csv', 'w', newline='') as vf:
        writer = csv.writer(vf)
        writer.writerow(['name', 'version'])
        for entry in json_data:
            writer.writerow([entry['name'], entry['version']])

def sync_metadata():
    with open('../data/sdk_api_list.json') as jf:
        json_data = json.load(jf)

    with open('../data/sdk_api_metadata.csv', 'w', newline='') as mf:
        writer = csv.writer(mf)
        writer.writerow(['name', 'supported_platforms', 'license'])
        for entry in json_data:
            writer.writerow([
                entry['name'],
                entry.get('supported_platforms', ''),
                entry.get('license', '')
            ])

if __name__ == "__main__":
    sync_versions()
    sync_metadata()
    print("Database sync complete.")
