import requests

# BNI API endpoint for disbursement
url = 'https://api.bni.co.id/disbursement'

# Your BNI API credentials
api_key = 'your_api_key'
access_token = 'your_access_token'

# Disbursement request data
data = {
    'loan_id': '12345',
    'borrower_name': 'John Doe',
    'bank_account': '1234567890',
    'amount': 1000.00,
}

# Set headers with API credentials
headers = {
    'Api-Key': api_key,
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

# Send the disbursement request
response = requests.post(url, json=data, headers=headers)

# Handle the response
if response.status_code == 200:
    print('Disbursement request successful')
    print('Response:', response.json())
else:
    print('Disbursement request failed')
    print('Error:', response.text)
