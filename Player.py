'''
                                        --- Tic Tac Toe Players ---
    Players for Tic Tac Toe game project.
    Both human and computer players developed.
'''

import random
import math

class Player():
    def __init__(self, letter):
        self.letter = letter

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        val = None
        valid_square = False
        while not valid_square:
            square = input(self.letter + "it's your turn. Input move 0-9: ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square, try again.")
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves() == 9):  # empty game all spaces available
            square = random.choice(game.available_moves())
        else:
            square = self.mini_max(game, self.letter)['position']
        return square

    def mini_max(self, game_state, player):
        # set which player is minimizing/maximizing
        max_player = self.letter # i.e yourself, you want best outcome
        other_player = 'O' if player == 'X' else 'X'

        # first check if previous move is winner
        if game_state.current_winner == other_player:
            # number of squares remaining after win, * by +1 for yourself or -1 for opponent (valuable or not)
            return {'position': None, 'score': 1 * (game_state.count_empty_sqaures() + 1) if other_player == max_player
                    else -1 * (game_state.count_empty_sqaures() + 1)}
        elif not game_state.count_empty_sqaures():
            # draw all squares filled with no winner
            return {'position': None, 'score': 0}

        if player == max_player:
            best_score = {'position': None, 'score': -math.inf}  # maximizing score
        else:
            best_score = {'position': None, 'score': math.inf}  # minimizing score
        for moves in game_state.available_moves():
            game_state.make_move(moves, player)
            score_simulation = self.mini_max(game_state, other_player)  # recursively checks all scores and gets best
                                                                        # value depending if its minimizing or maximizing
            # undo simulation and set next move to optimal move found
            game_state.board[moves] = ' '
            game_state.current_winner = None
            score_simulation['position'] = moves

            if player == max_player:
                if score_simulation['score'] > best_score['score']:
                    best_score = score_simulation
            else:
                if score_simulation['score'] < best_score['score']:
                    best_score = score_simulation
        return best_score
