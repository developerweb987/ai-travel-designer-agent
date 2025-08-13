from agents import Agent

class ExploreAgent(Agent):
    def __init__(self, model):
        super().__init__(
            name="ExploreAgent",
            instructions="You suggest attractions, activities, and food options at the destination."
        )
