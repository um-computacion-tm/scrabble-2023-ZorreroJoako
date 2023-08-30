from game.board import *
from game.player import *
from game.tilebag import *

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTile()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())