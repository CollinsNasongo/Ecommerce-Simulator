from faker import Faker
import random
from app.models import db, User, UserDemographics, Order, OrderItem, Payment, Product

fake = Faker()

def user_registration():
    # Create a fake user
    user = User(
        name=fake.name(),
        email=fake.unique.email(),
        phone_number=fake.phone_number(),
        address=fake.address(),
    )
    db.session.add(user)
    db.session.commit()

    # Create fake demographics for the user
    demographics = UserDemographics(
        user_id=user.user_id,
        age=random.randint(18, 65),
        gender=random.choice(['Male', 'Female']),
        city=fake.city(),
        state=fake.state(),
        country=fake.country(),
        zip_code=fake.zipcode(),
    )
    db.session.add(demographics)
    db.session.commit()

    return user

def user_purchase():
    # Get a random user
    users = User.query.all()
    if not users:
        return "No users found. Generate users first."
    user = random.choice(users)

    # Get a random product
    products = Product.query.all()
    if not products:
        return "No products found. Generate products first."
    product = random.choice(products)

    # Create an order
    order = Order(
        user_id=user.user_id,
        total_price=product.price,  # Assuming the order has only one product for simplicity
        status=random.choice(['Pending', 'Shipped', 'Delivered', 'Cancelled']),
    )
    db.session.add(order)
    db.session.commit()

    # Create an order item
    order_item = OrderItem(
        order_id=order.order_id,
        product_id=product.product_id,
        quantity=1,  # Assuming the user buys one quantity of the product
        price=product.price,
    )
    db.session.add(order_item)
    db.session.commit()

    # Create a payment
    payment = Payment(
        order_id=order.order_id,
        amount=order.total_price,
        method=random.choice(['Credit Card', 'PayPal', 'Bank Transfer', 'Cash on Delivery']),
        status=random.choice(['Pending', 'Completed', 'Failed', 'Refunded']),
    )
    db.session.add(payment)
    db.session.commit()

    return order