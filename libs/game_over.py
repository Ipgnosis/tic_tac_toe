# function to determine win or loss
# written by Russell on 4/8/20
# modified on 5/6 to incorporate new board data structure

# takes a board as a parameter and returns "X"/"O"/"D" ('X wins' / 'O wins' / 'Draw') or False for 'game in progress'
# board = list (2, 3, 4, 5, 6)

# e.g.:
# [6] 'X'| [7] ''  | [8] ''
# --------------------------
# [3] 'O'| [4] 'X' | [5] 'O'
# --------------------------
# [0] '' | [1] ''  | [2] 'X'


def win_loss(board):

    # check that a minimum of 5 moves have been made
    empty_cells = 9 - len(board)

    # not enough moves have been made
    if empty_cells >= 5:
        #print("win_loss: Too early - less than 5 moves made")
        return False

    x_moves = []
    o_moves = []
    moves_made = len(board)

    for move in range(len(board)):
        if move == 0 or move % 2 == 0:
            x_moves.append(board[move])
        else:
            o_moves.append(board[move])

    #print("X moves = " + str(x_moves))
    #print("O moves = " + str(o_moves))

    # all win combinations in a tuple of tuples
    win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (6, 3, 0),
                  (7, 4, 1), (8, 5, 2), (6, 4, 2), (8, 4, 0))

    for combo in win_combos:
        if combo[0] in x_moves and combo[1] in x_moves and combo[2] in x_moves:
            return ("X", moves_made)
        elif combo[0] in o_moves and combo[1] in o_moves and combo[2] in o_moves:
            return ("O", moves_made)

    # no win conditions have been found and all cells are full - this is a draw
    if empty_cells == 0:
        #print("win_loss: Draw - no win, no moves left")
        return ("D", moves_made)

    # no win conditions found and moves are left to be made
    #print("win_loss: No win condition, moves < 9")
    return False
