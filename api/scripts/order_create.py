import requests
import json

api_url = 'http://localhost:8000/api/orders/'

order_data = {
    "order":"order X",
    "quantity": "0",
    "cost": "00.00"
    }

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(api_url, data=json.dumps(order_data), headers=headers)

if response.status_code == 201:
    print("Order Created Successfully")
else:
    print("Error Creating order")
