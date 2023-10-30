import unittest
import io, sys
from unittest.mock import patch
from game.main import *
from game.scrabblegame import *

class TestMain(unittest.TestCase):
    def test_main(self):
        with patch('builtins.input', side_effect=[2]):
            main = Main()
            self.assertEqual(main.main(), 2)

    def test_main_fail(self):
        with patch('builtins.input', side_effect=[1, 5, 2]):
            main = Main()
            self.assertEqual(main.main(), 2)

    def test_main_fail2(self):
        with patch('builtins.input', side_effect=[1, 5, 2]):
            main = Main()
            self.assertNotEqual(main.main(), 1)

    def test_view_menu(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('menu', scrabble_game)
        expected = '''Turno del jugador Jugador 1

    Menu
    1) Ver tablero
    2) Ver Atril
    3) Ver Acciones
    4) Ver Puntuaciones
    Seleccion: '''
        self.maxDiff = None
        self.assertEqual(result, expected)

    def test_view_menu_board(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('board', scrabble_game)
        expected = '''Turno del jugador 1

    Tablero
    1) Ver tablero
    2) Salir'''

    def test_view_menu_rack(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('rack', scrabble_game)
        expected = '''Turno del jugador 1

    Atril
    1) Ver atril
    2) Salir
    Seleccion:'''

    def test_view_menu_actions(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('actions', scrabble_game)
        expected = '''Turno del jugador 1

    Acciones
    1) Colocar palabra
    2) Cambiar fichas
    3) Pasar turno
    4) Salir
    Seleccion:'''

    def test_view_menu_put_word(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('put_word', scrabble_game)
        expected = '''Turno del jugador 1

    Colocar palabra
    1) Colocar palabra
    2) Salir
    Seleccion:'''

    def test_view_menu_change_tiles(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('change_tiles', scrabble_game)
        expected = '''Turno del jugador 1

    Cambiar fichas
    1) Cambiar fichas
    2) Salir
    Seleccion:'''

    def test_view_menu_next_turn(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('next_turn', scrabble_game)
        expected = '''Turno del jugador 1

    Pasar turno
    1) Pasar turno
    2) Salir
    Seleccion:'''


    def test_view_menu_scores(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('scores', scrabble_game)
        expected = '''Turno del jugador 1

    Puntuaciones
    1) Ver puntuaciones
    2) Salir
    Seleccion:'''    
    
    @patch('builtins.input', side_effect=[1,2])
    def test_menu_board(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_board(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = ''' 
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

'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[7,2])
    def test_menu_board_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_board(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor no valido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)
    
    @patch('builtins.input', side_effect=[1,2])
    def test_menu_rack(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        scrabble_game.players[0].tiles = [Tile('L',1),Tile('D',1),Tile('V',1),Tile('D',1),Tile('C',1),Tile('L',1),Tile('H',1)]
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_rack(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''                     ATRIL

Letras ->  | L | D | V | D | C | L | H |
'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[7,2])
    def test_menu_rack_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_rack(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor no valido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)
    
    @patch('builtins.input', side_effect=[1,4])
    def test_menu_actions_1(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        with patch.object(main, 'menu_put_word') as mock_put_word:
            main.menu_actions(scrabble_game)
            mock_put_word.assert_called_once()


    @patch('builtins.input', side_effect=[2,4])
    def test_menu_actions_2(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        with patch.object(main, 'menu_change_tiles') as mock_change_tiles:
            main.menu_actions(scrabble_game)
            mock_change_tiles.assert_called_once()
    
    @patch('builtins.input', side_effect=[3,4])
    def test_menu_actions_3(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        with patch.object(main, 'menu_next_turn') as mock_next_turn:
            main.menu_actions(scrabble_game)
            mock_next_turn.assert_called_once()

    @patch('builtins.input', side_effect=[3,3,4])
    @patch('game.main.Main.menu_next_turn', return_value='cambio de turno')
    def test_menu_actions_3_next_turn(self,mock_input, mock_next_turn):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        main.menu_actions(scrabble_game)

    @patch('builtins.input', side_effect=[7,4])
    def test_menu_actions_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_actions(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor no valido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    # @patch('builtins.input', side_effect=[1,"2,3"])
    # @patch('game.tilebag.BagTile.take_tiles')
    # def test_menu_actions_change_tiles(self, mock_input, mock_take):
    #     main = Main()
    #     scrabble_game = ScrabbleGame(2)
    #     scrabble_game.players[0].name = 'Jugador 1'
    #     scrabble_game.players[1].name = 'Jugador 2'
    #     scrabble_game.next_turn()
    #     tileA = Tile('A', 1)
    #     tileB = Tile('B', 1)
    #     mock_take.return_value = [tileA, tileA]
    #     next_player = scrabble_game.players[0]
    #     scrabble_game.players[0].tiles = [tileB, tileB, tileB, tileB, tileB, tileB, tileB]
    #     main.menu_change_tiles(scrabble_game)
    #     self.assertEqual(scrabble_game.players[0].tiles, [tileA, tileA, tileB, tileB, tileB, tileB, tileB])
    #     self.assertEqual(next_player, scrabble_game.current_player) 

    @patch('builtins.input', side_effect=[7,2])
    def test_menu_actions_change_tiles_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_change_tiles(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor no valido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[1,2])
    def test_menu_actions_next_turn(self, mock_input):
        main = Main ()
        scrabble_game = ScrabbleGame (2)
        scrabble_game.players [0] .name = 'Jugador 1'
        scrabble_game.players [1] .name = 'Jugador 2'
        scrabble_game.next_turn ()
        self.assertEqual(main.menu_next_turn (scrabble_game), 'cambio de turno')
    
    @patch('builtins.input', side_effect=[7,2])
    def test_menu_actions_next_turn_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_next_turn(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor no valido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[1,2])
    def test_menu_actions_scores(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_scores(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Jugador 1: 0\nJugador 2: 0\n
'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[7,2])
    def test_menu_actions_scores_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_scores(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor no valido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    



if __name__ == '__main__':
    unittest.main()