"""
Binance Futures Trading Bot
Simple CLI for placing orders on Binance Testnet
"""

import os
import sys
import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler


def setup_logging():
    """Setup logging config"""
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.DEBUG)
    
    if logger.handlers:
        return logger
    
    # Console output - simple format
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    logger.addHandler(console)
    
    # File handler - detailed logs
    log_file = os.path.join(log_dir, "bot.log")
    file_handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s | %(levelname)s | %(funcName)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    ))
    logger.addHandler(file_handler)
    
    return logger


# Default logger
logger = setup_logging()

