from dataclasses import dataclass
from datetime import datetime
from .EventType import EventType
@dataclass(slots=True)
class Event:
    event_type:EventType
    timestamp:datetime
    payload:dict
