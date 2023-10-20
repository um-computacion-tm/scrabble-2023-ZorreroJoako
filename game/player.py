
class Player:
    def __init__(self,name="",score=0):
        self.name=name
        self.score=score
        self.tiles=[]

    def add_tiles(self,tiles):
        self.tiles.extend(tiles)

    
    def change_tiles(self,old_tiles_index,new_tiles):
        old_tiles=[]
        for i in old_tiles_index:
            old_tiles.append(self.tiles[i])
        for i in old_tiles_index:
            self.tiles.remove(self.tiles[i])
        self.add_tiles(new_tiles)
        return old_tiles
        

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

    
    
    