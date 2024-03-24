import requests
import json

response = requests.post(url = api_url,
                        data = json.dumps(customer_data),
                        headers = {'Content-Type':'application-json'})

customer_data = {
    "name":"Customer X",
    "email": "Customerx@email.com",
    "phone_number": "000-000-0000"
    }
    
data = json.dumps(customer_data)