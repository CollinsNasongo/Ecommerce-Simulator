from flask import Blueprint, jsonify
from app.utils import user_registration, user_purchase
from app.models import User, Order

main = Blueprint("main", __name__)

@main.route("/register_user", methods=["GET"])
def register_user():
    user = user_registration()
    return jsonify({
        "user_id": user.user_id,
        "name": user.name,
        "email": user.email
    }), 201

@main.route("/simulate_purchase", methods=["GET"])
def simulate_purchase(): 
    result = user_purchase()
    if isinstance(result, str):
        return jsonify({"error": result}), 400
    return jsonify({
        "order_id": result.order_id,
        "user_id": result.user_id,
        "total_price": str(result.total_price),
        "status": result.status
    }), 201

@main.route("/users", methods=["GET"])
def get_users():
    return jsonify([
        {"user_id": u.user_id, "name": u.name, "email": u.email}
        for u in User.query.all()
    ])

@main.route("/orders", methods=["GET"])
def get_orders():
    return jsonify([
        {"order_id": o.order_id, "user_id": o.user_id, "total_price": str(o.total_price)}
        for o in Order.query.all()
    ])
