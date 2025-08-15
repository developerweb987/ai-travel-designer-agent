import random

async def get_flights(destination: str):
    """Mock flight info"""
    flights = [
        {"airline": "SkyWays", "price": 550, "duration": "5h 30m"},
        {"airline": "AirExpress", "price": 480, "duration": "5h 10m"},
        {"airline": "TravelAir", "price": 600, "duration": "5h 40m"}
    ]
    return random.choice(flights)

async def suggest_hotels(destination: str):
    """Mock hotel suggestions"""
    hotels = {
        "Paris": ["Hotel Lumiere", "Eiffel Stay", "Seine View Inn"],
        "Tokyo": ["Shibuya Central Hotel", "Tokyo Tower Inn", "Sakura Stay"],
        "New York": ["Times Square Hotel", "Central Park View", "Brooklyn Lodge"]
    }
    return hotels.get(destination, ["Grand Plaza", "City Lights Hotel", "Urban Comfort Inn"])
