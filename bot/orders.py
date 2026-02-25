"""
Order handling functions
"""

from bot.client import BinanceClient, BinanceAPIError
from bot.validators import validate_symbol, validate_side, validate_order_type, validate_quantity, validate_price
from bot.logging_config import logger


def process_order(client, symbol, side, order_type, quantity, price=None):
    """
    Process and place an order
    
    Args:
        client: BinanceClient instance
        symbol: Trading pair (e.g. BTCUSDT)
        side: BUY or SELL
        order_type: MARKET or LIMIT
        quantity: Order quantity
        price: Limit price (required for LIMIT orders)
    
    Returns:
        Order response dict
    """
    # Validate inputs
    symbol = validate_symbol(symbol)
    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)
    price = validate_price(price, order_type)
    
    # Place order based on type
    if order_type == "MARKET":
        return client.place_market_order(symbol, side, quantity)
    else:
        return client.place_limit_order(symbol, side, quantity, price)


def print_order_summary(request, response):
    """Print order details in a readable format"""
    print("\n" + "="*50)
    print("ORDER SUMMARY")
    print("="*50)
    print(f"Symbol:      {request['symbol']}")
    print(f"Side:        {request['side']}")
    print(f"Type:        {request['order_type']}")
    print(f"Quantity:    {request['quantity']}")
    if request.get('price'):
        print(f"Price:       {request['price']}")
    print("-"*50)
    print(f"Order ID:    {response.get('orderId')}")
    print(f"Status:      {response.get('status')}")
    print(f"Executed:    {response.get('executedQty', '0')}")
    if response.get('avgPrice') and response.get('avgPrice') != '0':
        print(f"Avg Price:   {response.get('avgPrice')}")
    print("="*50)

