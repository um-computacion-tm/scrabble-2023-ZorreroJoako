import unittest
from game.board import *
from game.tilebag import Tile
from game.cell  import Cell


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

    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True

    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == False
if __name__ == '__main__':
    unittest.main()