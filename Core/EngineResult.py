from dataclasses import dataclass, field
from typing import List
@dataclass(slots=True)
class EngineResult:
    engine:str
    score:float
    probability:float
    bullish:bool
    bearish:bool
    reasons:List[str]=field(default_factory=list)
