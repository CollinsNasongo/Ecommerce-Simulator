from flask import Blueprint, jsonify, request, render_template
from app.utils import user_registration, user_purchase, clear_test_data
from app.models import db, User, UserDemographics, Order, Product, Category
from app.stream_simulator import simulate_user_activity_stream

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return jsonify({'message': 'Welcome to the E-commerce Simulator API'})


@main.route('/docs')
def swagger_ui():
    return render_template('swaggerui.html')

# -------------------- USERS --------------------
@main.route('/users', methods=['POST'])
def create_user():
    user = user_registration()
    return jsonify({
        'message': 'User registered successfully.',
        'user': {
            'user_id': user.user_id,
            'name': user.name,
            'email': user.email,
            'phone_number': user.phone_number,
            'address': user.address,
            'created_at': user.created_at.isoformat()
        }
    }), 201

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'user_id': u.user_id,
        'name': u.name,
        'email': u.email
    } for u in users])

@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'user_id': user.user_id,
        'name': user.name,
        'email': user.email,
        'phone_number': user.phone_number,
        'address': user.address
    })

@main.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': f'User {user_id} deleted.'})

# -------------------- USER DEMOGRAPHICS --------------------
@main.route('/users/<int:user_id>/demographics', methods=['GET'])
def get_demographics(user_id):
    demo = UserDemographics.query.get_or_404(user_id)
    return jsonify({
        'age': demo.age,
        'gender': demo.gender,
        'city': demo.city,
        'state': demo.state,
        'country': demo.country,
        'zip_code': demo.zip_code
    })

@main.route('/users/<int:user_id>/demographics', methods=['PUT'])
def update_demographics(user_id):
    demo = UserDemographics.query.get_or_404(user_id)
    data = request.json

    demo.age = data.get('age', demo.age)
    demo.gender = data.get('gender', demo.gender)
    demo.city = data.get('city', demo.city)
    demo.state = data.get('state', demo.state)
    demo.country = data.get('country', demo.country)
    demo.zip_code = data.get('zip_code', demo.zip_code)

    db.session.commit()
    return jsonify({'message': 'Demographics updated successfully.'})

# -------------------- ORDERS --------------------
@main.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{
        'order_id': o.order_id,
        'user_id': o.user_id,
        'total_price': o.total_price,
        'status': o.status
    } for o in orders])

@main.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify({
        'order_id': order.order_id,
        'user_id': order.user_id,
        'total_price': order.total_price,
        'status': order.status
    })

@main.route('/orders/user/<int:user_id>', methods=['GET'])
def get_orders_by_user(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'order_id': o.order_id,
        'total_price': o.total_price,
        'status': o.status
    } for o in orders])

# -------------------- PRODUCTS --------------------
@main.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        'product_id': p.product_id,
        'name': p.name,
        'description': p.description,
        'price': p.price,
        'stock_qty': p.stock_qty,
        'category': p.category.name if p.category else None
    } for p in products])

@main.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({
        'product_id': product.product_id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock_qty': product.stock_qty,
        'category': product.category.name if product.category else None
    })

@main.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        stock_qty=data.get('stock_qty', 0),
        category_id=data['category_id']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created.', 'product_id': product.product_id}), 201

@main.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': f'Product {product_id} deleted.'})

# -------------------- CATEGORIES --------------------
@main.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{
        'category_id': c.category_id,
        'name': c.name,
        'description': c.description
    } for c in categories])

@main.route('/categories', methods=['POST'])
def create_category():
    data = request.json
    category = Category(
        name=data['name'],
        description=data.get('description')
    )
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Category created.', 'category_id': category.category_id}), 201

@main.route('/categories/<int:category_id>/products', methods=['GET'])
def get_category_products(category_id):
    category = Category.query.get_or_404(category_id)
    return jsonify([{
        'product_id': p.product_id,
        'name': p.name,
        'price': p.price
    } for p in category.products])

# -------------------- SIMULATION --------------------
@main.route('/simulate_purchase', methods=['POST'])
def simulate_purchase():
    order = user_purchase()
    if isinstance(order, str):
        return jsonify({'message': order}), 400
    return jsonify({
        'message': 'Purchase simulated successfully.',
        'order': {
            'order_id': order.order_id,
            'user_id': order.user_id,
            'total_price': order.total_price,
            'status': order.status
        }
    }), 201

@main.route('/clear_test_data', methods=['DELETE'])
def api_clear_test_data():
    message = clear_test_data()
    return jsonify({'message': message})


@main.route('/simulate_user_activity', methods=['POST'])
def run_stream():
    max_events = int(request.args.get('max_events', 10))
    interval = float(request.args.get('interval_seconds', 1))

    simulate_user_activity_stream(interval_seconds=interval, max_events=max_events)

    return jsonify({'message': f'Simulated {max_events} events at {interval}s interval'})