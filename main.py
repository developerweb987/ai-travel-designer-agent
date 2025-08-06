from config import API_KEY
from agents.destination_agent import DestinationAgent
from agents.booking_agent import BookingAgent
from agents.explore_agent import ExploreAgent

def main():
    print("Welcome to AI Travel Designer Agent!\n")

    mood = input("What’s your travel mood or interest? (e.g., adventure, relaxation): ")

    dest_agent = DestinationAgent()
    destination = dest_agent.suggest_destination(mood)
    print(f"\nSuggested Destination: {destination}")

    booking_agent = BookingAgent()
    flights, hotels = booking_agent.book_travel(destination)

    print("\nAvailable Flights:")
    for flight in flights:
        print(f" - {flight}")

    print("\nSuggested Hotels:")
    for hotel in hotels:
        print(f" - {hotel}")

    explore_agent = ExploreAgent()
    explore_info = explore_agent.suggest_attractions_and_food(destination)

    print(f"\nExplore {destination}:")
    print(explore_info)

if __name__ == "__main__":
    main()
