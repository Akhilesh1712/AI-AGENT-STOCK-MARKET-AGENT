class StockAgent:
    def analyze_price(self, price):
        print(f"Analyzing price: {price} (Type: {type(price)})")  # Debugging statement

        if price is None:
            return "Price not available"
        elif float(price) < 100:

            return "Buy"
        elif price > 150:
            return "Sell"
        else:
            return "Hold"
