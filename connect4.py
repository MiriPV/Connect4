import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, colom, piece):
    board[row][colom] = piece 

def is_valid_location(board, colom):
    #returns false, if top row is full
    return board[ROW_COUNT - 1][colom] == 0

def get_next_open_row(board, colom):
    for r in range(ROW_COUNT):
        if board[r][colom] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    #Check horizontal locations for win. The last three colums don't have to be checked,
    #because there can no longer be 4 in a row if the columns before that were empty.
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    #Check vertical locations for win.
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    
    #Check diagonals positively sloped for win.
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    #Check diagonals negatively sloped for win.
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


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

            if winning_move(board, 1):
                print("PLAYER 1 WINS!")



    #Ask for input player 2
    else: 
        colom = int(input("Player 2, Make your selection(0-6): "))

        if is_valid_location(board, colom):
            row = get_next_open_row(board, colom)
            drop_piece(board, row, colom, 2)

            if winning_move(board, 2):
                print("PLAYER 2 WINS!")

    print_board(board)



    turn += 1
    turn = turn % 2