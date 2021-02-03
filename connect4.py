import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board

board = create_board()
game_over = False
turn = 0

while not game_over:
    #ask for player 1 input
    if turn == 0:
        selection = input("Player 1 Make your selection (0-6)")

    #ask for player 2 input