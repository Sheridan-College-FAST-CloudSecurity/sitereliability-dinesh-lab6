from fastapi import FastAPI
import random
import time

app = FastAPI()

# Tier 1 - Critical: Product Info
@app.get("/product-info")
def product_info():
    return {
        "product": "Iphone 16",
        "price": "$650",
        "availability": "Out of stock"
    }

# Tier 2 - Important: User Reviews
@app.get("/reviews")
def reviews():
    # Simulate 30% chance of failure
    if random.random() < 0.3:
        raise Exception("Reviews service unavailable")
    return {
        "reviews": ["It's nice mobile"]
    }

# Tier 3 - Nice-to-Have: Recommendations
@app.get("/recommendations")
def recommendations():
    # Simulate 70% chance of failure due to load
    if random.random() < 0.1:
        raise Exception("Too much load on recommendations")
    return {
        "recommendations": ["Awesome Mobile", "Best mobiles recently launched", "Camera"]
    }

# Optional: System load simulator
@app.get("/system-load")
def system_load():
    load = random.randint(10, 100)
    return {"cpu_load_percent": load}