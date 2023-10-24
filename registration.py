# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loan_app.db'
db = SQLAlchemy(app)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    # Additional customer details and relationships

# API endpoint for customer registration
@app.route('/register', methods=['POST'])
def register_customer():
    data = request.get_json()
    name = data['name']
    email = data['email']

    new_customer = Customer(name=name, email=email)
    db.session.add(new_customer)
    db.session.commit()
    
    return jsonify({"message": "Customer registered successfully"})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
