import unittest
import nflgame

class TestLive(unittest.TestCase):

    def test_get_current_year_and_week(self):
        year, week = nflgame.live.current_year_and_week()

        self.assertNotEqual(year, None)
        self.assertNotEqual(week, None)


if __name__ == '__main__':
    unittest.main()
