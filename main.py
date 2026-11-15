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
#Create
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
#Endpoint 2
#Endpoint 3
#Endpoint 4

if __name__ == '__main__':
    app.run(debug=True)