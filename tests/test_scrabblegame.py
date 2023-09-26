import unittest
from game.scrabblegame import *

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        game = ScrabbleGame(players_count=2)
        self.assertEqual(game.players_count,2)
        self.assertEqual(len(game.players),2)
        self.assertEqual(type(game.board),Board)
        self.assertEqual(type(game.tilebag),BagTile)
        self.assertIsNone(game.current_player)
        self.assertFalse(game.game_over)
    
    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        self.assertEqual (scrabble_game.current_player, scrabble_game.players[0])
    
    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        self.assertEqual (scrabble_game.current_player, scrabble_game.players[1])

    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        self.assertEqual (scrabble_game.current_player, scrabble_game.players[0])
if __name__ == '__main__':
    unittest.main()