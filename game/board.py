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

    def validate_len_of_word_in_board(self, word, location, orientation):
        location_x = location[0]
        location_y = location[1]
        len_word = len(word)
        if orientation == 'H':
            if location_x + len_word > 15:
                return False
            else:
                return True
        else:
            if location_y + len_word > 15:
                return False
            else:
                return True
        
    def board_empty(self):
        if self.grid[7][7].letter == None:
            return True
        elif self.grid[7][7].letter != None:
            return False


    def validate_word_place_board(self, word, location, orientation):
        # If the board is empty and the word is valid
        if self.board_empty() and self.validate_len_of_word_in_board(word, location, orientation):
            for i in range (len(word)):
                if orientation == "H":
                    pos_x = location[0] + i
                    if pos_x==7:
                        return True
                    else:
                        return False
                else:
                    pos_y = location[1] + i
                    if pos_y==7:
                        return True
                    else:
                        return False
        # If the board is not empty 
        else:
            h_space = len(word) <= len(self.grid)-location[0]
            v_space = len(word) <= len(self.grid)-location[1]
            intersections = 0
            is_valid = 0
            if (orientation=='H' and h_space):
                for i in range(len(word)):
                    cell = self.grid[location[0]][location[1]+i].letter
                    if cell is not None:
                        intersections += 1
                        if cell.letter == word[i]:
                            is_valid += 1
            elif ((not orientation=='H') and v_space):
                for i in range(len(word)):
                    cell = self.grid[location[0]+i][location[1]].letter
                    if cell is not None:
                        intersections += 1
                        if cell.letter == word[i]:
                            is_valid += 1
            if is_valid != 0 and intersections == is_valid:
                return True
            else:
                return False