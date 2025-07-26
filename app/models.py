from app.database import db

# Users Table
class User(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    # Relationships
    demographics = db.relationship('UserDemographics', backref='user', uselist=False, cascade="all, delete-orphan")
    orders = db.relationship('Order', backref='user', cascade="all, delete-orphan")


# User Demographics Table
class UserDemographics(db.Model):
    __tablename__ = 'user_demographics'

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False, check_constraint="gender IN ('Male', 'Female')")
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    zip_code = db.Column(db.String(20))


# Categories Table
class Category(db.Model):
    __tablename__ = 'categories'

    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    # Relationship
    products = db.relationship('Product', backref='category', cascade="all, delete-orphan")


# Products Table
class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_qty = db.Column(db.Integer, nullable=False, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    # Relationship
    order_items = db.relationship('OrderItem', backref='product', cascade="all, delete-orphan")


# Orders Table
class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False, check_constraint="status IN ('Pending', 'Shipped', 'Delivered', 'Cancelled')")
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    # Relationships
    order_items = db.relationship('OrderItem', backref='order', cascade="all, delete-orphan")
    payment = db.relationship('Payment', backref='order', uselist=False, cascade="all, delete-orphan")


# Order Items Table
class OrderItem(db.Model):
    __tablename__ = 'order_items'

    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)


# Payments Table
class Payment(db.Model):
    __tablename__ = 'payments'

    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    method = db.Column(db.String(20), nullable=False, check_constraint="method IN ('Credit Card', 'PayPal', 'Bank Transfer', 'Cash on Delivery')")
    status = db.Column(db.String(20), nullable=False, check_constraint="status IN ('Pending', 'Completed', 'Failed', 'Refunded')")
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
