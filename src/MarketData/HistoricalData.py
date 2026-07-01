class HistoricalData:
    """Historical candle provider."""

    def get_candles(self, instrument_token, start, end, interval):
        raise NotImplementedError
