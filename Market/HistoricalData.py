from kiteconnect import KiteConnect

class HistoricalData:
    def __init__(self, api_key:str, access_token:str):
        self.kite=KiteConnect(api_key=api_key)
        self.kite.set_access_token(access_token)

    def candles(self, instrument_token, start, end, interval="5minute"):
        return self.kite.historical_data(
            instrument_token=instrument_token,
            from_date=start,
            to_date=end,
            interval=interval
        )
