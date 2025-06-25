from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
import requests
from typing import Dict, Any

load_dotenv(override=True)

# Initialize FastMCP server
mcp = FastMCP("stock")
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

@mcp.tool()
async def get_stock(symbol: str, interval: str = "5min") -> Dict[str, Any] | str:
    """Get stock data for a symbol.

    Args:
        symbol: Symbol of the stock
        interval: Interval of the stock data
    """
    # Constants
    API_BASE = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + symbol + "&interval=" + interval + "&apikey=" + API_KEY
    
    try:
        response = requests.get(API_BASE)
        stock_data = response.json()
        if not stock_data:
            return "Unable to fetch stock data for this symbol. Please check the symbol and try again."
        return stock_data
    except Exception as e:
        return f"Error fetching stock data: {e}"

if __name__ == "__main__":
    # Initialize and run the server
    print("Starting MCP server...")
    mcp.run(transport='stdio')