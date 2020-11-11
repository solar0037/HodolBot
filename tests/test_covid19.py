import unittest
from hodolbot.covid19 import get_covid19


class TestCovid19(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.covid19 = get_covid19()

    def test_get_covid19(self):
        self.assertIsNotNone(self.covid19)


if __name__ == '__main__':
    unittest.main()
