# ============================================================
# strategies/base_strategy.py - Abstract Base Strategy
# ============================================================
# All concrete trading strategies should inherit from BaseStrategy
# and implement the generate_signals() method.
#
# Having a common interface makes it easy to:
#   - Swap strategies without changing the Trader class
#   - Backtest multiple strategies against the same historical data
#   - Unit-test each strategy in isolation
#
# TODO: Research the following strategy types and decide which to
#       implement first:
#
#   Trend-following strategies (good for sustained moves):
#     - Moving Average Crossover (SMA/EMA cross)
#     - MACD (Moving Average Convergence Divergence)
#     - Donchian Channel breakout
#
#   Mean-reversion strategies (good for range-bound markets):
#     - Bollinger Band squeeze / reversion
#     - RSI (Relative Strength Index) overbought/oversold
#     - Pairs trading (statistical arbitrage)
#
#   Momentum strategies:
#     - Rate of Change (ROC)
#     - Dual Momentum (relative momentum between assets)
#
#   Machine-learning based strategies (advanced):
#     - LSTM / time-series forecasting
#     - Reinforcement learning (RL) agents
#     - Sentiment analysis on news/social media
#
# TODO: Research backtesting frameworks (e.g., Backtrader, Zipline,
#       VectorBT) to evaluate strategy performance on historical data
#       before trading live or with paper money.
# TODO: Research walk-forward optimization to avoid over-fitting
#       strategy parameters to historical data.
# ============================================================

from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    """
    Abstract base class for all trading strategies.

    Subclasses must implement:
        generate_signals(prices) -> dict[str, str]
    """

    def __init__(self, name: str = "BaseStrategy"):
        """
        Args:
            name: Human-readable name for this strategy (used in logs).

        TODO: Accept strategy-specific hyperparameters (e.g., lookback
              period, threshold values) in __init__ so they can be tuned
              without subclassing.
        """
        self.name = name

    @abstractmethod
    def generate_signals(self, prices: dict) -> dict:
        """
        Analyze the provided price data and return trading signals.

        Args:
            prices: dict mapping symbol -> price data.
                    The exact shape (latest price, OHLCV bars, etc.)
                    depends on what the Trader passes in.
                    TODO: Define and document a standard price data
                          schema so all strategies use the same format.

        Returns:
            dict mapping symbol -> signal string.
            Suggested signal values:
              "BUY"  - open or add to a long position
              "SELL" - close an existing long position
              "HOLD" - take no action

            TODO: Research more granular signal types, e.g.:
              "SHORT" (open a short position – requires margin account)
              "SCALE_IN" / "SCALE_OUT" (partial position adjustments)
        """
        raise NotImplementedError

    def on_market_open(self):
        """
        Hook called once when the market opens each day.

        TODO: Use this to reset daily counters, refresh indicators,
              or place pre-market orders.
        """
        # TODO: Implement in subclasses as needed.
        pass

    def on_market_close(self):
        """
        Hook called once when the market is about to close.

        TODO: Use this to close intraday positions, log daily P&L,
              or prepare the watchlist for the next session.
        """
        # TODO: Implement in subclasses as needed.
        pass
