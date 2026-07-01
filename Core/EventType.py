from enum import Enum
class EventType(str,Enum):
    TICK='tick'
    CANDLE='candle'
    SIGNAL='signal'
