import asyncio
import aiohttp
import random
import time

BASE_URL = "http://127.0.0.1:5000"  # Change if hosted elsewhere

ENDPOINTS = ["/users", "/orders", "/register_user", "/simulate_purchase"]

async def call_api(session, endpoint):
    """Asynchronously call the given API endpoint."""
    url = f"{BASE_URL}{endpoint}"
    try:
        async with session.get(url) as response:
            data = await response.json()
            print(f"Called {endpoint}: {data}")
    except Exception as e:
        print(f"Error calling {endpoint}: {e}")

async def simulate_traffic(num_requests, total_time):
    """Simulate real-time application usage over a time span."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        start_time = time.time()
        for _ in range(num_requests):
            delay = random.uniform(0, total_time)  # Random delay within the time span
            endpoint = random.choice(ENDPOINTS)  # Randomly choose an API endpoint
            tasks.append(asyncio.create_task(delayed_request(session, endpoint, delay)))
        
        await asyncio.gather(*tasks)

async def delayed_request(session, endpoint, delay):
    """Wait for a random delay before making a request."""
    await asyncio.sleep(delay)
    await call_api(session, endpoint)

import asyncio

def get_user_inputs():
    """Prompt user for the number of requests and total duration."""
    while True:
        try:
            num_requests = int(input("Enter the number of API requests to send: "))
            total_time = int(input("Enter the total duration in seconds: "))
            if num_requests > 0 and total_time > 0:
                return num_requests, total_time
            else:
                print("Both values must be positive integers. Try again.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    num_requests, total_time = get_user_inputs()
    print(f"Simulating {num_requests} API requests over {total_time} seconds...")
    asyncio.run(simulate_traffic(num_requests, total_time))

