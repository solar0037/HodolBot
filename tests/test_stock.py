from hodolbot.stock import get_stock

def test_get_stock():
    assert get_stock() is not None
