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
        self.add_tiles_to_players()

    def next_turn(self):
        if self.current_player == None:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player)
            if index == len(self.players) - 1:
                self.current_player = self.players[0]
            else:
                self.current_player = self.players[index + 1]

    def add_tiles_to_players(self):
        for player in self.players:
            player.add_tiles(self.tilebag.take_tiles(7))

    def remove_tiles(self, tiles_index):
        for i in tiles_index:
            self.current_player.tiles.pop(i)
            
        
    def change_tiles(self, old_tiles_index, new_tiles):
        old_tiles = []
        for i in old_tiles_index:
            old_tiles.append(self.current_player.tiles[i])
            self.current_player.tiles[i] = new_tiles.pop(0)
        self.current_player.add_tiles(old_tiles)
        return old_tiles

    def view_scores(self):
        scores = ''
        for player in self.players:
            scores += player.name + ': ' + str(player.score) + '\n'
        return scores
    
    def view_players_lectern(self):
        lectern = ''
        for player in self.players:
            lectern += player.view_lectern() + '\n'
        return lectern

    def view_board(self):
        return self.board.show_board()

    def put_word_in_table(self):
        self.board.put_word_in_table(self.current_player)

    def end_game(self):
        if self.tilebag.tiles == []:
            for player in self.players:
                if player.tiles == []:
                    self.game_over = True
                else:
                    self.game_over = False
                    break
        else:
            self.game_over = False
        return self.game_over