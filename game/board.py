from game.tilebag import Tile, Wildcard, BagTile
from game.cell import Cell
from game.player import Player
from pyrae import dle

DATA = BagTile().tiles

class Board:
    def __init__(self):
        self.grid = [[ Cell(1, '') for _ in range(15) ]for _ in range(15)]
        WORD_MULTIPLIERS = ((0, 0), (7, 0), (0, 7), (7, 7), (0, 14), (7, 14), (14, 0), (14, 7), (14, 14), (1, 1), (2, 2), (3, 3), (4, 4), (10, 10), (11, 11), (12, 12), (13, 13), (1, 13), (2, 12), (3, 11), (4, 10), (10, 4), (11, 3), (12, 2), (13, 1))
        LETTER_MULTIPLIERS = ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9),(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11))
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                self.assing_multipliers2(row, col, WORD_MULTIPLIERS, LETTER_MULTIPLIERS)

    def assing_multipliers2(self, row, col, WORD_MULTIPLIERS, LETTER_MULTIPLIERS):
        if (row, col) in LETTER_MULTIPLIERS:
                if (row, col) in ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)):
                    multiplier = 3
                else:
                    multiplier = 2
                self.grid[row][col] = Cell(multiplier, 'letter', True)
        elif (row, col) in WORD_MULTIPLIERS:
            if (row, col) in ((0, 0), (7, 0), (0, 7), (0, 14), (7, 14), (14, 0), (14, 7), (14, 14)):
                multiplier = 3
            else:
                multiplier = 2
            self.grid[row][col] = Cell(multiplier, 'word', True)
        else:
            self.grid[row][col] = Cell(1, '', False)
            
    def validate_words_with_rae(self, word):
        valid=dle.search_by_word(word)
        if valid.title[:1] == 'D':
            return False
        else:
            return True
    
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

    def validate_wrapper(self,word,location,orientation,is_valid,intersections):
        for i in range(len(word)):
            cell = self.grid[location[0]+(0 if orientation == 'H' else i)][location[1]+(i if orientation == 'H' else 0)].letter
            if cell:
                intersections += 1
                if cell.letter == word[i]:
                    is_valid += 1
        return is_valid, intersections
            
    def validate_not_empty(self, word, location, orientation):
        h_space = len(word) <= len(self.grid)-location[0]
        v_space = len(word) <= len(self.grid)-location[1]
        intersections = 0
        is_valid = 0
        if (orientation=='H' and h_space):
            is_valid, intersections = self.validate_wrapper(word,location,orientation,is_valid,intersections)
        elif ((not orientation=='H') and v_space):
            is_valid, intersections = self.validate_wrapper(word,location,orientation,is_valid,intersections)
        return is_valid != 0 and intersections == is_valid

    def validate_word_place_board(self, word, location, orientation):
        if self.validate_words_with_rae(word):
            word = word.upper()
            if self.board_empty() and self.validate_len_of_word_in_board(word, location, orientation):
                for i in range (len(word)):
                    if orientation == "H":
                        position_x = location[0] + i
                        return position_x==7
                    else:
                        position_y = location[1] + i
                        return position_y==7
            else:
                return self.validate_not_empty(word, location, orientation)

    def words_with_accent(self, word):
        word = word.lower()
        for letter in word:
            if letter == 'á':
                word = word.replace('á', 'a')
            elif letter == 'é':
                word = word.replace('é', 'e')
            elif letter == 'í':
                word = word.replace('í', 'i')
            elif letter == 'ó':
                word = word.replace('ó', 'o')
            elif letter == 'ú':
                word = word.replace('ú', 'u')
        return word.upper()

    def show_board(self):
        view = " \n 0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  \n"
        y = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]

        for i, row in enumerate(self.grid):
            view += f"{y[i]}   "
            for cell in row:
                if not cell.letter:
                    if cell.multiplier_type == 'letter' and cell.multiplier == 3:
                        view += f"3L|"
                    elif cell.multiplier_type == 'letter' and cell.multiplier == 2:
                        view += f"2L|"
                    elif cell.multiplier_type == 'word' and cell.multiplier == 3:
                        view += f"3W|"
                    elif cell.multiplier_type == 'word' and cell.multiplier == 2:
                        view += f"2W|"
                    else:
                        view += f"  |"
                else:
                    view += f"{cell.letter.letter} |"
            view += "\n"
        return view

    def put_word(self,word,position,orientation):
        orientation = orientation.upper()
        horizontal = True if orientation == 'H' else False
        j=0
        for i in range(len(word)):
            cell = self.grid[position[0]][position[1]+i+j] if horizontal else self.grid[position[0]+i+j][position[1]]
            while cell.letter:
                j+=1
                cell = self.grid[position[0]][position[1]+i+j] if horizontal else self.grid[position[0]+i+j][position[1]]
            cell.letter = word[i]
    
    def get_word_without_intersections(self,word,pos,horizontal):
        horizontal = True if horizontal == 'H' else False
        result = ''
        for i in range(len(word)):
            cell = self.grid[pos[0] + (i if not horizontal else 0)][pos[1] + (i if horizontal else 0)].letter
            if not cell:
                result += word[i]
        return result

    def calculate_word_value(self, word, pos, horizontal, first=True):
        word = Player().split_word(word)
        points = 0
        word_multiplier = 1
        i = 0
        for letter in word:
            cell, invert_cell, side_cell = self.get_cells(pos, i, horizontal)
            available = not cell.letter and first
            j = 1
            if invert_cell and invert_cell.letter and available:
                side_word, j = self.get_side_word(invert_cell, i, (horizontal,True), pos, letter)
                points += self.calculate_word_value(side_word, (pos[0] - j + 1, pos[1] + i) if horizontal else (pos[0] + i, pos[1] - j + 1), not horizontal, False)
            elif side_cell and side_cell.letter and available:
                side_word, j = self.get_side_word(side_cell, i, (horizontal,False), pos, letter)
                points += self.calculate_word_value(side_word, (pos[0], pos[1] + i) if horizontal else (pos[0] + i, pos[1]), not horizontal, False)
            letter_value = self.get_letter_value(letter)
            word_multiplier, points = self.update_multipliers(cell, letter_value, word_multiplier, points, first)
            i += 1
        points = points * word_multiplier
        return points

    def get_cells(self, pos, i, horizontal):
        cell = self.grid[pos[0]][pos[1] + i] if horizontal else self.grid[pos[0] + i][pos[1]]
        if pos[0] > 0 and pos[1] > 0:
            invert_cell = self.grid[pos[0] - 1][pos[1] + i] if horizontal else self.grid[pos[0] + i][pos[1] - 1]
        else:
            invert_cell = None
        try:
            side_cell = self.grid[pos[0] + 1][pos[1] + i] if horizontal else self.grid[pos[0] + i][pos[1] + 1]
        except:
            side_cell = None
        return cell, invert_cell, side_cell

    def get_side_word(self, cell, i, orientation, pos, letter):
        horizontal = orientation[0]
        inverted = orientation[1]
        k = -1 if inverted else 1
        side_word = letter
        j = 1
        while cell.letter:
            side_word += cell.letter.letter
            cell = self.grid[pos[0] + (1 + j)*k][pos[1] + i] if horizontal else self.grid[pos[0] + i][pos[1] + (1 + j)*k]
            j += 1
        if inverted:
            side_word = side_word[::-1]
        return side_word, j

    def get_letter_value(self, letter):
        for tile in DATA:
            if letter == tile.letter:
                return tile.value
        return 0

    def update_multipliers(self, cell, letter_value, word_multiplier, points, first):
        if (cell.multiplier_type.lower() == 'word') and cell.activate:
            word_multiplier *= cell.multiplier
        points += (letter_value * cell.multiplier) if cell.multiplier_type.lower() == 'letter' and cell.activate else letter_value
        if first:
            cell.activate = False
        return word_multiplier, points