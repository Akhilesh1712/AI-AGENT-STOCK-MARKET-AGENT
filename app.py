from flask import Flask, request, jsonify
from stock_fetcher import fetch_stock_price
from agent import StockAgent

app = Flask(__name__)
agent = StockAgent()

@app.route('/stock/<ticker>', methods=['GET'])
def get_stock_price(ticker):
    price = fetch_stock_price(ticker)
    print(f"Fetched price: {price} (Type: {type(price)})")  # Debugging statement

    recommendation = agent.analyze_price(float(price))

    return jsonify({
        'ticker': ticker,
        'price': price,
        'recommendation': recommendation
    })

if __name__ == '__main__':
    app.run(debug=True)
