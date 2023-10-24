from flask import render_template, request, redirect, url_for
import requests
from app import app
from models import Loan

BNI_API_KEY = 'your_bni_api_key'  

@app.route('/disburse', methods=['POST'])
def disburse():
    loan_id = request.form['loan_id']
    loan = Loan.query.get(loan_id)
    
    if not loan.approved:
        return "Loan not approved"

    amount = loan.amount
    borrower_bank_account = loan.borrower.bank_account  # You should have this in your User model

    # Construct the disbursement request to BNI Bank API
    disbursement_data = {
        "api_key": BNI_API_KEY,
        "amount": amount,
        "bank_account": borrower_bank_account,
    }

    # Send the disbursement request to BNI Bank API
    response = requests.post('https://bni-bank-api-url.com/disburse', json=disbursement_data)

    if response.status_code == 200:
        # Update the loan status to mark it as disbursed
        loan.disbursed = True
        db.session.commit()
        return "Disbursement successful"
    else:
        return "Disbursement failed"

# Implement error handling and confirmation messages
