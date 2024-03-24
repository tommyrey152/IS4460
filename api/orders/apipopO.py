import requests
import json

response = requests.post(url = api_url,
                        data = json.dumps(order_data),
                        headers = {'Content-Type':'application-json'})

order_data = {
    "order":"order X",
    "quantity": "0",
    "cost": "00.00"
    }
    
data = json.dumps(order_data)