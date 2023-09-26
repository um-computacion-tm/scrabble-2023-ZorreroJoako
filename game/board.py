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
        else:
            return False
    
    # def validate_word_place_board_not_empty(self, word, location, orientation):
    #     x, y = location
    #     word_length = len(word)

    #     Verifica que la ubicación esté dentro de los límites del tablero
    #     if x < 0 or x >= 15 or y < 0 or y >= 15:
    #         return False

    #     Verifica que la palabra quepa en el tablero en la orientación especificada
    #     if (orientation == "H" and y + word_length > 15) or (orientation == "V" and x + word_length > 15):
    #         return False

    #     Verifica que no haya letras en las celdas ocupadas por la palabra
    #     for i in range(word_length):
    #         if orientation == "H":
    #             if self.grid[x][y + i] != ' ' and self.grid[x][y + i] != word[i]:
    #                 return False
    #         elif orientation == "V":
    #             if self.grid[x + i][y] != ' ' and self.grid[x + i][y] != word[i]:
    #                 return False

    #     return True