from dotenv import load_dotenv
from tools.mytools import *
import sys
import os
import re

# Load environment variables
load_dotenv()

def get_agent_response(user_input: str) -> str:
    try:
        # Convert to lowercase for easier matching
        input_lower = user_input.lower()
        
        # Check for stock price queries
        stock_price_patterns = [
            r"what is the stock price of (.+)",
            r"what is the current price of (.+)",
            r"current price of (.+)",
            r"stock price of (.+)"
        ]
        
        for pattern in stock_price_patterns:
            match = re.search(pattern, input_lower)
            if match:
                company_name = match.group(1).strip()
                try:
                    price = get_current_price(company_name)
                    return f"The current price of {company_name.title()} is ₹{price}."
                except Exception as e:
                    return f"Sorry, I couldn't find the stock price for {company_name.title()}. Please try another company name."
        
        # Check for historical price queries
        historical_patterns = [
            r"give me last (\d+) days? stock price of (.+)",
            r"last (\d+) days? stock price of (.+)",
            r"(\d+) days? stock price of (.+)"
        ]
        
        for pattern in historical_patterns:
            match = re.search(pattern, input_lower)
            if match:
                days = match.group(1)
                company_name = match.group(2).strip()
                try:
                    # Calculate start date (today - days)
                    import datetime
                    start_date = (datetime.datetime.now() - datetime.timedelta(days=int(days))).strftime("%Y-%m-%d")
                    historical_data = get_historical_price(f"{company_name}, {start_date}, {days}")
                    return f"The stock prices for {company_name.title()} for the last {days} days are: {historical_data}"
                except Exception as e:
                    return f"Sorry, I couldn't fetch the historical prices for {company_name.title()}. Please try another company name."
        
        # Check for return queries
        return_patterns = [
            r"give me last (.+) return of (.+)",
            r"last (.+) return of (.+)",
            r"(.+) return of (.+)"
        ]
        
        for pattern in return_patterns:
            match = re.search(pattern, input_lower)
            if match:
                duration = match.group(1)
                company_name = match.group(2).strip()
                try:
                    returns = evaluate_returns(f"{company_name}, {duration}")
                    return returns
                except Exception as e:
                    return f"Sorry, I couldn't calculate the returns for {company_name.title()}. Please try another company name."
        
        # For other queries, use a simple response
        if "time" in input_lower:
            current_time = check_system_time("%Y-%m-%d %H:%M:%S")
            return f"The current time is {current_time}."
        
        # Default response for unrecognized queries
        return "I'm Wealth Wise AI, your personal financial advisor. I can help you with stock prices, historical data, and financial calculations. What would you like to know?"
        
    except Exception as e:
        print("Error:", e)
        return f"Sorry, I couldn't understand that. Please try again."

# Test case
if __name__ == "__main__":
    # Sample test query
    if len(sys.argv) > 1:
        # Get the query from command line arguments
        query = ' '.join(sys.argv[1:])  # Join all arguments after script name
        print("Query:", query)
        response = get_agent_response(query)
        print("<Response>", response, "</Response>")
    else:
        print("Please provide a query as command line argument")
        print("Example: python agent.py 'What is the stock price of Adani green?'")