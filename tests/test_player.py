import unittest
from game.player import *
from game.tilebag import *
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
    
    def test_split_word(self):
        player = Player()
        splited_word = player.split_word('CASA')
        self.assertEqual(splited_word, ['C','A','S','A'])

    def test_split_word_with_ll(self):
        player = Player()
        splited_word = player.split_word('llorar')
        self.assertEqual(splited_word, ['LL','O','R','A', 'R'])

    def test_split_word_with_ch(self):
        player = Player()
        splited_word = player.split_word('chocar')
        self.assertEqual(splited_word, ['CH','O','C','A','R'])

    def test_split_word_with_rr(self):
        player = Player()
        splited_word = player.split_word('hierro')
        self.assertEqual(splited_word, ['H', 'I', 'E','RR','O'])

    def test_search_word_invalid(self):
        player = Player()
        player.add_tiles(['A','B','C','D'])
        self.assertFalse(player.search('CASA'))
    
    def test_search_word_valid(self):
        player = Player()
        player.add_tiles(['A','B','C','S', 'A'])
        self.assertTrue(player.search('CASA'))
        
    def test_view_lectern(self):
        player = Player()
        player.tiles = [Tile('A',1),Tile('A',1),Tile('A',1),Tile('A',1),Tile('A',1),Tile('A',1),Tile('A',1)]
        self.assertEqual(player.view_lectern(), '''                     ATRIL

Letras ->  | A | A | A | A | A | A | A |''')

if __name__ == '__main__':
    unittest.main()