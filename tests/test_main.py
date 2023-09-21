import unittest
from game.main import *   
class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(Main().main(),None)
    
    def players_count(self):
        self.assertEqual(Main().players_count(),None)
    
    def no_valid_players_count(self):
        players_count ==5
        with self.assertRaises(ValueError):
            Main().players_count()
            
if __name__ == '__main__':
    unittest.main()
    
        