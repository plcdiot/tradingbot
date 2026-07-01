from src.Engine.ConvictionEngine import ConvictionEngine

def test_engine():
    r=ConvictionEngine().evaluate()
    assert r.bullish==0
