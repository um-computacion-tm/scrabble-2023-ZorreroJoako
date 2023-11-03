
class Player:
    def __init__(self,name="",score=0):
        self.name=name
        self.score=score
        self.tiles=[]

    def add_tiles(self,tiles):
        self.tiles.extend(tiles)
        
    def split_word(self,word):
        word = word.upper()
        replacements = {'CH': '1', 'LL': '2', 'RR': '3'}
        for key, value in replacements.items():
            word = word.replace(key, value)
        result_word = []
        i = 0
        while i < len(word):
            if word[i] in ('1', '2', '3'):
                for key, value in replacements.items():
                    if value == word[i]:
                        result_word.append(key)
                        break
                i += 1
            else:
                result_word.append(word[i])
                i += 1
        return result_word

    def search(self, word):
        word = self.split_word(word)
        tiles = self.tiles.copy()
        for letter in word:
            if letter in tiles:
                tiles.remove(letter)
            else:
                return False
        return True


    def view_lectern(self):
        lectern = '                     ATRIL\n\nLetras ->  |'
        for tile in self.tiles:
            lectern += ' ' + tile.letter + ' |'
        return lectern

    def has_tiles(self,word):
        copy_lectern = self.tiles.copy()
        is_valid = 0
        word = word.upper()
        for letter in word:
            for tile in copy_lectern:
                if tile.letter == letter:
                    is_valid += 1
                    copy_lectern.remove(tile)
                    break
        if is_valid == len(word):
            return True
        else :
            return False

    def player_take_tiles(self,word):
        word = self.split_word(word)
        tiles=[]
        for letter in word:
            for tile in self.tiles:
                if tile.letter==letter.upper():
                    tiles.append(tile)
                    self.tiles.remove(tile)
                    break
        return tiles

    def fill_tiles(self, tiles):
        self.tiles.extend(tiles)
        return self.tiles
        

                    