import os
import asyncio
from dotenv import load_dotenv
from travel_agents.destination_agent import DestinationAgent
from travel_agents.booking_agent import BookingAgent
from travel_agents.explore_agent import ExploreAgent
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=base_url
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

destination_agent = DestinationAgent(model)
booking_agent = BookingAgent(model)
explore_agent = ExploreAgent(model)

async def travel_designer_loop():
    agent = Agent(
        name="AITravelDesignerAgent",
        instructions=(
            "You plan a complete travel experience. "
            "Hand off to DestinationAgent to suggest places, "
            "BookingAgent to simulate bookings, "
            "ExploreAgent to suggest attractions and food."
        ),
        handoffs=[destination_agent, booking_agent, explore_agent]
    )

    chat_history = []

    print("Welcome to AI Travel Designer Agent! Plan your travel experience.\n")

    while True:
        user_input = input("Your request: ").strip()
        if user_input.lower() in ["quit", "exit"]:
            print("Exiting Travel Designer. Goodbye!")
            break

        chat_history.append({"role": "user", "content": user_input})

        try:
            result = await Runner.run(agent, chat_history, run_config=config)
            response = result.final_output
            print(f"\n{response}\n")
            chat_history.append({"role": "developer", "content": response})
        except Exception as e:
            print(f"Error: {str(e)}\n")

if __name__ == "__main__":
    asyncio.run(travel_designer_loop())
