from dataclasses import dataclass

@dataclass
class ConvictionResult:
    bullish:int
    bearish:int
    reason:str=""

class ConvictionEngine:
    def evaluate(self):
        return ConvictionResult(0,0,"Not implemented")
