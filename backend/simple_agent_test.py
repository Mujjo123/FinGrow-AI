from tools.mytools import get_current_price

# Test the tool directly
try:
    price = get_current_price("Adani green")
    print(f"Adani green price: {price}")
except Exception as e:
    print(f"Error getting price: {e}")
    import traceback
    traceback.print_exc()