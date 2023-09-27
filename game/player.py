
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
            self.tiles[i]=new_tiles.pop(0)
        return old_tiles

    # def has_letters(self,word):
    