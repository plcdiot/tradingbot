from datetime import datetime
from TradingBot.Core.EventBus import EventBus
from TradingBot.Core.Event import Event
from TradingBot.Core.EventType import EventType

def test_publish():
 b=EventBus();x=[];b.subscribe(EventType.TICK,lambda e:x.append(e.payload['p']));b.publish(Event(EventType.TICK,datetime.now(),{'p':1}));assert x==[1]
