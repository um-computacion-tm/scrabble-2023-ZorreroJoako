import unittest
from game.board import *
from game.tilebag import Tile
from game.cell  import Cell
from unittest.mock import patch



class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid),15)
        self.assertEqual(len(board.grid[0]),15)

    def test_simple(self):
        cell_1 = Cell(multiplier=1,multiplier_type="letter")
        cell_1.add_letter(Tile('C', 1)) 
        cell_2 = Cell(multiplier=1,multiplier_type="letter")
        cell_2.add_letter(Tile('A', 1))
        cell_3 = Cell(multiplier=1,multiplier_type="letter")
        cell_3.add_letter(Tile('S', 2))
        cell_4 = Cell(multiplier=1,multiplier_type="letter")
        cell_4.add_letter(Tile('A', 1))

        word = [cell_1, cell_2, cell_3, cell_4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 5)
    
    def test_letter_multiplier(self):
        cell_1 = Cell(multiplier=1,multiplier_type="letter")
        cell_1.add_letter(Tile('C', 1)) 
        cell_2 = Cell(multiplier=1,multiplier_type="letter")
        cell_2.add_letter(Tile('A', 1))
        cell_3 = Cell(multiplier=2,multiplier_type="letter")
        cell_3.add_letter(Tile('S', 2))
        cell_4 = Cell(multiplier=1,multiplier_type="letter")
        cell_4.add_letter(Tile('A', 1))

        word = [cell_1, cell_2, cell_3, cell_4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 7)
    
    def test_word_multiplier(self):
        cell_1 = Cell(multiplier=1,multiplier_type="letter")
        cell_1.add_letter(Tile('C', 1)) 
        cell_2 = Cell(multiplier=1,multiplier_type="letter")
        cell_2.add_letter(Tile('A', 1))
        cell_3 = Cell(multiplier=2,multiplier_type="word")
        cell_3.add_letter(Tile('S', 2))
        cell_4 = Cell(multiplier=1,multiplier_type="letter")
        cell_4.add_letter(Tile('A', 1))

        word = [cell_1, cell_2, cell_3, cell_4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_letter_and_word_multiplier(self):
        cell_1 = Cell(multiplier=2,multiplier_type="letter")
        cell_1.add_letter(Tile('C', 1)) 
        cell_2 = Cell(multiplier=1,multiplier_type="letter")
        cell_2.add_letter(Tile('A', 1))
        cell_3 = Cell(multiplier=2,multiplier_type="word")
        cell_3.add_letter(Tile('S', 2))
        cell_4 = Cell(multiplier=1,multiplier_type="letter")
        cell_4.add_letter(Tile('A', 1))

        word = [cell_1, cell_2, cell_3, cell_4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 12)

    @patch('game.board.dle.search_by_word')
    def test_len_of_word_in_board_x(self,mock_search_by_word):
        mock_search_by_word.return_value.title = 'facultad | Definición | Diccionario de la lengua española | RAE - ASALE'
        board= Board()
        word='facultad'
        location=(7,4)
        orientation='H'
        self.assertEqual(board.validate_len_of_word_in_board(word,location,orientation),True)

    @patch('game.board.dle.search_by_word')
    def test_len_of_word_in_board_y(self,mock_search_by_word):
        mock_search_by_word.return_value.title = 'facultad | Definición | Diccionario de la lengua española | RAE - ASALE'
        board= Board()
        word='facultad'
        location=(7,4)
        orientation='V'
        self.assertEqual(board.validate_len_of_word_in_board(word,location,orientation),True)

    @patch('game.board.dle.search_by_word')
    def test_len_of_word_out_of_board_x(self,mock_search_by_word):
        mock_search_by_word.return_value.title = 'facultad | Definición | Diccionario de la lengua española | RAE - ASALE'
        board= Board()
        word='facultad'
        location=(10,5)
        orientation='H'
        self.assertEqual(board.validate_len_of_word_in_board(word,location,orientation),False)

    @patch('game.board.dle.search_by_word')
    def test_len_of_word_out_of_board_y(self,mock_search_by_word):
        mock_search_by_word.return_value.title = 'facultad | Definición | Diccionario de la lengua española | RAE - ASALE'
        board= Board()
        word='facultad'
        location=(5,10)
        orientation='V'
        self.assertEqual(board.validate_len_of_word_in_board(word,location,orientation),False)

    def test_board_empty(self):
        board = Board()
        self.assertEqual(board.board_empty(),True) 
        
    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        self.assertEqual(board.board_empty(),False)

    @patch('game.board.dle.search_by_word')
    def test_place_word_empty_board_horizontal_fine(self,mock_search_by_word):
        mock_search_by_word.return_value.title = 'facultad | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        self.assertEqual(board.validate_word_place_board(word, location, orientation),True)

    @patch('game.board.dle.search_by_word')
    def test_place_word_empty_board_horizontal_wrong(self,mock_search_by_word):
        mock_search_by_word.return_value.title = 'facultad | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "H"
        self.assertEqual(board.validate_word_place_board(word, location, orientation),False)

    @patch('game.board.dle.search_by_word')
    def test_place_word_empty_board_vertical_fine(self,mock_search_by_word):
        mock_search_by_word.return_value.title = 'facultad | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = "Facultad"
        location = (4, 7)
        orientation = "V"
        self.assertEqual(board.validate_word_place_board(word, location, orientation),True)

    @patch('game.board.dle.search_by_word')
    def test_place_word_empty_board_vertical_wrong(self,mock_search_by_word):
        mock_search_by_word.return_value.title = 'facultad | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "V"
        self.assertEqual(board.validate_word_place_board(word, location, orientation),False)
    
    @patch('game.board.dle.search_by_word')
    def test_invalidate_word_place_board(self,mock_search_by_word):
        mock_search_by_word.return_value.title = 'facultad | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        self.assertEqual(board.validate_word_place_board(word, location, orientation),False)
    
    
    @patch('game.board.dle.search_by_word')
    def test_place_word_not_empty_board_horizontal_fine(self,mock_search_by_word):
        mock_search_by_word.return_value.title = 'facultad | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        board.grid[7][7].letter = Tile('C',3)
        board.grid[8][7].letter = Tile('A',1)
        board.grid[9][7].letter = Tile('S',6)
        board.grid[10][7].letter = Tile('A',1) 
        word = "FACULTAD"
        location = (7, 5)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)
    
    @patch('game.board.dle.search_by_word')
    def test_place_word_not_empty_board_vertical_fine(self,mock_search_by_word):
        mock_search_by_word.return_value.title = 'facultad | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        board.grid[7][7].letter = Tile('C',3)
        board.grid[7][8].letter = Tile('A',1)
        board.grid[7][9].letter = Tile('S',6)
        board.grid[7][10].letter = Tile('A',1) 
        word = "FACULTAD"
        location = (5, 7)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertEqual(word_is_valid, True)
    
    @patch('game.board.dle.search_by_word')
    def test_valid_word_with_rae(self,mock_search_by_word):
        mock_search_by_word.return_value.title = 'facultad | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = "FACULTAD"
        self.assertEqual(board.validate_words_with_rae(word), True)

    @patch('game.board.dle.search_by_word')
    def test_invalid_word_with_rae(self,mock_search_by_word):
        mock_search_by_word.return_value.title = 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE'
        board = Board()
        word = "asdfghj"
        self.assertEqual(board.validate_words_with_rae(word), False)

    def test_valid_accent_word(self):
        board = Board()
        word = "Árbol"
        self.assertEqual(board.words_with_accent(word), 'ARBOL')

    def test_valid_accent_rest_of_words(self):
        board = Board()
        word1 = "Éste"
        word2 = "ahí"
        word3 = "cocción"
        word4 = "última"
        self.assertEqual(board.words_with_accent(word1), 'ESTE')
        self.assertEqual(board.words_with_accent(word2), 'AHI')
        self.assertEqual(board.words_with_accent(word3), 'COCCION')
        self.assertEqual(board.words_with_accent(word4), 'ULTIMA')
    
    def test_show_board_empty(self):
        board = Board()
        result = board.show_board()
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
        
    def test_show_board(self):
        board = Board()
        board.grid[7][7].letter = Tile('C',3)
        board.grid[8][7].letter = Tile('A',1)
        board.grid[9][7].letter = Tile('S',6)
        board.grid[10][7].letter = Tile('A',1)
        result = board.show_board()
        expected = """ 
 0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  
A   3W|  |  |2L|  |  |  |3W|  |  |  |2L|  |  |3W|
B     |2W|  |  |  |3L|  |  |  |3L|  |  |  |2W|  |
C     |  |2W|  |  |  |2L|  |2L|  |  |  |2W|  |  |
D   2L|  |  |2W|  |  |  |2L|  |  |  |2W|  |  |2L|
E     |  |  |  |2W|  |  |  |  |  |2W|  |  |  |  |
F     |3L|  |  |  |3L|  |  |  |3L|  |  |  |3L|  |
G     |  |2L|  |  |  |2L|  |2L|  |  |  |2L|  |  |
H   3W|  |  |2L|  |  |  |C |  |  |  |2L|  |  |3W|
I     |  |2L|  |  |  |2L|A |2L|  |  |  |2L|  |  |
J     |3L|  |  |  |3L|  |S |  |3L|  |  |  |3L|  |
K     |  |  |  |2W|  |  |A |  |  |2W|  |  |  |  |
L   2L|  |  |2W|  |  |  |2L|  |  |  |2W|  |  |2L|
M     |  |2W|  |  |  |2L|  |2L|  |  |  |2W|  |  |
N     |2W|  |  |  |3L|  |  |  |3L|  |  |  |2W|  |
O   3W|  |  |2L|  |  |  |3W|  |  |  |2L|  |  |3W|
""" 
        self.maxDiff = None
        self.assertEqual(result, expected)
    
    @patch('game.board.dle.search_by_word')
    def test_put_word_valid_horizontal(self, mock_search_by_word):
        mock_search_by_word.return_value.title ='casa | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = "Casa"
        location = (7, 7)
        orientation = "H"
        board.put_word(word, location, orientation)
        self.assertEqual(board.grid[7][7].letter, "C")
        self.assertEqual(board.grid[7][8].letter, "A")
        self.assertEqual(board.grid[7][9].letter, "S")
        self.assertEqual(board.grid[7][10].letter, "A")

    @patch('game.board.dle.search_by_word')
    def test_put_word_valid_vertical(self, mock_search_by_word):
        mock_search_by_word.return_value.title ='casa | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = "Casa"
        location = (7, 7)
        orientation = "V"
        board.put_word(word, location, orientation)
        self.assertEqual(board.grid[7][7].letter, "C")
        self.assertEqual(board.grid[8][7].letter, "A")
        self.assertEqual(board.grid[9][7].letter, "S")
        self.assertEqual(board.grid[10][7].letter, "A")
        
    @patch('game.board.dle.search_by_word')
    def test_put_word_invalid(self, mock_search_by_word):
        mock_search_by_word.return_value.title = 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE'
        board = Board()
        word = "asdfghj"
        location = (7, 7)
        orientation = "H"
        board.put_word(word, location, orientation)
        self.assertEqual(board.grid[7][7].letter, None)
        self.assertEqual(board.grid[7][8].letter, None)
        self.assertEqual(board.grid[7][9].letter, None)
        self.assertEqual(board.grid[7][10].letter, None)
        self.assertEqual(board.grid[7][11].letter, None)
        self.assertEqual(board.grid[7][12].letter, None)


if __name__ == '__main__':
    unittest.main()