import requests 
import json

id = 1

api_url = f'http://localhost:8000/api/orders/{id}/'

order_data = {
    "order":"order X",
    "quantity": "0",
    "cost": "00.00"
    }

headers = {
    'Content-Type': 'application/json'
}

response = requests.put(api_url, data=json.dumps(order_data), headers=headers)

if response.status_code == 200:
    print("Order Updated successfully")
else:
    print("Error updating order")
