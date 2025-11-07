import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure the API key
api_key = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# List available models
try:
    for model in genai.list_models():
        print(f"Model: {model.name}")
        print(f"Display Name: {model.display_name}")
        print(f"Description: {model.description}")
        print("---")
except Exception as e:
    print(f"Error listing models: {e}")