from flask import render_template, request, redirect, url_for
from app import app
from bni_integration import initiate_disbursement

@app.route('/disburse', methods=['POST'])
def disburse():
    # This route initiates the disbursement to the borrower's bank using BNI Bank's API.
    
    # Fetch the loan details from the database, including the borrower's bank account information.
    loan_id = request.form['loan_id']
    loan = Loan.query.get(loan_id)
    
    # You would need to provide a function to get the necessary bank account information from the user.
    # For security reasons, this typically involves additional verification and confirmation steps.
    bank_account = get_borrower_bank_account(loan.borrower)

    # Initiate the disbursement using the BNI API
    success, message = initiate_disbursement(bank_account, loan.amount)

    if success:
        # Update the loan status upon successful disbursement
        loan.approved = True
        db.session.commit()
        return redirect(url_for('loan_listing'))
    else:
        # Handle disbursement errors and show appropriate messages to the user
        return render_template('disbursement.html', error_message=message)

# Implement error handling and confirmation messages
