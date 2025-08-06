import google.generativeai as genai

class ExploreAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def suggest_attractions_and_food(self, destination):
        prompt = f"What are the top tourist attractions and famous food in {destination}?"
        response = self.model.generate_content(prompt)
        return response.text.strip()
