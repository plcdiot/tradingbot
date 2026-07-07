
from .indicator_base import Indicator

class EMAIndicator(Indicator):
    def __init__(self, period:int):
        self.period=period

    def calculate(self, values):
        if not values:
            return None
        k=2/(self.period+1)
        ema=values[0]
        for price in values[1:]:
            ema=price*k+ema*(1-k)
        return ema
