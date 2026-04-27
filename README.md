# AutoTrader

This is a senior project for designing, testing, and implementing an automated cryptocurrency and stock trader using the [Alpaca](https://alpaca.markets/) brokerage API.

> ⚠️ **This is a prototype / skeleton layout only. It is NOT a functional trading bot.**
> Many sections contain `TODO` comments indicating what needs to be researched and implemented.

---

## Project Structure

```
AutoTrader/
├── main.py                          # Entry point – run this to start the bot
├── requirements.txt                 # Python dependencies
├── .env.example                     # Template for API credentials (copy to .env)
└── alpaca_trader/
    ├── config.py                    # Configuration & environment variables
    ├── trader.py                    # Core Trader class (API connection, orders)
    ├── strategies/
    │   ├── base_strategy.py         # Abstract base class for all strategies
    │   └── moving_average.py        # Placeholder SMA crossover strategy
    └── utils/
        └── helpers.py               # Shared utility functions
```

## Getting Started

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up credentials**
   ```bash
   cp .env.example .env
   # Edit .env and add your Alpaca paper-trading API key and secret
   ```

3. **Run the skeleton**
   ```bash
   python main.py
   ```
   The bot will start and immediately exit – no trades will be placed until the `TODO` sections are implemented.

## Key Areas to Research & Implement

- [ ] Alpaca REST API and WebSocket streaming
- [ ] Order types: market, limit, stop, stop-limit, trailing stop
- [ ] Position sizing strategies (fixed fractional, Kelly criterion, ATR-based)
- [ ] Technical indicators: SMA, EMA, MACD, RSI, Bollinger Bands
- [ ] Backtesting framework (Backtrader, VectorBT, or Zipline)
- [ ] Risk management: max daily loss, circuit breakers, correlation limits
- [ ] Scheduling / market-hours awareness (Alpaca `/v2/clock` endpoint)
- [ ] Persistent state (database storage so the bot survives restarts)
- [ ] Alerting: Slack / email notifications on errors or large P&L moves
- [ ] Deployment: Docker, systemd, or a cloud VM for 24/7 uptime

## Resources

- [Alpaca Documentation](https://alpaca.markets/docs/)
- [alpaca-trade-api Python SDK](https://github.com/alpacahq/alpaca-trade-api-python)
- [alpaca-py (newer SDK)](https://alpaca.markets/sdks/python/)
- [Alpaca Paper Trading](https://app.alpaca.markets/) – free simulated account

