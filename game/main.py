from game.scrabblegame import *

class ValueError(Exception):
    pass
class Main():
    def main(self):
        print("Bienvenido a Scrable")
        while True:
            try:
                players_count = int(input("Ingrese el numero de jugadores (2-4)"))
                if players_count <=1   or players_count > 4:
                    raise ValueError
                break
            except ValueError:
                print ("Valor no valido")
        return players_count

    
    
        scrabble_game = ScrabbleGame(players_count=players_count)
        print ("Cantidad de jugadores: ", len(scrabble_game.players))
        scrabble_game.next_turn()
        print ("Turno de: ", scrabble_game.current_player)
        word= input("Ingrese una palabra: ")
        location_x= input ("Ingrese la coordenada x: ")
        location_y= input ("Ingrese la coordenada y: ")
        location = [location_x, location_y]
        orientation = input ("Ingrese la orientación (V/H): ")