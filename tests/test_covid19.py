from hodolbot.covid19 import get_covid19

def test_get_covid19():
    assert get_covid19() is not None
