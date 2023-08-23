import random


class TakeTilesException(Exception):
    pass

class PutTilesException(Exception):
    pass

class TileNotFoundException(Exception):
    pass

ALLTILES = 100


class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class Wildcard(Tile):
    def __init__(self, letter, value):
        super().__init__(letter="", value=0)
    
    def wildcard_choose(self,letter_Wildcard):
        for i in BagTile().tiles:
            if i.letter==letter_Wildcard.upper() :
                self.letter=i.letter
                self.value=i.value
                break
        if self.letter=="":
            raise TileNotFoundException
            
        
        
class BagTile:
    def __init__(self):
        self.tiles = [Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1),
            Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1),
            Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1),
            Tile('L', 1), Tile('L', 1), Tile('L', 1), Tile('L', 1),
            Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1),
            Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1),
            Tile('R', 1), Tile('R', 1), Tile('R', 1), Tile('R', 1), Tile('R', 1),
            Tile('S', 1), Tile('S', 1), Tile('S', 1), Tile('S', 1), Tile('S', 1), Tile('S', 1),
            Tile('T', 1), Tile('T', 1), Tile('T', 1), Tile('T', 1),
            Tile('U', 1), Tile('U', 1), Tile('U', 1), Tile('U', 1), Tile('U', 1),
            Tile('D', 2), Tile('D', 2), Tile('D', 2), Tile('D', 2), Tile('D', 2),
            Tile('G', 2), Tile('G', 2), 
            Tile('B', 3), Tile('B', 3),
            Tile('C', 3), Tile('C', 3), Tile('C', 3), Tile('C', 3),
            Tile('M', 3), Tile('M', 3),
            Tile('P', 3), Tile('P', 3),
            Tile('F', 4),
            Tile('H', 4), Tile('H', 4),
            Tile('V', 4),
            Tile('Y', 4),
            Tile('CH', 5),
            Tile('Q', 5),
            Tile('J', 8),
            Tile('LL', 8),
            Tile('Ñ', 8),
            Tile('RR', 8),
            Tile('X', 8),
            Tile('Z', 10),Wildcard("",0 ), Wildcard("", 0)]
        random.shuffle(self.tiles)

    


    def take_tiles(self, cantidad):
        take_tiles = []

        try:
            if cantidad > len(self.tiles):
                raise TakeTilesException
            else:
                for _ in range(cantidad):
                    take_tiles.append(self.tiles.pop())
                return take_tiles
        
        except TakeTilesException:
            print('No hay más fichas para sacar de la bolsa')
            return take_tiles

    def put_tiles(self, tiles):
        try:
            if len(tiles) + len(self.tiles) <= ALLTILES:
                self.tiles.extend(tiles)
            else:
                raise PutTilesException 

        except PutTilesException:
            print('No se pueden poner más fichas en la bolsa')

    def tiles_leftover(self):
        return len(self.tiles)
