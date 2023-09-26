from game.board import *
from game.player import *
from game.tilebag import *
from game.cell import *

class ScrabbleGame:
    def __init__(self, players_count):
        self.players_count = players_count
        self.players = []
        self.board = Board()
        self.tilebag = BagTile()
        self.current_player = None
        self.game_over = False
        self.current_player= None
        for i in range(self.players_count):
            self.players.append(Player())

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            index=self.players.index(self.current_player)+1
            self.current_player=self.players[index]