from agents import Agent
from tools.travel_tools import get_flights, suggest_hotels

booking_agent = Agent(
    name="BookingAgent",
    instructions="Simulate booking flights and hotels for the chosen destination.",
    model=None,
    handoffs=[]
)
