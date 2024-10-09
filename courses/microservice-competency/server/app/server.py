from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# Simulated database
customers = {}

class Customer:
    def __init__(self, name, email, phone):
        self.id = str(uuid4())
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

# CRUD Operations

@app.route('/customers', methods=['POST'])
def create_customer():
    """
    Create a new customer.
    JSON payload should contain name, email, and phone number.
    """
    if not request.json or 'name' not in request.json or 'email' not in request.json or 'phone' not in request.json:
        return jsonify({"error": "Invalid JSON or missing fields"}), 400
    
    customer = Customer(request.json['name'], request.json['email'], request.json['phone'])
    customers[customer.id] = customer
    
    return jsonify(customer.to_dict()), 201

@app.route('/customers', methods=['GET'])
def get_customers():
    """
    Retrieve all customers
    """
    customer_list = []
    for customer in customers.values():
        customer_list.append(customer.to_dict())

    return jsonify(customer_list)

# @app.route('/customers/<customer_id>', methods=['GET'])
# def get_customer(customer_id):
#     """
#     Retrieve customer by ID.
#     """
#     pass
    

# @app.route('/customers/<customer_id>', methods=['PUT'])
# def update_customer(customer_id):
#     """
#     Update an existing customer.
#     """
#     pass

# @app.route('/customers/<customer_id>', methods=['DELETE'])
# def delete_customer(customer_id):
#     """
#     Delete a customer.
#     """
#     pass

if __name__ == '__main__':
    app.run(debug=True)