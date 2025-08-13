from agents import Agent

class DestinationAgent(Agent):
    def __init__(self, model):
        super().__init__(
            name="DestinationAgent",
            instructions="You suggest travel destinations based on user preferences."
        )
