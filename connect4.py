import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board

board = create_board()
game_over = False
turn = 0

while not game_over:
    #Ask for input player 1
    if turn == 0:
        selection = int(input("Player 1, Make your selection(0-6): "))


    #Ask for input player 2
    else: 
        selection = int(input("Player 2, Make your selection(0-6): "))

    turn += 1
    turn = turn % 2