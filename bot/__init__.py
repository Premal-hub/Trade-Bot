"""
Trading Bot Package
"""

__version__ = '1.0.0'

from bot.client import BinanceClient, BinanceAPIError
from bot.orders import process_order, print_order_summary
from bot.validators import validate_symbol, validate_side, validate_order_type, validate_quantity, validate_price

__all__ = [
    'BinanceClient',
    'BinanceAPIError',
    'process_order',
    'print_order_summary',
    'validate_symbol',
    'validate_side',
    'validate_order_type',
    'validate_quantity',
    'validate_price',
]

