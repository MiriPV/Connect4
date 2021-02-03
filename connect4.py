import numpy as np
import pygame
import sys
import math

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

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

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE)) 
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init() 

SQUARESIZE = 75

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myFont = pygame.font.SysFont("monospace", 50)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK,(0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN:   
            # #Ask for input player 1
            if turn == 0:
                posx = event.pos[0]
                colom = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, colom):
                    row = get_next_open_row(board, colom)
                    drop_piece(board, row, colom, 1)

                if winning_move(board, 1):
                    pygame.draw.rect(screen, BLACK,(0, 0, width, SQUARESIZE))
                    pygame.display.update()
                    label = myFont.render("Player 1 wins!!", 1, RED)
                    screen.blit(label, (40, 10))
                    game_over = True



            #Ask for input player 2
            else: 
                posx = event.pos[0]
                colom = int(math.floor(posx/SQUARESIZE))
                

                if is_valid_location(board, colom):
                    row = get_next_open_row(board, colom)
                    drop_piece(board, row, colom, 2)

                if winning_move(board, 2):
                    pygame.draw.rect(screen, BLACK,(0, 0, width, SQUARESIZE))
                    pygame.display.update()
                    label = myFont.render("Player 2 wins!!", 1, YELLOW)
                    screen.blit(label, (40,10))
                    game_over = True

            print_board(board)
            draw_board(board)



            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(7000)