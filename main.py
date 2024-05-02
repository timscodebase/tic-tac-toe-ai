import sys
import pygame
import numpy as np

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (180, 180, 180)
GRAY = GREY
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Proportions & Sizes
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = SCREEN_WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tic Tac Toe Ai')
screen.fill(BLACK)

board = np.zeros((BOARD_ROWS, BOARD_COLS))

def draw_lines(color=WHITE) -> None:
  for i in range(1, BOARD_ROWS):
    pygame.draw.line(screen, color, (0, SQUARE_SIZE * i), (SCREEN_WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
    pygame.draw.line(screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, SCREEN_HEIGHT), LINE_WIDTH)

def draw_figures(color=WHITE) -> None:
  for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
      if board[row][col] == 1:
        pygame.draw.circle(screen, color, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
      elif board[row][col] == 2:
        pygame.draw.line(screen, color, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), (col * SQUARE_SIZE + SQUARE_SIZE * 3 // 4, row * SQUARE_SIZE + SQUARE_SIZE * 3 // 4), CROSS_WIDTH)
        pygame.draw.line(screen, color, (col * SQUARE_SIZE + SQUARE_SIZE * 3 // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE * 3 // 4), CROSS_WIDTH)

def mark_square(row, col, player) -> None:
  board[row][col] = player

def available_square(row, col) -> bool:
  return board[row][col] == 0


def is_board_full(check_board=board) -> bool:
  for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
      if check_board[row][col] == 0:
        return False
      
def check_win(player, check_board=board) -> bool:
  # Horizontal win
  for col in range(BOARD_COLS):
    if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player:
      return True

  # Vertical win
  for row in range(BOARD_ROWS):
    if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player:
      return True

  # Diagonal win
  if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
    return True
  if check_board[0][2] == player and check_board[1][1] == player and check_board[2][0] == player:
    return True
  
  return False

def minimax(minimax_board=board, depth, is_maximizing) -> float:
  if check_win(2, minimax_board):
    return float('inf')
  elif check_win(1, minimax_board):
    return float('-inf')
  elif is_board_full(minimax_board):
    return 0
  
  if is_maximizing:
    best_score = -1000
    for row in range(BOARD_ROWS):
      for col in range(BOARD_COLS):
        if minimax_board[row][col] == 0:
          minimax_board[row][col] = 2
          score = minimax(minimax_board, depth + 1, False)
          minimax_board[row][col] = 0
          best_score = max(score, best_score)

    return best_score
  else:
    best_score = 1000
    for row in range(BOARD_ROWS):
      for col in range(BOARD_COLS):
        if minimax_board[row][col] == 0:
          minimax_board[row][col] = 1
          score = minimax(minimax_board, depth + 1, True)
          minimax_board[row][col] = 0
          best_score = min(score, best_score)

    return best_score