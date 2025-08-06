import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env in the same folder
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

genai.configure(api_key=API_KEY)
