import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'Areeba',
    'roll': 1,
    'city': 'Lahore'
}

json_data = json.dumps(data)

# POST request with JSON headers
response = requests.post(url=URL, data=json_data, headers={'Content-Type': 'application/json'})

try:
    # Try to parse JSON response
    print(response.json())
except json.JSONDecodeError:
    print("❌ Failed to decode JSON.")
    print("Status Code:", response.status_code)

    print("Raw response text:", response.text)
