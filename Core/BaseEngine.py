from abc import ABC, abstractmethod
from .EngineResult import EngineResult
class BaseEngine(ABC):
    def __init__(self,name:str): self.name=name
    @abstractmethod
    def evaluate(self,market_snapshot)->EngineResult: ...
