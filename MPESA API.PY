import requests
import json

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

r = requests.get(api_url, auth=(consumer_key, consumer_secret))

access_token = json.loads(r.text)['access_token']

api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

headers = {'Authorization': 'Bearer ' + access_token}

request = {
    "BusinessShortCode": "",
    "Password": "",
    "Timestamp": "",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "",
    "PartyA": "",
    "PartyB": "",
    "PhoneNumber": "",
    "CallBackURL": "",
    "AccountReference": "",
    "TransactionDesc": ""
}

response = requests.post(api_url, json=request, headers=headers)

print(response.text)
