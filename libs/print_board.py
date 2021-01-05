# tty prints a board in the terminal
# written by Russell on 4/7/20
# modified on 5/6 to incorporate new board data structure

# takes a string board (list of char) as a parameter
# outputs a tic-tac-toe board representation to the terminal

def print_board(str_board):

    # input = [" ", "", "X", "X", " ", "O", "O", "X", " "]

    # ouptput =

    #  O | X |
    # -----------
    #  X |   | O
    # -----------
    #    |   | X

    horiz_line = "-----------"
    divider = " | "
    space = " "

    print("\n")
    print(space + str_board[6] + divider +
          str_board[7] + divider + str_board[8])
    print(horiz_line)
    print(space + str_board[3] + divider +
          str_board[4] + divider + str_board[5])
    print(horiz_line)
    print(space + str_board[0] + divider +
          str_board[1] + divider + str_board[2])
    print("\n")


# takes a string board or a game list as a parameter
def tty_print(board = False):

    this_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    start_board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    if not board:
        print_board(start_board)
    elif type(board[0]) == str:
        print_board(board)
    elif type(board[0]) == int:

        for move in range(len(board)):

            if move == 0 or move % 2 == 0:
                this_board[board[move]] = "X"
            elif move % 2 == 1:
                this_board[board[move]] = "O"

        print_board(this_board)


#stand alone test run
if __name__ == "__main__":

    from transpose import rotate90, rotate180, rotate270, reflect_diagonal_left, reflect_diagonal_right, reflect_horizontal, reflect_vertical

    example_board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    string_board = [" ", " ", "X", "X", " ", "O", "O", "X", " "]
    board = [2, 5, 3, 6, 7]
    print("\n")

    # start/empty board
    print("start/empty board")
    tty_print()

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
