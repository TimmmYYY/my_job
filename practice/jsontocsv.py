import csv
import json

# Read JSON file
with open('data/json.json', 'r') as json_file:
    data = json.load(json_file)

# Check if data is an array or an object
if isinstance(data, list):
    # Extract keys from the first object
    keys = data[0].keys()
elif isinstance(data, dict):
    # Extract keys from the object
    keys = data.keys()
else:
    raise ValueError("Invalid JSON data format.")

# Write data to CSV file
with open('out/json.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys)
    writer.writeheader()

    if isinstance(data, list):
        writer.writerows(data)
    elif isinstance(data, dict):
        writer.writerow(data)

print("CSV file created successfully.")
