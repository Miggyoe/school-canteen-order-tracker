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
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()

    if not data or "item" not in data:
        return jsonify({"error": "Missing item"}), 400

    new_order = {
        "order_id": len(orders_data) + 1,
        "item": data["item"],
        "paid": data.get("paid", False)
    }
    orders_data.append(new_order)
    return jsonify({"message": f"Order {new_order['order_id']} created"}), 201

#Endpoint 4
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    for order in orders_data:
        if order["order_id"] == order_id:
            orders_data.remove(order)
            return jsonify({"message": f"Order {order_id} deleted"}), 200
    return jsonify({"error": f"Order {order_id} not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)