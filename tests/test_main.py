import unittest
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

    # def test_menu(self):
    #     main = Main()
    #     result = main.menu('menu', scrabble_game)
    #     expected = '''    Menu
    # 1) Tablero
    # 2) Atril
    # 3) Acciones
    # 4) Puntuaciones
    # Seleccion: '''

    #     self.maxDiff = None
    #     self.assertEqual(result, expected)


#     def test_menu_board(self):
#         main = Main()
#         self.assertEqual(main.menu('board', scrabble_game), '''    Tablero
#     1) Ver tablero
#     2) Salir
#     Seleccion: ''')

#     def test_menu_rack(self):
#         main = Main()
#         self.assertEqual(main.menu('rack', scrabble_game), '''    Atril
#     1) Ver atril
#     2) Salir
#     Seleccion: ''')

#     def test_menu_actions(self):
#         main = Main()
#         self.assertEqual(main.menu('actions', scrabble_game), '''    Acciones
#     1) Colocar palabra
#     2) Pasar turno
#     3) Cambiar fichas
#     4) Salir
#     Seleccion: ''')

#     def test_menu_put_word(self):
#         main = Main()
#         self.assertEqual(main.menu('put_word', scrabble_game), '''    Colocar palabra
#     1) Colocar palabra
#     2) Salir
#     Seleccion: ''')

    # def test_menu_next_turn(self):
    #     main = Main()
    #     self.assertEqual(main.menu('next_turn', scrabble_game), '''    Pasar turno
    # 1) Pasar turno
    # 2) Salir
    # Seleccion: ''')

#     def test_menu_change_tiles(self):
#         main = Main()
#         self.assertEqual(main.menu('change_tiles', scrabble_game), '''    Cambiar fichas
#     1) Cambiar fichas
#     2) Salir
#     Seleccion: ''')
        
    

#     def test_menu_scores(self):
#         main = Main()
#         self.assertEqual(main.menu('scores', scrabble_game), '''    Puntuaciones
#     1) Ver puntuaciones
#     2) Salir
#     Seleccion: ''')

    
if __name__ == '__main__':
    unittest.main()