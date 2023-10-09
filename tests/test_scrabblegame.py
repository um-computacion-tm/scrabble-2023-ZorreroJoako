import unittest
from game.scrabblegame import *
from game.board import *

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

    def test_end_game_when_tilebag_is_empty_and_player_tiles_are_empty(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.tilebag.tiles = []
        scrabble_game.players[0].tiles = []
        scrabble_game.players[1].tiles = []
        scrabble_game.players[2].tiles = []
        self.assertTrue(scrabble_game.end_game())

    def test_end_game_when_tilebag_is_empty(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.tilebag.tiles = []
        scrabble_game.players[0].tiles = ['A']
        scrabble_game.players[1].tiles = ['A']
        scrabble_game.players[2].tiles = ['A']
        self.assertFalse(scrabble_game.end_game())

    def test_end_game_when_player_tiles_are_empty(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.tilebag.tiles = ['A']
        scrabble_game.players[0].tiles = []
        scrabble_game.players[1].tiles = []
        scrabble_game.players[2].tiles = []
        self.assertFalse(scrabble_game.end_game())

if __name__ == '__main__':
    unittest.main()