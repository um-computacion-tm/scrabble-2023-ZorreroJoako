from game.tilebag import Tile
from game.tilebag import Wildcard
from game.cell import Cell
class Board:
    def __init__(self):
        self.grid = [[ Cell(1, '') for _ in range(15) ]
        for _ in range(15)]
    
    def calculate_word_value(self, word):
        value = 0
        for cell in word:
            value += cell.calculate_value()
        for cell in word:
            if cell.multiplier_type == 'word':
                value *= cell.multiplier
                cell.multiplier = 1
        return value

    def validate_len_word(self, word, location_x, location_y,orientation):
        self.location_x= location_x
        self.location_y= location_y
        len_word = len(word)
        

            
