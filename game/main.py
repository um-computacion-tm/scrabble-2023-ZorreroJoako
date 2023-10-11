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

    def menu(self, menu):
        if menu == 'menu':
            return '''    Menu
    1) Ver tablero
    2) Ver Atril
    3) Ver Acciones
    4) Ver Puntuaciones
    Seleccion: '''
        elif menu == 'actions':
            return '''    Acciones
    1) Colocar palabra
    2) Pasar turno
    3) Cambiar fichas
    4) Salir
    Seleccion: '''  
        elif menu == 'scores':
            return '''    Puntuaciones
    1) Ver puntuaciones
    2) Salir
    Seleccion: '''
        elif menu == 'board':
            return '''    Tablero
    1) Ver tablero
    2) Salir
    Seleccion: '''
        elif menu == 'rack':
            return '''    Atril
    1) Ver atril
    2) Salir
    Seleccion: '''
        elif menu == 'change_tiles':
            return '''    Cambiar fichas
    1) Cambiar fichas
    2) Salir
    Seleccion: '''
        
        # scrabble_game = ScrabbleGame(players_count=players_count)
        # print ("Cantidad de jugadores: ", len(scrabble_game.players))
        # scrabble_game.next_turn()
        # print ("Turno de: ", scrabble_game.current_player)
        # word= input("Ingrese una palabra: ")
        # location_x= input ("Ingrese la coordenada x: ")
        # location_y= input ("Ingrese la coordenada y: ")
        # location = [location_x, location_y]
        # orientation = input ("Ingrese la orientación (V/H): ")