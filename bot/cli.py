"""
Trading Bot CLI
Simple command line interface for Binance Futures
"""

import os
import sys
import argparse
from bot.client import BinanceClient, BinanceAPIError
from bot.orders import process_order, print_order_summary
from bot.logging_config import logger


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", "-s", required=True, help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", "-t", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", "-q", required=True, help="Order quantity")
    parser.add_argument("--price", "-p", help="Limit price (required for LIMIT orders)")
    parser.add_argument("--api-key", default=os.environ.get("BINANCE_API_KEY"), help="API Key")
    parser.add_argument("--api-secret", default=os.environ.get("BINANCE_API_SECRET"), help="API Secret")
    
    args = parser.parse_args()
    
    # Check API credentials
    if not args.api_key or not args.api_secret:
        print("Error: API key and secret required")
        print("Set as environment variables or use --api-key and --api-secret")
        sys.exit(1)
    
    # Build request dict for logging
    request = {
        "symbol": args.symbol,
        "side": args.side,
        "order_type": args.type,
        "quantity": args.quantity,
        "price": args.price
    }
    
    print(f"\nPlacing {args.type} {args.side} order for {args.quantity} {args.symbol}")
    
    try:
        # Create client
        client = BinanceClient(args.api_key, args.api_secret)
        
        # Place order
        response = process_order(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
        
        # Print result
        print_order_summary(request, response)
        print("\n✓ Order placed successfully!")
        
    except BinanceAPIError as e:
        print(f"\n✗ API Error: {e}")
        logger.error(f"API Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"\n✗ Validation Error: {e}")
        logger.error(f"Validation Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        logger.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

