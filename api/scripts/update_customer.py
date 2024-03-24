import requests 
import json

id = 1

api_url = f'http://localhost:8000/api/customers/{id}/'

customer_data = {
    'name': 'Customer XXXXX',
    'email': 'customer@newemail.com',
    'phone_number': '123456789'
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.put(api_url, data=json.dumps(customer_data), headers=headers)

if response.status_code == 200:
    print("Customer Updated successfully")
else:
    print("Error updating customer")
