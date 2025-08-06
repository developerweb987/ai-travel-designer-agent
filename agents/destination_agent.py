import google.generativeai as genai

class DestinationAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def suggest_destination(self, mood_or_interest):
        prompt = f"Suggest one best travel destination for someone interested in {mood_or_interest}."
        response = self.model.generate_content(prompt)
        return response.text.strip()
