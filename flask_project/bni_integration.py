# This file contains functions for interacting with BNI Bank's API for disbursements.

import requests
from app import app

# BNI Bank's API endpoint for disbursement
BNI_API_URL = 'https://api.bni.co.id'

def initiate_disbursement(bank_account, amount):
    # This function sends a disbursement request to BNI Bank's API.
    # 'bank_account' should contain the recipient's bank account information.
    
    # Authenticate with the BNI API using your API key from config.py
    headers = {
        'Authorization': 'Bearer ' + app.config['BNI_API_KEY'],
        'Content-Type': 'application/json'
    }

    # Create a disbursement request payload
    disbursement_data = {
        'account_number': bank_account['account_number'],
        'amount': amount
        # Include other necessary data as per BNI Bank's API documentation
    }

    # Send the disbursement request
    response = requests.post(BNI_API_URL + '/disburse', json=disbursement_data, headers=headers)

    if response.status_code == 200:
        # Disbursement was successful
        return True, 'Disbursement was successful.'
    else:
        # Handle disbursement errors and provide an error message
        return False, 'Disbursement failed. Error: ' + response.text
