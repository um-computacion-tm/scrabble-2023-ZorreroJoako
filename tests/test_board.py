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
        word = [Tile('C',1),Tile('A',1),Tile('S',1),Tile('A',1)]
        location = (7, 7)
        orientation = "H"
        board.put_word(word, location, orientation)
        self.assertEqual(board.grid[7][7].letter.letter, "C")
        self.assertEqual(board.grid[7][8].letter.letter, "A")
        self.assertEqual(board.grid[7][9].letter.letter, "S")
        self.assertEqual(board.grid[7][10].letter.letter, "A")
    
    @patch('game.board.dle.search_by_word')
    def test_put_word_valid_vertical(self, mock_search_by_word):
        mock_search_by_word.return_value.title ='casa | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = [Tile('C',1),Tile('A',1),Tile('S',1),Tile('A',1)]
        location = (7, 7)
        orientation = "V"
        board.put_word(word, location, orientation)
        self.assertEqual(board.grid[7][7].letter.letter, "C")
        self.assertEqual(board.grid[8][7].letter.letter, "A")
        self.assertEqual(board.grid[9][7].letter.letter, "S")
        self.assertEqual(board.grid[10][7].letter.letter, "A")

    @patch('game.board.dle.search_by_word')
    def test_put_word_valid_with_previous_word(self, mock_search_by_word):
        mock_search_by_word.return_value.title ='casa | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        board.grid[7][7].letter = Tile('C',3)
        word = [Tile('A',1),Tile('S',1),Tile('A',1)]
        location = (7, 7)
        orientation = "V"
        board.put_word(word, location, orientation)
        self.assertEqual(board.grid[7][7].letter.letter, "C")
        self.assertEqual(board.grid[8][7].letter.letter, "A")
        self.assertEqual(board.grid[9][7].letter.letter, "S")
        self.assertEqual(board.grid[10][7].letter.letter, "A")

    def test_get_word_without_intersections_intersected(self):
        board = Board()
        board.grid[7][6].letter = Tile('C',3)
        board.grid[7][7].letter = Tile('A',1)
        board.grid[7][8].letter = Tile('S',1)
        board.grid[7][9].letter = Tile('A',1)
        word = 'laso'
        location = (6,7)
        orientation = "V"
        result_word = board.get_word_without_intersections(word,location,orientation)
        self.assertEqual(result_word,'lso')

    def test_get_word_without_intersections_intersected(self):
        board = Board()
        board.grid[7][7].letter = Tile('L',1)
        board.grid[7][8].letter = Tile('A',1)
        word = 'las'
        location = (7,7)
        orientation = "H"
        result_word = board.get_word_without_intersections(word,location,orientation)
        self.assertEqual(result_word,'s')

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        board = Board()        
        word = 'casa'
        pos=(10,6)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 6)

    def test_simple_with_double_letter(self):
        board = Board()
        word = 'lluvia'
        pos=(10,5)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 15)
        
    def test_with_word_multiplier_2(self):
        board = Board()        
        word = 'casa'
        pos=(7,6)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 12)

    def test_with_word_multiplier_3(self):
        board = Board()        
        word = 'casa'
        pos=(14,6)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 18)

    def test_with_letter_multiplier_2(self):
        board = Board()        
        word = 'casa'
        pos=(8,8)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 9)

    def test_with_letter_multiplier_3(self):
        board = Board()        
        word = 'casa'
        pos=(9,8)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 8)

    def test_with_letter_multiplier_and_word_multiplier(self):
        board = Board()        
        word = 'casa'
        pos=(14,0)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 21)

    def test_with_letter_multiplier_and_word_multiplier_no_active(self):
        board = Board()        
        word = 'casa'
        pos=(14,0)
        value = board.calculate_word_value(word, pos, horizontal=True)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 6)

    def test_simple_intersection(self):
        board = Board()
        board.grid[7][2].tile = Tile('E', 1)
        board.grid[7][3].tile = Tile('S', 1)
        board.grid[7][4].tile = Tile('T', 1)
        board.grid[7][5].tile = Tile('R', 1)
        board.grid[7][6].tile = Tile('E', 1)
        board.grid[7][7].tile = Tile('N', 1)
        board.grid[7][8].tile = Tile('O', 1)
        board.grid[7][7].active = False
        word = 'mes'
        pos=(6,6)
        horizontal = True
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value, 9)

    def test_simple_intersection_inverted(self):
        board = Board()
        board.grid[7][2].tile = Tile('E', 1)
        board.grid[7][3].tile = Tile('S', 1)
        board.grid[7][4].tile = Tile('T', 1)
        board.grid[7][5].tile = Tile('R', 1)
        board.grid[7][6].tile = Tile('E', 1)
        board.grid[7][7].tile = Tile('N', 1)
        board.grid[7][8].tile = Tile('O', 1)
        board.grid[7][7].active = False
        word = 'mes'
        pos=(8,6)
        horizontal = True
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value, 9)

    def test_simple_intersection_2(self):
        board = Board()
        board.grid[7][5].letter = Tile('C', 3)
        board.grid[7][6].letter = Tile('A', 1)
        board.grid[7][7].letter = Tile('S', 1)
        board.grid[7][8].letter = Tile('A', 1)
        board.grid[6][8].letter = Tile('L', 1)
        board.grid[8][8].letter = Tile('S', 1)
        board.grid[9][8].letter = Tile('O', 1)
        board.grid[9][7].letter = Tile('S', 1)
        board.grid[9][6].letter = Tile('O', 1)
        word = 'cosa'
        pos=(7,5)
        horizontal = False
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value, 14)

    def test_simple_intersection_inverted_2(self):
        board = Board()
        board.grid[7][5].tile = Tile('C', 3)
        board.grid[7][6].tile = Tile('A', 1)
        board.grid[7][7].tile = Tile('S', 1)
        board.grid[7][8].tile = Tile('A', 1)
        board.grid[8][5].tile = Tile('O', 1)
        board.grid[9][5].tile = Tile('S', 1)
        board.grid[10][5].tile = Tile('A', 1)
        board.grid[9][7].tile = Tile('S', 1)
        board.grid[9][6].tile = Tile('O', 1)
        board.grid[9][8].tile = Tile('O', 1)
        board.grid[7][7].active = False
        word = 'laso'
        pos=(5,9)
        horizontal = False
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value, 6)

    def test_simple_intersection_inverted_3(self):
        board = Board()
        board.grid[7][5].tile = Tile('C', 3)
        board.grid[7][6].tile = Tile('A', 1)
        board.grid[7][7].tile = Tile('S', 1)
        board.grid[7][8].tile = Tile('A', 1)
        board.grid[8][5].tile = Tile('O', 1)
        board.grid[9][5].tile = Tile('S', 1)
        board.grid[10][5].tile = Tile('A', 1)
        board.grid[9][7].tile = Tile('S', 1)
        board.grid[9][6].tile = Tile('O', 1)
        board.grid[9][8].tile = Tile('O', 1)
        board.grid[7][7].active = False
        board.grid[9][5].active = False
        word = 'lasos'
        pos=(5,9)
        horizontal = False
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value, 9)

    def test_out_of_range_side(self):
        board = Board()
        word = 'casa'
        pos = (14,10)
        horizontal = True
        value = board.calculate_word_value(word, pos, horizontal)
        pos = (0,0)
        horizontal = True
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value!=None, True)

    def test_letter_not_available(self):
        board = Board()
        word = 'c?sa'
        pos = (7,7)
        horizontal = True
        value = board.calculate_word_value(word,pos,horizontal)
        self.assertEqual(value, 10)

    def test_calculate_word_value_with_intersection(self):
        board = Board()
        board.grid[7][7].letter = Tile('C',3)
        board.grid[7][8].letter = Tile('A',1)
        board.grid[7][9].letter = Tile('S',2)
        board.grid[7][10].letter = Tile('A',1)
        board.grid[7][7].active = False
        word = 'faca'
        location = (6,8)
        orientation = False
        self.assertEqual(board.calculate_word_value(word,location,orientation),16)
if __name__ == '__main__':
    unittest.main()