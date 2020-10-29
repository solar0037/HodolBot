import unittest
from hodolbot.stock import get_stock


class TestStock(unittest.TestCase):
    def test_get_stock(self):
        stock = get_stock()
        self.assertIsNotNone(stock)


if __name__ == '__main__':
    unittest.main()
