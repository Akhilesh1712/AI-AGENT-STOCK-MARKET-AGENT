import requests

def fetch_stock_price(ticker):
    response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&apikey=W8LVDR6U4ESRLB0M')

    if response.status_code == 200:
        data = response.json()
        return data['Time Series (1min)'][list(data['Time Series (1min)'].keys())[0]]['1. open']

    else:
        return None
