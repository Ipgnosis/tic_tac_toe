# test the game_over function

from print_board import tty_print
from game_over import win_loss

print("test_game_over: Too early")
#board = ["", "", "", "", "X", "", "O", "", ""]
board = [4, 6]
tty_print(board)
print(win_loss(board))
print("\n")

print("test_game_over: No winner yet - 5 moves made")
#board = ["X", "", "", "X", "X", "", "O", "", "O"]
board = [4, 6, 0, 8, 3]
tty_print(board)
print(win_loss(board))
print("\n")

print("test_game_over: No moves left, - no win - draw")
#         "X", "X", "0"
#         "O", "X", "X",
#board = ["X", "O", "O", "O", "X", "X", "X", "X", "0"]
board = [0, 1, 4, 3, 5, 8, 7, 2, 6]
tty_print(board)
print(win_loss(board))
print("\n")

print("test_game_over: X wins down the left vertical")
#board = ["X", "O", "", "X", "O", "", "X", "", ""]
board = [0, 1, 3, 4, 6]
tty_print(board)
print(win_loss(board))
print("\n")

print("test_game_over: X wins on the middle horizontal")
#board = ["O", "", "", "X", "X", "X", "O", "", ""]
board = [3, 0, 4, 6, 5]
tty_print(board)
print(win_loss(board))
print("\n")

print("test_game_over: O wins on the left to right diagonal")
#board = ["X", "X", "O", "X", "O", "", "O", "", "X"]
board = [0, 2, 1, 4, 3, 6, 8]
tty_print(board)
print(win_loss(board))
print("\n")

print("test_game_over: X wins on the last move on the right to left diagonal")
#board = ["X", "X", "O", "O", "X", "O", "O", "X", "X"]
board = [0, 2, 1, 3, 4, 5, 7, 6, 8]
tty_print(board)
print(win_loss(board))
print("\n")
