import os
import asyncio
from dotenv import load_dotenv

from travel_agents.destination_agent import destination_agent
from travel_agents.booking_agent import booking_agent
from travel_agents.explore_agent import explore_agent

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
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

destination_agent.model = model
booking_agent.model = model
explore_agent.model = model

destination_agent.handoffs = [booking_agent]
booking_agent.handoffs = [explore_agent]

async def travel_designer_loop():
    travel_agent = Agent(
        name="TravelDesignerAgent",
        instructions=(
            "Plan a full travel experience. "
            "DestinationAgent finds places, "
            "BookingAgent simulates travel booking, "
            "ExploreAgent suggests attractions & food."
        ),
        model=model,
        handoffs=[destination_agent, booking_agent, explore_agent]
    )

    chat_history = []

    print("\n Welcome to AI Travel Designer Agent! Let's plan your dream trip.\n")

    while True:
        user_input = input("Your travel request: ").strip()
        if user_input.lower() in ["quit", "exit"]:
            print("\n Exiting AI Travel Designer. Goodbye!")
            break

        chat_history.append({"role": "user", "content": user_input})

        try:
            result = await Runner.run(travel_agent, chat_history, run_config=config)
            response = result.final_output
            print(f"\n {response}\n")
            chat_history.append({"role": "assistant", "content": response})
        except Exception as e:
            print(f"\n Error: {str(e)}\n")

if __name__ == "__main__":
    asyncio.run(travel_designer_loop())
