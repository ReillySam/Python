'''
                                        --- AI & Tic Tac Toe ---
    The aim of this project is to implement a revised version of Tic Tac Toe with the addition of a computer player
    to play against.
    To train the computer player, so it chooses the best possible move to make. Implementing MinMax algorithm with
    alpha beta pruning to achieve this.
'''

import math


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.winner = None

    def make_board(self):
        return [' ' for _ in range(9)]

    def print_board(self):
        # for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
        #     print('| ' + ' | '.join(row) + ' |')

        for i in range(3):
            row = self.board[i*3: (i+1) *3]
            # print(row)
            print('| ' + ' | '.join(row) + ' |')

    def print_board_numbers(self):
        # 0 1 2
        board_numbers = [[str(i) for i in range(j*3, (j+1) * 3)] for j in range(3)]
        print(board_numbers)
        for row in board_numbers:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check row
        row_idx = math.floor(square / 3) # remainder == row
        row = self.board[row_idx * 3: (row_idx + 1) * 3]  # indexes all squares in row
        if all([sq == letter for sq in row]): # checks id all squares in row are same and equal to letter
            return True
        # check column
        col_idx = square % 3  # remainder == column
        column = [self.board[col_idx + (i * 3)] for i in range(3)]  # all column squares
        if all(sq == letter for sq in column):
            return True
        # check diagonal
        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]  # checks board index for each of the listed indexes
            if all(sq == letter for sq in diagonal_1):
                return True
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all(sq == letter for sq in diagonal_2):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def count_empty_sqaures(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, square in enumerate(self.board) if square == ' ']

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_numbers()

    letter = 'X'
    while game.empty_squares():


ttt = TicTacToe()
ttt.print_board()
ttt.print_board_numbers()
print(ttt.winner(0, 0))
