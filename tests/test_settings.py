from TradingBot.Config.settings import Settings

def test_settings():
    s=Settings()
    assert hasattr(s,"environment")
