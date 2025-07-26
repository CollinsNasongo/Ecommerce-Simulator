from flask import Blueprint, jsonify
from app.utils import  user_registration, user_purchase
from app.models import User, Order

main = Blueprint('main', __name__)

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'user_id': u.user_id, 'name': u.name, 'email': u.email} for u in users])

@main.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{'order_id': o.order_id, 'user_id': o.user_id, 'total_price': o.total_price, 'status': o.status} for o in orders])

@main.route('/register_user', methods=['GET'])
def register_user():
    user = user_registration()
    return jsonify({
        'message': 'User registered successfully.',
        'user': {
            'user_id': user.user_id,
            'name': user.name,
            'email': user.email,
            'phone_number': user.phone_number,
            'address': user.address,
        }
    })

@main.route('/simulate_purchase', methods=['GET'])
def simulate_purchase():
    order = user_purchase()
    if isinstance(order, str):  # If the function returns an error message
        return jsonify({'message': order}), 400
    return jsonify({
        'message': 'Purchase simulated successfully.',
        'order': {
            'order_id': order.order_id,
            'user_id': order.user_id,
            'total_price': order.total_price,
            'status': order.status,
        }
    })