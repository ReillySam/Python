'''
                                         --- TIC TAC TOE ---
    First goal is to implement a simple dynamic version of Tic Tac Toe.
    Secondly look how to implement an AI version to play against.
    Possibly using MinMax algorithm and/or alpha beta pruning. Implement with greater structure and design.
    
    Still needs some error handling but basically runs
'''

                                      # Basic but dynamic TicTacToe Game

import itertools

def win(current_game):
    # Horizontal
    for row in current_game:
        if all(item == row[0] and item != ' ' for item in row):
            print("Player {} WINS! (Horizontal)".format(row[0]))
            return True

    # Vertical  - Needs handling
    for col in range(len(current_game)):    # wouldn't work with enumerate function.
        check = []
        for row in current_game: check.append(row[col])
        if len(set(check)) == 1 and check[col] != ' ':
            print("Player {} WINS! (Vertical)".format(check[col]))
            return True

    # Diagonal (0,2) to (2,0)
    diag = []
    for col, row in enumerate(range(len(current_game))[::-1]):
        diag.append(current_game[col][row])
    if len(set(diag)) == 1 and diag[0] != ' ':
        print("Player {} WINS! (Diagonally /)".format(diag[0]))
        return True

    # (0,0) to (2,2) diagonal
    diag = []
    for item in range(len(current_game)):
        diag.append(current_game[item][item])
    if len(set(diag)) == 1 and diag[0] != ' ':
        print("Player {} WINS! (Diagonally \\)".format(diag[0]))
        return True


def game_board(game_map, player='', row=0, column=0, display=False):
    try:
        if game_map[row][column] != ' ':
            print("Position taken by {}. Choose another\n".format(game_map[row][column]))
            return game_map, False
        print("    " + "    ".join([str(i) for i in range(len(game))]))
        if not display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map

    except IndexError as e:
        print("Error: Remember to index between 0 and {}. ".format(len(game_map)), e)
        return game_map, False

    except Exception as e:
        print("Error: ",e)
        return game_map, False

play = True
players = itertools.cycle(('X', 'O'))  # itertool to cycle between the two items
while play:
    game_size = int(input("What size game would you like to play? "))
    print(":) let's play TIC TAC TOE!")
    game = [[' ' for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game_board(game, display=True)
    
    while not game_won:
        cur_player = next(players)   # itertool used here, next()
        print("\nPlayer {} you're turn!".format(cur_player))
        col_choice = int(input("- Pick a column: "))
        row_choice = int(input("- Pick a row: "))
        game_board(game, cur_player, row_choice, col_choice)
        
        if win(game):
            game_won = True
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            play_again = input("Play again? (y/n): ")
            if play_again.lower() == 'y':
                play = True
            elif play_again.lower() == 'n':
                print("Thanks for playing!!")
                play = False
            else: raise ValueError
