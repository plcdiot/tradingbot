from dataclasses import dataclass

@dataclass
class Position:
    symbol:str
    qty:int
    pnl:float=0.0
