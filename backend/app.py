from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import re
from onboard import *
# Import the agent function directly
from agent import get_agent_response
import gemini_fin_path
import os

app = Flask(__name__)
# Configure CORS for production
CORS(app, origins=["https://fingrow-ai-frontend.onrender.com", "http://localhost:5173", "http://localhost:5174"])

@app.route('/', methods=['GET'])
def home():
    return jsonify("FinGrow AI Backend is Running!")

# =================== DYNAMIC APIS ===================
@app.route('/agent', methods=['POST'])
def agent():
    try:
        inp = request.form.get('input')
        print(f"Received input: {inp}")
        
        if inp:
            # Directly call the agent function instead of using subprocess
            print(inp)
            try:
                final_answer = get_agent_response(inp)
                return jsonify({'output': final_answer, 'thought': 'Direct agent response'})
            except Exception as e:
                print(f"Error calling agent: {str(e)}")
                import traceback
                traceback.print_exc()
                return jsonify({'error': str(e)}), 500
        
        return jsonify({'error': 'no input'}), 400
    except Exception as e:
        print(f"Error in /agent endpoint: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/ai-financial-path', methods=['POST'])
def ai_financial_path():
    try:
        print("Received financial path request")
        print(f"Form data: {request.form}")
        
        if 'input' not in request.form:
            print("ERROR: No input in form data")
            return jsonify({'error': 'No input provided'}), 400
            
        input_text = request.form.get('input','')
        risk = request.form.get('risk', 'conservative')
        print(f"Input: {input_text}")
        print(f"Risk: {risk}")
        
        response = gemini_fin_path.get_gemini_response(input_text, risk)
        print(f"Generated response: {response}")
        return jsonify(response)
    except Exception as e:
        print(f"Error in /ai-financial-path endpoint: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Error: {str(e)}'}), 500

# =================== STATIC APIS ===================
@app.route('/auto-bank-data', methods=['get'])
def AutoBankData():
    return bank_data

@app.route('/auto-mf-data', methods=['get'])
def AutoMFData():
    return mf_data


# =================== CONENCTION APIS ===================

# =================== BOTS ===================

if __name__ == "__main__":
    # Use the PORT environment variable for Render, default to 5000 for local development
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)