import json
with open('sample.json', 'r') as f:
    data = json.load(f)
    print(data)
    print(data['store_name'])