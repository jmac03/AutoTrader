# ============================================================
# config.py - Application Configuration
# ============================================================
# This module loads and exposes all configuration values that the
# trader needs (API credentials, account settings, trading parameters).
#
# SECURITY NOTE: Never hard-code API keys or secrets directly in
# source code.  Store them in a .env file (excluded from version
# control via .gitignore) and load them with python-dotenv.
#
# TODO: Add a .env.example file so new developers know which
#       environment variables are required.
# TODO: Research Alpaca's paper-trading vs live-trading base URLs
#       and decide which base URL to use during development.
#       Paper trading URL:  https://paper-api.alpaca.markets
#       Live trading URL:   https://api.alpaca.markets
# ============================================================

import os
from dotenv import load_dotenv

# Load variables from a .env file in the project root (if present).
# The .env file should look like:
#   ALPACA_API_KEY=PKXXXXXXXXXXXXXXXX
#   ALPACA_SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#   ALPACA_BASE_URL=https://paper-api.alpaca.markets
load_dotenv()

# ── Alpaca API credentials ──────────────────────────────────
# TODO: Validate that these are not None at startup and raise a
#       descriptive error if they are missing.
ALPACA_API_KEY: str = os.getenv("ALPACA_API_KEY", "")
ALPACA_SECRET_KEY: str = os.getenv("ALPACA_SECRET_KEY", "")

# Base URL controls whether trades are paper (simulated) or live.
# Default to paper trading so accidental runs don't use real money.
ALPACA_BASE_URL: str = os.getenv(
    "ALPACA_BASE_URL", "https://paper-api.alpaca.markets"
)

# ── Trading parameters ──────────────────────────────────────
# TODO: Research appropriate default values for position sizing,
#       stop-loss percentages, and take-profit targets.
# TODO: Move these to a YAML or JSON config file so they can be
#       changed without editing Python source code.

# List of ticker symbols the bot is allowed to trade.
# TODO: Research how to dynamically update this list (e.g., from a
#       watchlist stored in a database or fetched from a screener).
WATCHLIST: list = ["AAPL", "TSLA", "AMZN"]

# Maximum dollar amount to risk per trade.
# TODO: Implement proper position-sizing logic (e.g., fixed fractional,
#       Kelly criterion) rather than using a flat dollar amount.
MAX_TRADE_AMOUNT: float = 1000.00

# Percentage of the portfolio to allocate per position (0.0 – 1.0).
# TODO: Enforce that total open positions do not exceed 100 % of equity.
POSITION_SIZE_PCT: float = 0.05  # 5 % per position

# ── Data feed settings ──────────────────────────────────────
# TODO: Research Alpaca's data feed tiers (free IEX vs paid SIP) and
#       understand the latency / accuracy trade-offs.
DATA_FEED: str = "iex"  # Options: "iex" (free) or "sip" (paid)

# ── Logging ─────────────────────────────────────────────────
# TODO: Set up a structured logging configuration (e.g., rotating file
#       handler) so that trade history can be reviewed after the fact.
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
