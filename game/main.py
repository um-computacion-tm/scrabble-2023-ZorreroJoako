from game.scrabblegame import *
from game.board import *

class ValueError(Exception):
    pass
class Main():
    def main(self):
        print("Bienvenido a Scrabble")
        while True:
            try:
                players_count = int(input("Ingrese el numero de jugadores (2-4)"))
                if players_count <=1   or players_count > 4:
                    raise ValueError
                break
            except:
                print ("Valor no valido")
        return players_count

    def menu(self, menu, scrabble_game):
        show_menu = f'Turno del jugador {scrabble_game.current_player.name}\n\n'
        if menu == 'menu':
            show_menu +=  '''    Menu
    1) Ver tablero
    2) Ver Atril
    3) Ver Acciones
    4) Ver Puntuaciones
    5) Salir
    Seleccion: '''
        elif menu == 'board':
            show_menu +=  '''    Tablero
    1) Ver tablero
    2) Salir
    Seleccion: '''
        elif menu == 'rack':
            show_menu += '''    Atril
    1) Ver atril
    2) Salir
    Seleccion: '''
        elif menu == 'actions':
            show_menu += '''    Acciones
    1) Colocar palabra
    2) Cambiar fichas
    3) Pasar turno
    4) Salir
    Seleccion: '''  
        elif menu == 'put_word':
            show_menu += '''    Colocar palabra
    1) Colocar palabra
    2) Salir
    Seleccion: '''
        elif menu == 'change_tiles':
            show_menu += '''    Cambiar fichas
    1) Cambiar fichas
    2) Salir
    Seleccion: '''
        elif menu == 'next_turn':
            show_menu += '''    Pasar turno
    1) Pasar turno
    2) Salir
    Seleccion: '''
        elif menu == 'scores':
            show_menu += '''    Puntuaciones
    1) Ver puntuaciones
    2) Salir
    Seleccion: '''
        elif menu == 'exit':
            show_menu += '''    Salir
    1) Salir
    2) Volver al menu
    Seleccion: '''
        return show_menu

    def menu_board(self, scrabble_game):
        while True:
            try:
                option = int(input(self.menu('board', scrabble_game)))
                if option == 1:
                    print(scrabble_game.view_board())
                elif option == 2:
                    break
                else:
                    raise ValueError
            except:
                print ("Valor no valido")
    
    def menu_rack(self, scrabble_game):
        while True:
            try:
                option = int(input(self.menu('rack', scrabble_game)))
                if option == 1:
                    print(scrabble_game.current_player.view_lectern())
                elif option == 2:
                    break
                else:
                    raise ValueError
            except:
                print ("Valor no valido")

    def menu_actions(self, scrabble_game):
        while True:
            try:
                option = int(input(self.menu('actions', scrabble_game)))
                if option == 1:
                    self.menu_put_word(scrabble_game)
                elif option == 2:
                    self.menu_change_tiles(scrabble_game)
                elif option == 3:
                    value = self.menu_next_turn(scrabble_game)
                    if value == 'cambio de turno':
                        break
                elif option == 4:
                    break
                else:
                    raise ValueError
            except:
                print ("Valor no valido")
        
    def menu_put_word(self, scrabble_game):
        while True:
            try:
                option = int(input(self.menu('put_word', scrabble_game)))
                if option == 1:
                    return self.put_word_wrapper(scrabble_game)
                elif option == 2:
                    break
                else:
                    raise ValueError
            except ValueError:
                print ("Valor no valido")

    def put_word_wrapper(self, scrabble_game):
        word= input("Ingrese una palabra: ")
        location_x= int(input ("Ingrese la coordenada x: "))
        location_y= int(input ("Ingrese la coordenada y: "))
        location = [location_x, location_y]
        orientation = input ("Ingrese la orientación (V/H): ").upper()
        if scrabble_game.board.validate_word_place_board(word, location, orientation):
            word = scrabble_game.board.words_with_accent(word)
            horizontal = True if orientation == 'H' else False
            points = self.scrabble_game.board.calculate_word_value(word,location,horizontal)
            if not scrabble_game.board.board_empty():
                word = scrabble_game.board.get_word_without_intersections(word, location, orientation=='H')
            if scrabble_game.current_player.has_tiles(word):
                tiles = scrabble_game.current_player.player_take_tiles(word)
                scrabble_game.current_player.points += points
                scrabble_game.board.put_word(tiles, location, orientation)
                scrabble_game.current_player.add_tiles(scrabble_game.tilebag.take_tiles(len(word)))
                scrabble_game.next_turn()
                return 'cambio de turno'
        elif scrabble_game.board.validate_word_place_board(word, location, orientation):
            print ("No tienes las fichas")
        elif scrabble_game.current_player.has_tiles(word):
            print ("La palabra es invalida")
        else:
            print ("La palabra o las fichas son invalidas")

    def menu_change_tiles(self, scrabble_game):
        while True:
            try:
                option = int(input(self.menu('change_tiles', scrabble_game)))
                if option == 1:
                    tiles_index = input("Ingrese los indices de las fichas que desea cambiar: ")
                    print(f'Tiles: {tiles_index}')
                    tiles_index = tiles_index.split(',')
                    tiles_index = [int(i) for i in tiles_index]
                    old_tiles = scrabble_game.current_player.tiles
                    new_tiles = scrabble_game.tilebag.take_tiles(len(tiles_index))
                    scrabble_game.change_tiles(tiles_index)
                    print(scrabble_game.current_player.view_lectern())
                    scrabble_game.next_turn()
                    return 'cambio de turno'
                elif option == 2:
                        break
                else:
                    raise ValueError
            except:
                print ("Valor no valido")

    def menu_next_turn(self, scrabble_game):
        while True:
            try:
                option = int(input(self.menu('next_turn', scrabble_game)))
                if option == 1:
                    scrabble_game.next_turn()
                    return 'cambio de turno'
                elif option == 2:
                    break
                else:
                    raise ValueError
            except:
                print ("Valor no valido")

    def menu_scores(self, scrabble_game):
        while True:
            try:
                option = int(input(self.menu('scores', scrabble_game)))
                if option == 1:
                    print(scrabble_game.view_scores())
                elif option == 2:
                    break
                else:
                    raise ValueError
            except:
                print ("Valor no valido")
    

    def menu_salir(self, scrabble_game):
        while True:
            try:
                option = int(input(self.menu('exit', scrabble_game)))
                if option == 1:
                    scrabble_game.game_over = True
                    print ("Gracias por jugar\n")
                    break
                elif option == 2:
                    break
                else:
                    raise ValueError
            except:
                print ("Valor no valido")
            
    def play_game(self, scrabble_game):
        while scrabble_game.game_over == False:
            try:
                option = int(input(self.menu('menu', scrabble_game)))
                if option == 1:
                    self.menu_board(scrabble_game)
                elif option == 2:
                    self.menu_rack(scrabble_game)
                elif option == 3:
                    self.menu_actions(scrabble_game)
                elif option == 4:
                    self.menu_scores(scrabble_game)
                elif option == 5:
                    self.menu_salir(scrabble_game)
                else:
                    raise ValueError
            except:
                print ("Valor no valido")

    def play(self):
        players_count = self.main()
        scrabble_game = ScrabbleGame(players_count=players_count)
        for i in range(players_count):
            name = input("Ingrese el nombre del jugador " + str(i+1) + ": ")
            scrabble_game.players[i].name = name
        scrabble_game.current_player = scrabble_game.players[0]
        self.play_game(scrabble_game)
    
if __name__ == "__main__":
    main = Main()
    main.play()