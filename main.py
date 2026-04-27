#!/usr/bin/env python3
# ============================================================
# main.py - Entry Point
# ============================================================
# Run this file to start the Alpaca trading bot.
#
# Usage:
#   python main.py
#
# Prerequisites:
#   1. Install dependencies:   pip install -r requirements.txt
#   2. Create a .env file with your Alpaca credentials:
#        ALPACA_API_KEY=<your key>
#        ALPACA_SECRET_KEY=<your secret>
#        ALPACA_BASE_URL=https://paper-api.alpaca.markets
#
# TODO: Add CLI argument parsing (argparse or click) so users can:
#         --strategy <name>    choose a trading strategy at runtime
#         --dry-run            print signals without placing orders
#         --log-level DEBUG    adjust verbosity without editing source
# TODO: Add a health check / preflight function that verifies:
#         - API credentials are set and valid
#         - The account is active and not restricted
#         - Dependencies are installed
#       Print a clear error message and exit if any check fails.
# TODO: Research process management tools (systemd, supervisor, Docker)
#       for running the bot as a persistent service on a server.
# ============================================================

import logging

from alpaca_trader.utils.helpers import setup_logging
from alpaca_trader.trader import Trader

# Configure logging before anything else so all modules use the same format.
# TODO: Read LOG_LEVEL from config instead of hard-coding it here.
setup_logging(level="INFO")

logger = logging.getLogger(__name__)


def main():
    """
    Application entry point.

    TODO: Add error handling / alerting so that unhandled exceptions
          are caught, logged, and optionally trigger a notification
          (email, Slack, PagerDuty) before the process exits.
    TODO: Implement a watchdog / restart mechanism so the bot
          automatically recovers from transient network errors.
    """
    logger.info("=" * 60)
    logger.info("  AutoTrader - Alpaca Trading Bot (Prototype)")
    logger.info("  *** NOT FUNCTIONAL - skeleton layout only ***")
    logger.info("=" * 60)

    # ── Initialize the trader ────────────────────────────────
    # TODO: Pass the desired strategy name as a parameter once multiple
    #       strategies are available.
    trader = Trader()

    # ── Fetch account info (placeholder call) ───────────────
    # TODO: Remove this comment and uncomment once credentials are set up:
    # account = trader.get_account()
    # logger.info("Buying power: %s", account.buying_power)

    # ── Start the main trading loop ──────────────────────────
    # TODO: Uncomment once the run loop is implemented in trader.py:
    # trader.run()

    logger.info("Bot exited cleanly (no trading occurred – skeleton run).")


if __name__ == "__main__":
    main()
