# Stock Agent API

## Overview
The Stock Agent API is an AI-driven application that fetches the latest stock market prices and provides buy, sell, or hold recommendations. Built using Python, LangChain, and an LLM API, this project aims to assist users in making informed investment decisions based on real-time data.

## Project Structure
```
stock_agent/
├── app.py                
├── requirements.txt    
├── README.md           
├── stock_fetcher.py      
├── agent.py             
└── utils.py             
```

## Setup

1. Clone the repository or download the project files.
   ```bash
   git clone https://github.com/Akhilesh1712/AI-AGENT-STOCK-MARKET-AGENT.git
   ```
2. Navigate to the project directory:
   ```bash
   cd stock_agent
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```
2. Access the API endpoint to fetch stock prices and recommendations:
   ```
   GET /stock/<ticker>
   ```

### Example

To get the stock price and recommendation for a specific ticker, use the following command:
```bash
curl http://127.0.0.1:5000/stock/AAPL
```

### API Response
The API will return a JSON response containing:
- `ticker`: The stock ticker symbol.
- `price`: The current stock price.
- `recommendation`: The buy/sell/hold recommendation based on the analysis.

### Error Handling
In case of an error (e.g., invalid ticker), the API will return a JSON response with an appropriate error message.

## Contribution
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.
