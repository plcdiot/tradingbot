from kiteconnect import KiteTicker

class KiteLive:
    def __init__(self, api_key:str, access_token:str):
        self.api_key=api_key
        self.access_token=access_token
        self.kws=KiteTicker(api_key, access_token)
        self._callbacks={}

    def register(self,name,fn):
        self._callbacks[name]=fn

    def connect(self):
        if "ticks" in self._callbacks:
            self.kws.on_ticks=self._callbacks["ticks"]
        if "connect" in self._callbacks:
            self.kws.on_connect=self._callbacks["connect"]
        self.kws.connect(threaded=True)
