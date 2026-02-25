# Complete Setup Guide - Binance Futures Trading Bot

================================================================================
STEP 1: GET BINANCE FUTURES TESTNET API CREDENTIALS
================================================================================

1. Go to: https://testnet.binancefuture.com
2. Click "Register" to create a testnet account
3. After login, go to your profile (top right corner)
4. Click "API Keys" 
5. Click "Create API" button
6. Give your key a name (e.g., "trading-bot")
7. Copy the API Key and Secret Key - SAVE THEM SECURELY!

NOTE: These are TESTNET credentials, not real money!

================================================================================
STEP 2: INSTALL DEPENDENCIES
================================================================================

Run this command in your terminal:

    pip install python-binance

================================================================================
STEP 3: CONFIGURE API CREDENTIALS
================================================================================

You have THREE options to add your API credentials:

--- OPTION A: Environment Variables (Recommended) ---
Add these to your terminal BEFORE running the bot:

    export BINANCE_API_KEY="PASTE_YOUR_API_KEY_HERE"
    export BINANCE_API_SECRET="PASTE_YOUR_API_SECRET_HERE"

--- OPTION B: Add Directly in cli.py (Line 16-17) ---
File: trading_bot/bot/cli.py

Find these lines:
    parser.add_argument("--api-key", default=os.environ.get("BINANCE_API_KEY"), help="API Key")
    parser.add_argument("--api-secret", default=os.environ.get("BINANCE_API_SECRET"), help="API Secret")

Change them to:
    parser.add_argument("--api-key", default="PASTE_YOUR_API_KEY_HERE", help="API Key")
    parser.add_argument("--api-secret", default="PASTE_YOUR_API_SECRET_HERE", help="API Secret")

--- OPTION C: Command Line Arguments ---
Run the bot with API keys as arguments:

    python -m bot.cli -s BTCUSDT --side BUY -t MARKET -q 0.01 --api-key YOUR_KEY --api-secret YOUR_SECRET

================================================================================
STEP 4: RUN THE BOT
================================================================================

--- Example 1: MARKET Buy Order ---
    python -m bot.cli -s BTCUSDT --side BUY -t MARKET -q 0.01

--- Example 2: MARKET Sell Order ---
    python -m bot.cli -s ETHUSDT --side SELL -t MARKET -q 0.1

--- Example 3: LIMIT Buy Order ---
    python -m bot.cli -s BTCUSDT --side BUY -t LIMIT -q 0.01 -p 45000

--- Example 4: LIMIT Sell Order ---
    python -m bot.cli -s BTCUSDT --side SELL -t LIMIT -q 0.01 -p 55000

================================================================================
COMMAND ARGUMENTS EXPLAINED
================================================================================

-s, --symbol        Trading pair (e.g., BTCUSDT, ETHUSDT, SOLUSDT)
--side             Order direction: BUY or SELL
-t, --type         Order type: MARKET or LIMIT
-q, --quantity     How much to buy/sell
-p, --price        Limit price (REQUIRED for LIMIT orders only)
--api-key          Your Binance API Key
--api-secret       Your Binance API Secret

================================================================================
TROUBLESHOOTING
================================================================================

Q: "API key and secret required"
A: You need to set the API credentials using one of the methods in Step 3

Q: "API-key format invalid"
A: Your API key is incorrect. Double-check your credentials from testnet

Q: "Symbol must end with USDT"
A: Use valid symbols like BTCUSDT, ETHUSDT, etc.

Q: "Price required for LIMIT orders"
A: Add -p or --price argument for LIMIT orders

Q: "Quantity must be positive"
A: Use a positive number for quantity

================================================================================
PROJECT FILES REFERENCE
================================================================================

File                    Purpose
----------------------  ----------------------------------------------------------
bot/cli.py              Main entry point - run commands here (Line 15+)
bot/client.py           Binance API connection (Line 10-13)
bot/orders.py           Order processing logic
bot/validators.py       Input validation
bot/logging_config.py  Logging setup
logs/bot.log            All activity logged here
README.md              Basic documentation

================================================================================

