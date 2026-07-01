from dataclasses import dataclass
from typing import List
@dataclass(slots=True)
class Signal:
 symbol:str
 action:str
 confidence:float
 reasons:List[str]
