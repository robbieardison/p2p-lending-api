from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///p2p_loan.db'  # Use a real database in production
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'your_secret_key'

# Import routes and other components

if __name__ == '__main__':
    app.run(debug=True)
