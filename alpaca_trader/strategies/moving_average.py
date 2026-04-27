# ============================================================
# strategies/moving_average.py - Moving Average Crossover Strategy
# ============================================================
# This is a placeholder / skeleton for a Simple Moving Average (SMA)
# crossover strategy.  It is NOT functional yet.
#
# Strategy logic overview (to be implemented):
#   - A "golden cross" (short SMA crosses ABOVE long SMA) is a BUY signal.
#   - A "death cross"  (short SMA crosses BELOW long SMA) is a SELL signal.
#   - Otherwise, hold the current position.
#
# Example parameter values commonly used:
#   Short window:  9-day  or 20-day SMA
#   Long  window:  21-day or 50-day SMA
#
# TODO: Research whether SMA or EMA (Exponential Moving Average) produces
#       better results for the symbols in the watchlist.  EMA gives more
#       weight to recent prices, making it more responsive.
# TODO: Research how to source OHLCV (Open, High, Low, Close, Volume) bar
#       data from Alpaca's /v2/stocks/{symbol}/bars endpoint.
# TODO: Consider using the pandas-ta or ta-lib library to calculate
#       moving averages instead of implementing them manually.
# TODO: Backtest this strategy before trading with real or paper money.
# ============================================================

import logging
from alpaca_trader.strategies.base_strategy import BaseStrategy

logger = logging.getLogger(__name__)


class MovingAverageCrossover(BaseStrategy):
    """
    Placeholder for a Simple Moving Average crossover strategy.

    Args:
        short_window: Number of periods for the short (fast) SMA.
        long_window:  Number of periods for the long  (slow) SMA.
    """

    def __init__(self, short_window: int = 9, long_window: int = 21):
        super().__init__(name="MovingAverageCrossover")

        if short_window >= long_window:
            raise ValueError("short_window must be less than long_window.")

        self.short_window = short_window
        self.long_window = long_window

        # TODO: Store historical price data in a structure that supports
        #       efficient rolling-window calculations (e.g., a pandas
        #       DataFrame or a collections.deque).
        self.price_history: dict = {}  # symbol -> list of closing prices

        logger.info(
            "MovingAverageCrossover strategy loaded (short=%s, long=%s)",
            short_window,
            long_window,
        )

    def generate_signals(self, prices: dict) -> dict:
        """
        Generate BUY / SELL / HOLD signals based on SMA crossover.

        Args:
            prices: dict mapping symbol -> latest closing price (float).
                    TODO: Update this to accept full OHLCV bar data once
                          the Trader is able to supply it.

        Returns:
            dict mapping symbol -> "BUY" | "SELL" | "HOLD"

        TODO: Implement the actual SMA calculation and crossover detection.
        TODO: Add a minimum history requirement – do not emit a signal
              until at least `long_window` data points have been collected.
        TODO: Research signal smoothing to avoid "whipsaw" (rapid back-and-
              forth signals caused by noise in the price data).
        """
        signals = {}

        for symbol, price in prices.items():
            # ── Step 1: Append the latest price to history ───
            if symbol not in self.price_history:
                self.price_history[symbol] = []
            self.price_history[symbol].append(price)

            history = self.price_history[symbol]

            # ── Step 2: Check if we have enough data ─────────
            if len(history) < self.long_window:
                # Not enough data yet; hold.
                # TODO: Log how many more data points are needed.
                signals[symbol] = "HOLD"
                continue

            # ── Step 3: Calculate moving averages ────────────
            # TODO: Replace these placeholder lines with real SMA math:
            #   short_sma = sum(history[-self.short_window:]) / self.short_window
            #   long_sma  = sum(history[-self.long_window:])  / self.long_window
            short_sma = float("nan")  # Placeholder until calculation is implemented
            long_sma = float("nan")   # Placeholder until calculation is implemented

            # ── Step 4: Detect crossover and emit signal ─────
            # TODO: Implement crossover detection:
            #   prev_short_sma = sum(history[-self.short_window-1:-1]) / self.short_window
            #   prev_long_sma  = sum(history[-self.long_window-1:-1])  / self.long_window
            #
            #   if prev_short_sma <= prev_long_sma and short_sma > long_sma:
            #       signals[symbol] = "BUY"   # golden cross
            #   elif prev_short_sma >= prev_long_sma and short_sma < long_sma:
            #       signals[symbol] = "SELL"  # death cross
            #   else:
            #       signals[symbol] = "HOLD"

            signals[symbol] = "HOLD"  # Default until implemented
            logger.debug(
                "%s | short_sma=%s long_sma=%s signal=%s",
                symbol, short_sma, long_sma, signals[symbol],
            )

        return signals
