import unittest
from hodolbot.ranking import get_programming, get_anime


class TestRanking(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.programming = get_programming()
        cls.anime = get_anime()

    def test_get_programming(self):
        self.assertIsNotNone(self.programming)
    
    def test_get_anime(self):
        self.assertIsNotNone(self.anime)


if __name__ == '__main__':
    unittest.main()
