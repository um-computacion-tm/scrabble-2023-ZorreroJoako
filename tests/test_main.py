import unittest
from unittest.mock import patch
from game.main import *

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

    def test_menu(self):
        main = Main()
        self.assertEqual(main.menu('menu'), '''    Menu
    1) Ver tablero
    2) Ver Atril
    3) Ver Acciones
    4) Ver Puntuaciones
    Seleccion: ''')

    def test_menu_actions(self):
        main = Main()
        self.assertEqual(main.menu('actions'), '''    Acciones
    1) Colocar palabra
    2) Pasar turno
    3) Cambiar fichas
    4) Salir
    Seleccion: ''')

    def test_menu_scores(self):
        main = Main()
        self.assertEqual(main.menu('scores'), '''    Puntuaciones
    1) Ver puntuaciones
    2) Salir
    Seleccion: ''')

    def test_menu_board(self):
        main = Main()
        self.assertEqual(main.menu('board'), '''    Tablero
    1) Ver tablero
    2) Salir
    Seleccion: ''')

    def test_menu_rack(self):
        main = Main()
        self.assertEqual(main.menu('rack'), '''    Atril
    1) Ver atril
    2) Salir
    Seleccion: ''')

    def test_menu_change_tiles(self):
        main = Main()
        self.assertEqual(main.menu('change_tiles'), '''    Cambiar fichas
    1) Cambiar fichas
    2) Salir
    Seleccion: ''')
        
if __name__ == '__main__':
    unittest.main()