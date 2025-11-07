import os
import google.generativeai as genai
import re
import json
from dotenv import load_dotenv

load_dotenv()

# Configure the API key
api_key = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Create the model
model = genai.GenerativeModel('models/gemini-2.0-flash-001')

def get_gemini_response(user_input: str, risk: str) -> dict:
    try:
        prompt = f"""You are a personal financial advisor dedicated to helping in financial journey. Focus on providing guidance on budgeting, investing, retirement planning, debt management, and wealth building strategies. Be precise and practical in your advice while considering individual circumstances.

Key areas of expertise:
- Budgeting and expense tracking
- Investment strategies and portfolio management
- Retirement planning
- Debt management and elimination
- Tax planning considerations
- Emergency fund planning
- Risk management and insurance

Provide balanced, ethical financial advice and acknowledge when certain situations may require consultation with other financial professionals.

For the given user query you have to response a proper output by giving proper response in the following format
Strictly follow the given format only

User query: {user_input}
Risk profile: {risk}

Respond with a JSON object in the following format:
{{
  "nodes": [
    {{
      "id": "start",
      "position": {{ "x": 250, "y": 50 }},
      "data": {{ "label": "Investment\\n₹1,00,000" }},
      "style": {{
        "background": "bg-blue-100",
        "border": "border-blue-500"
      }}
    }},
    {{
      "id": "index",
      "position": {{ "x": 50, "y": 200 }},
      "data": {{ "label": "Index Funds\\n₹40,000" }},
      "style": {{
        "background": "bg-indigo-100",
        "border": "border-indigo-500"
      }}
    }},
    {{
      "id": "midcap",
      "position": {{ "x": 250, "y": 200 }},
      "data": {{ "label": "Mid-Cap Stocks\\n₹35,000" }},
      "style": {{
        "background": "bg-orange-100",
        "border": "border-orange-500"
      }}
    }},
    {{
      "id": "gold",
      "position": {{ "x": 450, "y": 200 }},
      "data": {{ "label": "Gold Investment\\n₹25,000" }},
      "style": {{
        "background": "bg-yellow-100",
        "border": "border-yellow-500"
      }}
    }}
  ],
  "edges": [
    {{
      "id": "e-index",
      "source": "start",
      "target": "index",
      "label": "40%",
      "style": {{ "stroke": "stroke-indigo-500" }}
    }},
    {{
      "id": "e-midcap",
      "source": "start",
      "target": "midcap",
      "label": "35%",
      "style": {{ "stroke": "stroke-orange-500" }}
    }},
    {{
      "id": "e-gold",
      "source": "start",
      "target": "gold",
      "label": "25%",
      "style": {{ "stroke": "stroke-yellow-500" }}
    }}
  ]
}}
"""
        
        response = model.generate_content(prompt)
        response_text = response.text
        
        # Extract content between ```json and ``` blocks
        json_match = re.search(r'```json\s*(.*?)\s*```', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
            return json.loads(json_str)
        else:
            # Try to parse the entire response as JSON
            return json.loads(response_text)
    except Exception as e:
        print(f"Error: {e}")
        return {"error": f"Failed to generate response: {str(e)}"}

if __name__ == "__main__":
    # Sample test query
    test_query = "I have around ten lakh rupees where should I invest them"
    print("Test Query:", test_query)
    response = get_gemini_response(test_query, "moderate")
    print("Response:", response)