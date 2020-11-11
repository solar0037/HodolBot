import time
import unittest
from hodolbot.ranking import get_programming, get_anime


class TestRanking(unittest.TestCase):
    def test_get_programming(self):
        programming = get_programming()
        self.assertIsNotNone(programming)
        time.sleep(0.1)
    
    def test_get_anime(self):
        anime = get_anime()
        self.assertIsNotNone(anime)
        time.sleep(0.1)


if __name__ == '__main__':
    unittest.main()
