import time
import unittest
from hodolbot.stock import get_stock


class TestStock(unittest.TestCase):
    def test_get_stock(self):
        stock = get_stock()
        self.assertIsNotNone(stock)
        time.sleep(0.1)


if __name__ == '__main__':
    unittest.main()
