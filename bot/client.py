"""
Binance Futures API client
""" 

from binance.client import Client
from bot.logging_config import logger


class BinanceAPIError(Exception):
    """API error"""
    pass


class BinanceClient:
    """Simple wrapper for Binance Futures API"""
    
    TESTNET_URL = "https://testnet.binancefuture.com"
    
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = None
        self._init_client()
    
    def _init_client(self):
        """Initialize the Binance client"""
        try:
            self.client = Client(self.api_key, self.api_secret, testnet=True)
            self.client.FUTURES_URL = self.TESTNET_URL
            logger.info("Connected to Binance Testnet")
        except Exception as e:
            logger.error(f"Failed to connect: {e}")
            raise BinanceAPIError(f"Connection failed: {e}")
    
    def get_balance(self):
        """Get account balance"""
        try:
            account = self.client.futures_account()
            return float(account.get('totalMarginBalance', 0))
        except Exception as e:
            logger.error(f"Balance error: {e}")
            raise BinanceAPIError(str(e))
    
    def get_price(self, symbol):
        """Get current price for symbol"""
        try:
            ticker = self.client.futures_symbol_ticker(symbol=symbol)
            return float(ticker['price'])
        except Exception as e:
            logger.error(f"Price error: {e}")
            raise BinanceAPIError(str(e))
    
    def place_market_order(self, symbol, side, quantity):
        """Place market order"""
        try:
            logger.info(f"Placing market {side} {quantity} {symbol}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logger.info(f"Order placed: {order.get('orderId')}")
            return order
        except Exception as e:
            logger.error(f"Order failed: {e}")
            raise BinanceAPIError(str(e))
    
    def place_limit_order(self, symbol, side, quantity, price):
        """Place limit order"""
        try:
            logger.info(f"Placing limit {side} {quantity} {symbol} @ {price}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            logger.info(f"Order placed: {order.get('orderId')}")
            return order
        except Exception as e:
            logger.error(f"Order failed: {e}")
            raise BinanceAPIError(str(e))

