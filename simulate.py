import asyncio
import aiohttp
import random
import os

BASE_URL = os.getenv("SIM_BASE_URL", "http://127.0.0.1:5000")
ENDPOINTS = ["/users", "/orders", "/register_user", "/simulate_purchase"]

async def call_api(session, endpoint):
    url = f"{BASE_URL}{endpoint}"
    try:
        async with session.get(url) as response:
            data = await response.json()
            print(f"Called {endpoint}: {data}")
    except Exception as e:
        print(f"Error calling {endpoint}: {e}")

async def simulate_traffic(num_requests, total_time):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_requests):
            delay = random.uniform(0, total_time)
            endpoint = random.choice(ENDPOINTS)
            tasks.append(asyncio.create_task(asyncio.sleep(delay)))
            tasks.append(asyncio.create_task(call_api(session, endpoint)))
        await asyncio.gather(*tasks)

def get_user_inputs():
    while True:
        try:
            n = int(input("Number of API requests: "))
            t = int(input("Total duration (s): "))
            if n > 0 and t > 0:
                return n, t
        except ValueError:
            pass
        print("Please enter positive integers.")

if __name__ == "__main__":
    n, t = get_user_inputs()
    print(f"Simulating {n} requests over {t}s…")
    asyncio.run(simulate_traffic(n, t))
