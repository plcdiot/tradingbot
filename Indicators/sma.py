
from .indicator_base import Indicator

class SMAIndicator(Indicator):
    def __init__(self, period:int):
        self.period=period

    def calculate(self, values):
        if len(values)<self.period:
            return None
        return sum(values[-self.period:])/self.period
