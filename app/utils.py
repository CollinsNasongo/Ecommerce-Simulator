from faker import Faker
import random
from app.models import db, User, UserDemographics, Order, OrderItem, Payment, Product

fake = Faker()

def generate_email(name: str) -> str:
    first, last = name.lower().split()[0:2]
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com'])
    
    # Optional: Add digits for variety
    suffix = str(random.randint(1, 99)) if random.random() < 0.3 else ''
    
    return f"{first}.{last}{suffix}@{domain}"


def user_registration():
    try:
        name = fake.name()
        email = generate_email(name)

        user = User(
            name=name,
            email=email,
            phone_number=fake.phone_number(),
            address=fake.address()
        )
        db.session.add(user)
        db.session.flush()

        demographics = UserDemographics(
            user_id=user.user_id,
            age=random.randint(18, 65),
            gender=random.choice(['Male', 'Female']),
            city=fake.city(),
            state=fake.state(),
            country=fake.country(),
            zip_code=fake.zipcode()
        )
        db.session.add(demographics)
        db.session.commit()

        return user

    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Failed to register user: {e}")



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
def clear_test_data():
    db.session.execute('DELETE FROM payments')
    db.session.execute('DELETE FROM order_items')
    db.session.execute('DELETE FROM orders')
    db.session.execute('DELETE FROM user_demographics')
    db.session.execute('DELETE FROM users')
    db.session.commit()
    return "Payments, order items, orders, users, and demographics cleared."
