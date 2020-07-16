# test the print_board module
# invoke the rotate and reflect functions from the transpose.py file


import sys
sys.path.append('tic_tac_toe')



from print_board import tty_print
from transpose import rotate90, rotate180, rotate270, reflect_diagonal_left, reflect_diagonal_right, reflect_horizontal, reflect_vertical

example_board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
string_board = [" ", " ", "X", "X", " ", "O", "O", "X", " "]
board = [2, 5, 3, 6, 7]

# example board
print("example board")
tty_print(example_board)

# string board
print("string board")
tty_print(string_board)

# integer board
print("integer board")
tty_print(board)

# rotate tests
print("rotate90")
board90 = rotate90(board)
tty_print(board)
tty_print(board90)

"""
print("rotate180")
board180 = rotate180(board)
tty_print(board)
tty_print(board180)

print("rotate270")
board270 = rotate270(board)
tty_print(board)
tty_print(board270)

# reflect tests
print("reflect_horizontal")
board_horiz = reflect_horizontal(board)
tty_print(board)
tty_print(board_horiz)

print("reflect_vertical")
board_vert = reflect_vertical(board)
tty_print(board)
tty_print(board_vert)

print("reflect_diagonal_right")
board_diag_right = reflect_diagonal_right(board)
tty_print(board)
tty_print(board_diag_right)

print("reflect_diagonal_left")
board_diag_left = reflect_diagonal_left(board)
tty_print(board)
tty_print(board_diag_left)
"""
