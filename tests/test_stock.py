import unittest
from hodolbot.stock import get_stock


class TestStock(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.stock = get_stock()
    
    def test_get_stock(self):
        self.assertIsNotNone(TestStock.stock)


if __name__ == '__main__':
    unittest.main()
