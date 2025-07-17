from app.database import db

class User(db.Model):
    user_id      = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(128), nullable=False)
    email        = db.Column(db.String(128), unique=True, nullable=False)
    phone_number = db.Column(db.String(32))
    address      = db.Column(db.String(256))
    demographics = db.relationship("UserDemographics", backref="user", uselist=False)
    orders       = db.relationship("Order", backref="user")

class UserDemographics(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    user_id  = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    age      = db.Column(db.Integer)
    gender   = db.Column(db.String(32))
    city     = db.Column(db.String(64))
    state    = db.Column(db.String(64))
    country  = db.Column(db.String(64))
    zip_code = db.Column(db.String(16))

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(128), nullable=False)
    price      = db.Column(db.Numeric(10,2), nullable=False)
    items      = db.relationship("OrderItem", backref="product")

class Order(db.Model):
    order_id    = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    total_price = db.Column(db.Numeric(10,2))
    status      = db.Column(db.String(32))
    items       = db.relationship("OrderItem", backref="order")
    payment     = db.relationship("Payment", backref="order", uselist=False)

class OrderItem(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    order_id   = db.Column(db.Integer, db.ForeignKey("order.order_id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"), nullable=False)
    quantity   = db.Column(db.Integer)
    price      = db.Column(db.Numeric(10,2))

class Payment(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.order_id"), nullable=False)
    amount   = db.Column(db.Numeric(10,2))
    method   = db.Column(db.String(32))
    status   = db.Column(db.String(32))
