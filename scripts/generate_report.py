import json

with open('../data/sdk_api_list.json') as f:
    data = json.load(f)

print("=== SDK/API Report ===")
for item in data:
    print(f"{item['name']} (v{item['version']}) by {item['business_entity']}")
    print(f"Purpose: {item['purpose']}")
    print(f"Platforms: {item.get('supported_platforms', 'N/A')} | License: {item.get('license', 'N/A')}")
    print("-" * 40)
