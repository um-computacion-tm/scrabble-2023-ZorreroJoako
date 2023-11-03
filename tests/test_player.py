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

    def test_has_tiles(self):
        player = Player()
        player.tiles = [Tile('A',1),Tile('C',1),Tile('T',1),Tile('S',1),Tile('A',1),Tile('R',1),Tile('T',1)]
        result = player.has_tiles('casa')
        self.assertEqual(result, True)

    def test_has_tiles(self):
        player = Player()
        player.tiles = [Tile('A',1),Tile('C',1),Tile('T',1),Tile('S',1),Tile('B',1),Tile('R',1),Tile('T',1)]
        result = player.has_tiles('casa')
        self.assertEqual(result, False)
    
    # def test_player_take_tiles(self):
    #     player = Player()
    #     tileA = Tile ('A',1)
    #     tileC = Tile ('C',1)
    #     tileG = Tile ('G',2)
    #     tileS = Tile ('S',1)
    #     tileT = Tile ('T',1)
    #     player.tiles = [tileA,tileC,tileG,tileS,tileT,tileA,tileT]
    #     player.player_take_tiles('casa')
    #     self.assertEqual(player.tiles, [tileG,tileT,tileT])
        

if __name__ == '__main__':
    unittest.main()