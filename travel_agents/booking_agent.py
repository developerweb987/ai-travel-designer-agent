from agents import Agent
from tools.flights import get_flights
from tools.hotels import suggest_hotels

class BookingAgent(Agent):
    def __init__(self, model):
        super().__init__(
            name="BookingAgent",
            instructions="You simulate flight and hotel booking for the user."
        )

    def book_trip(self, destination):
        flights = get_flights(destination)
        hotels = suggest_hotels(destination)
        return {"flights": flights, "hotels": hotels}
