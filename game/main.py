from game.scrabblegame import *

class ValueError(Exception):
    pass
class Main():
    def main(self):
        print("Welcome to Scrabble")
        while True:
            try:
                players_count = int(input("Enter the number of players (2-4)"))
                if players_count <=1   or players_count > 4:
                    raise ValueError
                break
            except ValueError:
                print ("Valor no valido")
        pass
        scrabble_game = ScrabbleGame(players_count=players_count)
        print ("Cantidad de jugadores: ", len(scrabble_game.players))
        scrabble_game.next_turn()
        print ("Turno de: ", scrabble_game.current_player)
        word= input("Enter a Word: ")
        location_x= input ("Enter x coordinate: ")
        location_y= input ("Enter y coordinate: ")
        location = [location_x, location_y]
        orientation = input ("Enter orientation (V/H): ")