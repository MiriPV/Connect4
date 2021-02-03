import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(board, row, colom, piece):
    board[row][colom] = piece 

def is_valid_location(board, colom):
    #returns false, if top row (5) is full
    return board[5][colom] == 0

def get_next_open_row(board, colom):
    for r in range(ROW_COUNT):
        if board[r][colom] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    #Ask for input player 1
    if turn == 0:
        colom = int(input("Player 1, Make your selection(0-6): "))

        if is_valid_location(board, colom):
            row = get_next_open_row(board, colom)
            drop_piece(board, row, colom, 1)



    #Ask for input player 2
    else: 
        colom = int(input("Player 2, Make your selection(0-6): "))

        if is_valid_location(board, colom):
            row = get_next_open_row(board, colom)
            drop_piece(board, row, colom, 2)

    print_board(board)



    turn += 1
    turn = turn % 2