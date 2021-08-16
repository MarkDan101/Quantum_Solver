from itertools import product
import numpy as np

class QuantAnnealingSudoku:
  def __init__ (self, grid_9x9=True):
    self.grid_9x9 = grid_9x9


  def check_sudoku(self, grid):
    digits = set(range(1,10))
    threes = [[0,1,2],[3,4,5],[6,7,8]]
    grid_format = 9

    if(self.grid_9x9== False):
      digits = set(range(1,4))
      threes = [[0,1],[2,3]]
      grid_format= 4

    error_count =0
    if len(grid) != grid_format or not all(len(row) == grid_format for row in grid):
      error_count += 1

    if not all(set(row) == digits for row in grid):
      error_count +=1

    columns = [[row[c] for row in grid ] for c in range(grid_format)]

    if not all (set(col) == digits for col in columns):
      error_count +=1

    for row_block , col_block in product(threes , threes):
      block = [grid[r][c] for r,c in product(row_block, col_block)]
      if set(block) != digits:
        error_count +=1

    return error_count;

  def encode_board_to_binary(self, board):
    binary_board = np.zeros((9,9,9)).tolist()
    if(self.grid_9x9) is False :
      binary_board = np.zeros((4,4,4)).tolist()

    for row_index, row in enumerate (board):
      for col_index , cell in enumerate(row):
        if cell > 0 :
          binary_board[cell-1][row_index][col_index] = 1

    return binary_board








  def decode_board_to_binary(self, binary_board):
    board=np.zeros((9,9))
    if self.grid_9x9 is False:
      board = np.zeros((4,4))

    for k, color in enumerate(binary_board):
      for i, row in enumerate(color):
        for j, cell_value in enumerate(row):
            if cell_value>0:
                board[i][j]+=int(k+1)
            else:
                board[i][j]+=int(0)

    return board





  def print_board(self , board):
    if isinstance(board,str):
      raise 'board as string not accepted'

    rows = 'ABCDEFGHI'
    cols = '123456789'
    boxes = [[("{}{}".format(r,c)) for c in cols ]
             for r in rows]

    if self.grid_9x9 is False:
      rows = 'abcd'
      cols = '1234'
      boxes = [[("{}{}".format(r,c)) for c in cols]
               for r in rows]

      for row, _boxes in enumerate(boxes):
        if row and row%2 ==0 :
          print('-'*6+"|"+'-'*6)

        for col , box in enumerate (_boxes):
          if col and col%2 ==0:
            print('|', end='')

          print(' {} '.format((int(board[row][col]) or '-')), end='')

        print()
      print()

    else:
        for row, _boxes in enumerate(boxes):
            if row and row % 3 == 0:
                    print('-'*9+"|"+'-'*9+"|"+'-'*9)
            for col, box in enumerate(_boxes):
                    if col and col % 3 == 0:
                        print('|', end='')
                    print(' {} '.format((int(board[row][col]) or '-')), end='')
            print()
        print() 
