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

    def test_view_players_lectern(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.view_players_lectern()
        assert True
    
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

    def test_view_scores(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.players[0].score = 10
        scrabble_game.players[1].score = 20
        scrabble_game.players[2].score = 30
        self.assertEqual(scrabble_game.view_scores(),''': 10
: 20
: 30
''')

    def test_view_board(self):
        scrabble_game = ScrabbleGame(players_count=3)
        result = scrabble_game.view_board()
        expected = """ 
 0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  
A   3W|  |  |2L|  |  |  |3W|  |  |  |2L|  |  |3W|
B     |2W|  |  |  |3L|  |  |  |3L|  |  |  |2W|  |
C     |  |2W|  |  |  |2L|  |2L|  |  |  |2W|  |  |
D   2L|  |  |2W|  |  |  |2L|  |  |  |2W|  |  |2L|
E     |  |  |  |2W|  |  |  |  |  |2W|  |  |  |  |
F     |3L|  |  |  |3L|  |  |  |3L|  |  |  |3L|  |
G     |  |2L|  |  |  |2L|  |2L|  |  |  |2L|  |  |
H   3W|  |  |2L|  |  |  |2W|  |  |  |2L|  |  |3W|
I     |  |2L|  |  |  |2L|  |2L|  |  |  |2L|  |  |
J     |3L|  |  |  |3L|  |  |  |3L|  |  |  |3L|  |
K     |  |  |  |2W|  |  |  |  |  |2W|  |  |  |  |
L   2L|  |  |2W|  |  |  |2L|  |  |  |2W|  |  |2L|
M     |  |2W|  |  |  |2L|  |2L|  |  |  |2W|  |  |
N     |2W|  |  |  |3L|  |  |  |3L|  |  |  |2W|  |
O   3W|  |  |2L|  |  |  |3W|  |  |  |2L|  |  |3W|
"""
        self.maxDiff = None
        self.assertEqual(result, expected)


    
if __name__ == '__main__':
    unittest.main()