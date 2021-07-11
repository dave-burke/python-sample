from copy import *

board = {
    'tl': ' ', 'tm': ' ', 'tr': ' ',
    'ml': ' ', 'mm': ' ', 'mr': ' ',
    'bl': ' ', 'bm': ' ', 'br': ' ',
}

player = 'X'

def print_board(board):
    print(f"{board['tl']}|{board['tm']}|{board['tr']}")
    print('-+-+-')
    print(f"{board['ml']}|{board['mm']}|{board['mr']}")
    print('-+-+-')
    print(f"{board['bl']}|{board['bm']}|{board['br']}")

def run_turn(player, board):
    new_board = copy(board)
    while True:
        turn = input(f'Player {player}, where do you want to play? ')
        pos = board[turn]
        if pos == ' ':
            new_board[turn] = player
            break
        else:
            print('That space is not empty.')
    return ('X' if player == 'O' else 'O', new_board)

print_board(board)
for i in range(9):
    player, board = run_turn(player, board)
    print_board(board)

