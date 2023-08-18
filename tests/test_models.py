import unittest
from game.tiles import *

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

class TestTileBag(unittest.TestCase):
    def test_tilebag(self):
        tilebag = BagTile()
        self.assertEqual(tilebag.tiles_leftover(), ALLTILES)

    def test_take_tiles(self):
        tilebag = BagTile()
        tilebag.take_tiles(7)
        self.assertEqual(tilebag.tiles_leftover(), ALLTILES-7)
        
    def test_draw_too_much_tiles(self):
        tilebag= BagTile()
        self.assertEqual(tilebag.take_tiles(ALLTILES+1),[])
        
    def test_put_tiles(self):
        tilebag=BagTile()
        taken=tilebag.take_tiles(6)
        tilebag.put_tiles([taken[0], taken[5], taken[2]])
        self.assertEqual(tilebag.tiles_leftover(),ALLTILES-3)

    def test_put_too_much_tiles(self):
        tilebag=BagTile()
        tilebag.put_tiles([Tile('A',1)])
        self.assertEqual(tilebag.tiles_leftover(),ALLTILES)
        

if __name__ == '__main__':
    unittest.main()