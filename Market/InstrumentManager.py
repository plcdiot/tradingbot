import pandas as pd

class InstrumentManager:
    def __init__(self, csv_path:str):
        self.df=pd.read_csv(csv_path)

    def search(self, exchange:str, name:str):
        q=self.df[
            (self.df["exchange"]==exchange) &
            (self.df["tradingsymbol"].str.contains(name, case=False))
        ]
        return q

    def by_token(self, token:int):
        return self.df[self.df["instrument_token"]==token]
