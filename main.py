from flask import Flask, request, jsonify

app = Flask(__name__)

orders_data = [
        {"order_id": 1, "item": "Pancit", "paid": False},
        {"order_id": 2, "item": "Burger", "paid": False},
        {"order_id": 3, "item": "Pizza", "paid": False},
        {"order_id": 4, "item": "Fries", "paid": False},
        {"order_id": 5, "item": "Pasta", "paid": False},
        ]

#Endpoint 1
#Endpoint 2
#Endpoint 3
#Endpoint 4

if __name__ == '__main__':
    app.run(debug=True)