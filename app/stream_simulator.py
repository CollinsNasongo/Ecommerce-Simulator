import time
import random
from app.utils import user_registration, user_purchase

def simulate_user_activity_stream(interval_seconds=2, max_events=None):
    """
    Simulates a real-time stream of user activity:
    - New user registrations
    - User purchases
    """
    event_count = 0

    while True:
        event_type = random.choices(
            ['register', 'purchase'],
            weights=[0.3, 0.7],
            k=1
        )[0]

        if event_type == 'register':
            try:
                user = user_registration()
                print(f"[REGISTER] User {user.user_id} - {user.name} ({user.email}) registered.")
            except Exception as e:
                print(f"[ERROR] Registration failed: {e}")

        elif event_type == 'purchase':
            result = user_purchase()
            if isinstance(result, str):
                print(f"[WARN] {result}")
            else:
                print(f"[PURCHASE] Order {result.order_id} by User {result.user_id} - Total: ${result.total_price:.2f}")

        event_count += 1
        if max_events and event_count >= max_events:
            print(f"[STREAM] Simulated {max_events} events. Stopping.")
            break

        time.sleep(interval_seconds)