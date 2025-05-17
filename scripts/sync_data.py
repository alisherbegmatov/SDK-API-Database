import csv       # Imports the csv module to read from and write to CSV files
import json      # Imports the json module to load and parse JSON data
import os        # Imports the os module to interact with the operating system

# Print current working directory for debugging purposes
print(f"Current working directory: {os.getcwd()}")
# Prints the current directory where the script is running to help locate files correctly

# Helper function to load JSON safely
def load_json_file(file_path):
    try:
        # Tries to open the file in read mode with UTF-8 encoding
        with open(file_path, encoding='utf-8') as f:
            return json.load(f)  # Parses and returns the JSON content as a Python object
    except Exception as e:
        # If there's an error (e.g. file not found or JSON syntax error), print it
        print(f"Error loading JSON file: {e}")
        exit(1)  # Exit the script with an error code

# Function to extract name and version info and save to CSV
def sync_versions():
    # Load the JSON data from the specified file
    json_data = load_json_file('data/sdk_api_list.json')  # Corrected path

    # Open a CSV file in write mode, creating it if it doesn't exist
    with open('data/sdk_api_versions.csv', 'w', newline='') as vf:
        writer = csv.writer(vf)  # Create a CSV writer object
        writer.writerow(['name', 'version'])  # Write the CSV header row
        for entry in json_data:
            # For each entry in the JSON, write a row with name and version
            writer.writerow([entry.get('name', 'N/A'), entry.get('version', 'N/A')])

# Function to extract name, supported platforms, and license info and save to CSV
def sync_metadata():
    # Load the JSON data again (same file as above)
    json_data = load_json_file('data/sdk_api_list.json')  # Corrected path

    # Open a second CSV file to write metadata
    with open('data/sdk_api_metadata.csv', 'w', newline='') as mf:
        writer = csv.writer(mf)  # Create a CSV writer object
        writer.writerow(['name', 'supported_platforms', 'license'])  # Write header
        for entry in json_data:
            # Write a row with name, supported platforms, and license info
            writer.writerow([
                entry.get('name', 'N/A'),
                entry.get('supported_platforms', 'N/A'),
                entry.get('license', 'N/A')
            ])

# Main block: runs when script is executed directly (not imported)
if __name__ == "__main__":
    sync_versions()       # Call function to generate sdk_api_versions.csv
    sync_metadata()       # Call function to generate sdk_api_metadata.csv
    print("Database sync complete.")  # Inform user that both CSVs were generated
