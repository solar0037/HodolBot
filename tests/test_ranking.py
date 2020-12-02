from hodolbot.ranking import get_programming, get_anime

def test_get_programming():
    assert get_programming() is not None

def test_get_anime():
    assert get_anime() is not None
