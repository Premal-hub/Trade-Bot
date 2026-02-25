# Binance Futures Trading Bot

A simple Python CLI tool for placing orders on Binance Futures Testnet.

## Requirements

- Python 3.8+
- Binance Futures Testnet account
- API Key and Secret from testnet

## Setup

1. Install dependencies:
```bash
pip install python-binance
```

2. Get API credentials:
   - Go to https://testnet.binancefuture.com
   - Create account and generate API key/secret

3. Set environment variables:
```bash
export BINANCE_API_KEY="your_api_key"
export BINANCE_API_SECRET="your_api_secret"
```

## Usage

Run the bot:
```bash
python -m bot.cli -s BTCUSDT --side BUY -t MARKET -q 0.01
```

Arguments:
- `-s, --symbol`     Trading pair (e.g. BTCUSDT)
- `--side`          BUY or SELL
- `-t, --type`      MARKET or LIMIT
- `-q, --quantity`  Order quantity
- `-p, --price`     Limit price (required for LIMIT orders)

## Examples

Market buy order:
```bash
python -m bot.cli -s BTCUSDT --side BUY -t MARKET -q 0.001
```

Limit sell order:
```bash
python -m bot.cli -s BTCUSDT --side SELL -t LIMIT -q 0.001 -p 50000
```

## Project Files

```
bot/
  client.py         - Binance API wrapper
  orders.py         - Order processing
  validators.py     - Input validation
  logging_config.py - Logging setup
  cli.py            - CLI entry point
```

## Logs

Logs are saved in the `logs/` folder. Check `bot.log` for details.

