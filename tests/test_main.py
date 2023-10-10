import unittest
from unittest.mock import patch
from game.main import *

class TestMain(unittest.TestCase):
    def test_main(self):
        with patch('builtins.input', side_effect=[2]):
            main = Main()
            self.assertEqual(main.main(), 2)

    def test_main_fail(self):
        with patch('builtins.input', side_effect=[1, 5, 2]):
            main = Main()
            self.assertEqual(main.main(), 2)

    def test_main_fail2(self):
        with patch('builtins.input', side_effect=[1, 5, 2]):
            main = Main()
            self.assertNotEqual(main.main(), 1)
        
if __name__ == '__main__':
    unittest.main()