from collections import defaultdict
class EventBus:
    def __init__(self): self._h=defaultdict(list)
    def subscribe(self,t,h): self._h[t].append(h)
    def publish(self,e):
        [h(e) for h in self._h[e.event_type]]
