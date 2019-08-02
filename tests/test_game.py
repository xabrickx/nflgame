import unittest
import nflgame

class TestGame(unittest.TestCase):

    def test_game_can_query_by_week(self):
        games = nflgame.games(2013, week=1)

        self.assertEqual(len(games), 16)


if __name__ == '__main__':
    unittest.main()
