import requests
import json

api_url = 'http://localhost:8000/api/customers/'

customer_data = {
    "name": "Customer X",
    "email": "customerx@email.com",
    "phone_number": "000-000-0000"
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(api_url, data=json.dumps(customer_data), headers=headers)

if response.status_code == 201:
    print("Customer Created Successfully")
else:
    print("Error Creating Customer")
