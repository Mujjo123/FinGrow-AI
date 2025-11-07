import sys
sys.path.append('tools')
from tools.mytools import get_ticker_from_company

# Test different variations of Adani Green
test_names = ["Adani green", "Adani Green", "Adani Green Energy", "Adani Enterprises"]

for name in test_names:
    try:
        ticker = get_ticker_from_company(name)
        print(f"{name} -> {ticker}")
    except Exception as e:
        print(f"{name} -> Error: {e}")