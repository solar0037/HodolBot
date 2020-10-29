import unittest
from hodolbot.covid19 import get_covid19


class TestCovid19(unittest.TestCase):
    def test_get_covid19(self):
        covid19 = get_covid19()
        self.assertIsNotNone(covid19)


if __name__ == '__main__':
    unittest.main()
