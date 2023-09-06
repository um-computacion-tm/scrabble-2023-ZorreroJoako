import unittest
from game.player import *

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player('Elio', 2)
        self.assertEqual(player_1.name, 'Elio')
        self.assertEqual(player_1.score, 2)
        self.assertEqual(len(player_1.tiles),0)
    
    def test_add_tiles(self):
        player_1 = Player()
        player_1.add_tiles(['A','B','C','D'])
        self.assertEqual(len(player_1.tiles),4)
        self.assertEqual(player_1.tiles,['A','B','C','D'])
    
    def test_change_tiles(self):
        player=Player()
        player.add_tiles(['A','B','C','D'])
        old_tiles_index=[0,1,2]
        new_tiles=['E','F','G']
        old_tiles=player.change_tiles(old_tiles_index,new_tiles)
        self.assertEqual(old_tiles,['A','B','C'])
        self.assertEqual(player.tiles,['E','F','G','D'])

if __name__ == '__main__':
    unittest.main()