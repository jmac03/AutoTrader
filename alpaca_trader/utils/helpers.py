# ============================================================
# utils/helpers.py - Miscellaneous Utility Functions
# ============================================================
# This module will hold helper functions that are used across
# the project but do not belong to a single class.
#
# TODO: Research and implement the helpers that are most urgently
#       needed, likely in this order:
#         1. is_market_open()     - before implementing the run loop
#         2. setup_logging()      - before any real testing
#         3. calculate_position_size() - before placing orders
# ============================================================

import logging

# TODO: Import datetime / timezone once time-based helpers (e.g., market
#       schedule checks) are implemented.
# from datetime import datetime, timezone

logger = logging.getLogger(__name__)


def setup_logging(level: str = "INFO") -> None:
    """
    Configure the root logger with a consistent format.

    TODO: Add a rotating file handler so logs are saved to disk and
          do not grow unboundedly.
    TODO: Research structured logging (JSON format) to make logs easier
          to parse with tools like Kibana, Splunk, or Datadog.
    TODO: Add a Slack/email/SMS alert handler for critical log events
          (e.g., when a large loss is detected or an order is rejected).

    Args:
        level: Logging level string, e.g. "DEBUG", "INFO", "WARNING".
    """
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger.debug("Logging configured at level: %s", level)


def is_market_open(api=None) -> bool:
    """
    Return True if the US stock market is currently open.

    TODO: Implement using Alpaca's /v2/clock endpoint:
        clock = api.get_clock()
        return clock.is_open
    TODO: Handle pre-market and after-hours trading windows if
          the strategy requires extended-hours order placement.
    TODO: Account for market holidays (Alpaca's clock endpoint
          already handles this automatically).

    Args:
        api: An authenticated Alpaca REST API client instance.

    Returns:
        bool – True if the market is open, False otherwise.
    """
    if api is None:
        logger.warning(
            "is_market_open called without an API client; returning False."
        )
        return False

    # TODO: Replace placeholder with real Alpaca clock call:
    # clock = api.get_clock()
    # return clock.is_open
    logger.warning("is_market_open is not yet implemented; returning False.")
    return False


def calculate_position_size(
    buying_power: float,
    price: float,
    risk_pct: float = 0.05,
) -> float:
    """
    Calculate the number of shares to buy based on available buying
    power and the desired risk percentage.

    Simple calculation:
        dollars_to_risk = buying_power * risk_pct
        shares          = dollars_to_risk / price

    Args:
        buying_power: Available cash in the account (USD).
        price:        Current market price per share (USD).
        risk_pct:     Fraction of buying power to allocate (0.0 – 1.0).

    Returns:
        float – Number of shares to buy (may be fractional).

    TODO: Research more sophisticated position-sizing methods:
          - Fixed fractional (what this function currently does)
          - Fixed dollar amount per trade
          - Volatility-based sizing (ATR-based)
          - Kelly Criterion
    TODO: Add a maximum position size cap to prevent a single trade
          from consuming too much of the portfolio.
    TODO: Round down to the nearest whole share if fractional shares
          are not supported for the given symbol.
    """
    if price <= 0:
        logger.error("Invalid price: %s; cannot calculate position size.", price)
        return 0.0

    dollars_to_risk = buying_power * risk_pct
    shares = dollars_to_risk / price
    logger.debug(
        "Position size: $%.2f buying power x %.1f%% = %.4f shares @ $%.2f",
        buying_power, risk_pct * 100, shares, price,
    )
    return shares


def format_currency(amount: float) -> str:
    """
    Format a float as a USD currency string.

    Example:
        format_currency(1234.5) -> "$1,234.50"

    TODO: Extend to support multiple currencies if crypto trading is added.
    """
    return f"${amount:,.2f}"
