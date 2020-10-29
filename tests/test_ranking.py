import unittest
from hodolbot.ranking import get_programming, get_anime


class TestRanking(unittest.TestCase):
    def test_get_programming(self):
        programming = get_programming()
        self.assertIsNotNone(programming)
    
    def test_get_anime(self):
        anime = get_anime()
        self.assertIsNotNone(anime)


if __name__ == '__main__':
    unittest.main()
