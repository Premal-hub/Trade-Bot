"""
Input validators for trading orders
"""

def validate_symbol(symbol):
    """Validate trading symbol"""
    if not symbol:
        raise ValueError("Symbol cannot be empty")
    symbol = symbol.upper().strip()
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT (e.g., BTCUSDT)")
    return symbol


def validate_side(side):
    """Validate order side"""
    if not side:
        raise ValueError("Side cannot be empty")
    side = side.upper().strip()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side


def validate_order_type(order_type):
    """Validate order type"""
    if not order_type:
        raise ValueError("Order type cannot be empty")
    order_type = order_type.upper().strip()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type


def validate_quantity(qty):
    """Validate quantity"""
    try:
        quantity = float(qty)
    except (ValueError, TypeError):
        raise ValueError("Quantity must be a number")
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    return quantity


def validate_price(price, order_type):
    """Validate price - required for LIMIT orders"""
    if order_type == "MARKET":
        return None
    if not price:
        raise ValueError("Price required for LIMIT orders")
    try:
        return float(price)
    except (ValueError, TypeError):
        raise ValueError("Price must be a number")

