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
def tty_print(board):

    this_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    if not board:
        print_board(this_board)
    elif type(board[0]) == str:
        print_board(board)
    elif type(board[0]) == int:

        for move in range(len(board)):

            if move == 0 or move % 2 == 0:
                this_board[board[move]] = "X"
            elif move % 2 == 1:
                this_board[board[move]] = "O"

        print_board(this_board)
