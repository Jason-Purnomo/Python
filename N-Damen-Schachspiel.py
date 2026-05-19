import random

#2. Schritt
def print_board(board):
  for row in board:
    for value in row:
      print('Q' if value == 1 else '.', end='')
      print()

#3. Schritt
def is_safe(board, row, col):
  # Überprüfen der Spalte
  for i in range(row):
    if board[i][col] == 1:
      return False
  
  # Überprüfen der oberen linken Diagonale
  for i,j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
    if board[i][j] == 1:
      return False

  # Überprüfen der oberen rechten Diagonale
  for i,j in zip(range(row-1, -1, -1), range(col+1, N, 1)):
    if board[i][j] == 1:
      return False

  return True

#4. Schritt
def solve(data, row = 0, rand = False):
  # Endkriterium
  if row == len(data):
    return True

  # Zufallsreihenfolge der Spalten generieren
  cols = list(range(len(data)))
  if rand:
    random.shuffle(cols)

  # Damen in Spalte setzen
  #for col in range(len(data)):
  for col in cols:
    if is_safe(data, row, col):
      # Dame setzen
      data[row][col] = 1

      # Rekursiver Aufruf
      if solve(data, row+1):
        return True

      # Dame falsch platziert --> zurücknehmen 
      data[row][col] = 0

      # Es konnte keine Dame platziert werden
      return False

#1. Schritt
N = 8
board = [[0 for _ in range(N)] for _ in range(N)]
"""
Inner List: [0 for _ in range(N)] creates one row--> [0, 0, 0, 0, 0, 0, 0, 0]
Outer List: [[0 for _ in range(N)] for _ in range(N)] repeats that row N times
           --> [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
"""
print_board(board)

#5. Schritt
solve(board, rand=True)
print()     #Trenn-zeile hinzufügen
print_board(board)
