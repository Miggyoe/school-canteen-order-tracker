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
@app.route('/orders', methods=['GET'])
def get_all_orders():
    if not orders_data:
        return jsonify({"message": "No orders found"}), 404
    return jsonify(orders_data), 200

#Endpoint 2
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_single_order(order_id):
    for order in orders_data:
        if order["order_id"] == order_id:
            return jsonify(order), 200
    return jsonify({"error": "Order not found"}), 404

#Endpoint 3
#Endpoint 4

if __name__ == '__main__':
    app.run(debug=True)