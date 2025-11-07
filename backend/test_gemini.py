import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure the API key
api_key = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Try different model names
models_to_try = [
    "gemini-1.5-pro-latest",
    "gemini-1.5-flash-latest",
    "gemini-1.0-pro",
    "models/gemini-1.5-pro-latest",
    "models/gemini-1.5-flash-latest"
]

model = None
for model_name in models_to_try:
    try:
        model = genai.GenerativeModel(model_name)
        print(f"Successfully loaded model: {model_name}")
        break
    except Exception as e:
        print(f"Failed to load model {model_name}: {e}")
        continue

if model is None:
    print("Failed to load any model")
    exit(1)

# Generate content
response = model.generate_content("Write a short poem about programming.")
print(response.text)