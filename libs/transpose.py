# rotate and reflect functions
# written by Russell on 4/7/20
# rewritten by Russsell on 5/7/20 to accomodate game data structure change
# added numpy array iterations

#import numpy as np

# rotate functions:
# takes a board as a parameter and returns that board rotated
# board = list (2, 3, 4, 5, 6)
# ( '', '', 'X', 'O', 'X', 'O', 'X', '', '')
# cycling through a dictionary (rotation) to get the new order
# e.g.:
# [6] 'X'| [7] ''  | [8] ''
# --------------------------
# [3] 'O'| [4] 'X' | [5] 'O'
# --------------------------
# [0] '' | [1] ''  | [2] 'X'
# rotates 90 degrees right to:
# [6] '' | [7] '0' | [8] 'X'
# --------------------------
# [3] '' | [4] 'X' | [5] ''
# --------------------------
# [0] 'X'| [1] 'O' | [2] ''


def rotate90(this_board):

    # rotate 90
    rotation = {0: 6, 1: 3, 2: 0, 3: 7, 4: 4, 5: 1, 6: 8, 7: 5, 8: 2}

    #np_board = np.array(this_board)

    board90 = []

    for cell in range(len(this_board)):
    #for cell in np_board:    
        board90.append(rotation[this_board[cell]])
        #board90.append(rotation[np_board[cell]])

    return board90


def rotate180(this_board):

    # rotate 180
    rotation = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}

    #np_board = np.array(this_board)

    board180 = []

    for cell in range(len(this_board)):
    #for cell in np_board:
        board180.append(rotation[this_board[cell]])
        #board180.append(rotation[np_board[cell]])

    return board180


def rotate270(this_board):

    # rotate 270
    rotation = {0: 2, 1: 5, 2: 8, 3: 1, 4: 4, 5: 7, 6: 0, 7: 3, 8: 6}

    #np_board = np.array(this_board)

    board270 = []

    for cell in range(len(this_board)):
    #for cell in np_board:
        board270.append(rotation[this_board[cell]])
        #board270.append(rotation[np_board[cell]])

    return board270


# reflect functions:
# takes a board (list) as a parameter and returns that board (list) reflected
# board = list ('', '', 'X', 'O', 'X', 'O', 'X', '', '')
# cycling through a tuple (reflection) to get the new order
# e.g.:
# [6] 'X' | [7] ''  | [8] ''
# ---------------------------
# [3] 'O' | [4] 'X' | [5] 'O'
# ---------------------------
# [0] ''  | [1] ''  | [2] 'X'
# reflects horizontal to:
# [6] ''  | [7] ''  | [8] 'X'
# ---------------------------
# [3] 'O' | [4] 'X' | [5] '0'
# ---------------------------
# [0] 'X' | [1] ''  | [2] ''


def reflect_horizontal(this_board):

    # reflect horizontal
    reflection = {0: 6, 1: 7, 2: 8, 3: 3, 4: 4, 5: 5, 6: 0, 7: 1, 8: 2}

    #np_board = np.array(this_board)

    board_horizontal = []

    for cell in range(len(this_board)):
    #for cell in np_board:
        board_horizontal.append(reflection[this_board[cell]])
        #board_horizontal.append(reflection[np_board[cell]])

    return board_horizontal


def reflect_vertical(this_board):

    # reflect vertical
    reflection = {0: 2, 1: 1, 2: 0, 3: 5, 4: 4, 5: 3, 6: 8, 7: 7, 8: 6}

    #np_board = np.array(this_board)

    board_vertical = []

    for cell in range(len(this_board)):
    #for cell in np_board:
        board_vertical.append(reflection[this_board[cell]])
        #board_vertical.append(reflection[np_board[cell]])

    return board_vertical


def reflect_diagonal_right(this_board):

    # reflect diagonal right down to left
    reflection = {0: 8, 1: 5, 2: 2, 3: 7, 4: 4, 5: 1, 6: 6, 7: 3, 8: 0}

    #np_board = np.array(this_board)

    board_diagonal_right = []

    for cell in range(len(this_board)):
    #for cell in np_board:
        board_diagonal_right.append(reflection[this_board[cell]])
        #board_diagonal_right.append(reflection[np_board[cell]])

    return board_diagonal_right


def reflect_diagonal_left(this_board):

    # reflect diagonal left down to right
    reflection = {0: 0, 1: 3, 2: 6, 3: 1, 4: 4, 5: 7, 6: 2, 7: 5, 8: 8}

    #np_board = np.array(this_board)

    board_diagonal_left = []

    for cell in range(len(this_board)):
    #for cell in np_board:
        board_diagonal_left.append(reflection[this_board[cell]])
        #board_diagonal_left.append(reflection[np_board[cell]])

    return board_diagonal_left
