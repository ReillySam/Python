'''
                                        --- AI & Tic Tac Toe ---
    The aim of this project is to implement a revised version of Tic Tac Toe with the addition of a computer player
    to play against.
    To train the computer player, so it chooses the best possible move to make. Implementing MinMax algorithm with
    alpha beta pruning to achieve this.
'''

class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.winner = None

    def make_board(self):
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

        for i in range(3):
            for row in self.board[i*3: (i+1) *3]:
                print(i, ' _ ' + ' _ '.join(row) + ' _')

    def print_board_numbers(self):
        # 0 1 2
        board_numbers = [[str(i) for i in range(j*3, (j+1) * 3)] for j in range(3)]
        print(board_numbers)
        for row in board_numbers:
            print('| ' + ' | '.join(row) + ' |')


ttt = TicTacToe()
print(ttt.make_board())
ttt.print_board()
ttt.print_board_numbers()
