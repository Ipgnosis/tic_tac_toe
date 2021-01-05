# calls transpose.py to check if the board is a duplicate of one already saved
# returns true if game already recorded, false if not already recorded
# written by Russell on 5/5/20

import sys

from libs.transpose import rotate90, rotate180, rotate270, reflect_diagonal_left, reflect_diagonal_right, reflect_horizontal, reflect_vertical
from libs.print_board import tty_print

# test data subsituting for game record file
# game_records = [
#    {"result": "X", "game": [0, 6, 1, 4, 2]},  # rotate90
#    {"result": "O", "game": [8, 7, 0, 1, 6, 4]},  # rotate180
#    {"result": "X", "game": [0, 2, 8, 4, 6, 1, 3]},  # rotate270
#    {"result": "O", "game": [6, 1, 3, 0, 2, 4, 8, 7]},  # reflect diagonal left
#    {"result": "X", "game": [3, 0, 4, 1, 2, 8, 6, 7, 5]}, # relect diagonal right
#    {"result": "O", "game": [2, 4, 5, 8, 6, 7]},  # reflect horizontal
#    {"result": "D", "game": [1, 8, 7, 4, 0, 2, 5, 3, 6]}  # reflect vertical
#   ]
# end of test data

# check for duplicate games in the game_record file
def duplicate_game(board, game_class):

    # param1 is a game board submitted to the tests below
    # param2 is the object from the instance of class ML_base
    # compare the board to the transposed board
    # if one of these comparisons don't return true, then
    # there are no comparisons on file and returns false

    #print("this_board", board)

    # check rotate90
    #print("r90", rotate90(board))
    if game_class.find_match(rotate90(board)):
        return True
    
    # check rotate180
    #print("r180", rotate180(board))
    if game_class.find_match(rotate180(board)):
        return True

    # check rotate270
    #print("r270", rotate270(board))
    if game_class.find_match(rotate270(board)):
        return True

    # check reflect_diagonal_left
    #print("rdl", reflect_diagonal_left(board))
    if game_class.find_match(reflect_diagonal_left(board)):
        return True

    # check reflect_diagonal_right
    #print("rdr", reflect_diagonal_right(board))
    if game_class.find_match(reflect_diagonal_right(board)):
        return True

    # check reflect_horizontal
    #print("rh", reflect_horizontal(board))
    if game_class.find_match(reflect_horizontal(board)):
        return True

    # check reflect_vertical
    #print("rv", reflect_vertical(board))
    if game_class.find_match(reflect_vertical(board)):
        return True

    # no comparison found for this game
    #print("compare: returning False")
    return False

# compile a list of games transposed from the current game
# this is required because we don't know what orientation prior games were stored in
def get_transposed_games(this_board):

    # create a set of dicts containing the transposed game and the name of the 
    # function to reverse out the transposition later
    tx1 = rotate90(this_board)
    tx2 = rotate180(this_board)
    tx3 = rotate270(this_board)
    tx4 = reflect_diagonal_left(this_board)
    tx5 = reflect_diagonal_right(this_board)
    tx6 = reflect_horizontal(this_board)
    tx7 = reflect_vertical(this_board)

    orig_game = {"transpose": this_board, "reverse": "original"}
    r90 = {"transpose": tx1, "reverse": "rotate270"}
    r180 = {"transpose": tx2, "reverse": "rotate180"}
    r270 = {"transpose": tx3, "reverse": "rotate90"}
    rdl = {"transpose": tx4, "reverse": "reflect_diagonal_left"}
    rdr = {"transpose": tx5, "reverse": "reflect_diagonal_right"}
    rh = {"transpose": tx6, "reverse": "reflect_horizontal"}
    rv = {"transpose": tx7, "reverse": "reflect_vertical"}

    # compile a list of the dicts to be returned
    dup_games_list = [orig_game, r90, r180, r270, rdl, rdr, rh, rv]
    
    #print("get_transposed_games: dup_games_list -", dup_games_list)

    return dup_games_list

# convert the transposed games back to the original orientation
def reorient_games(transposed_games, winning_games):

    # transpose back
    # this_board = this_board
    # r90 = rotate270(r90)
    # r180 = rotate180(r180)
    # r270 = rotate270(r90)
    # rdl = reflect_diagonal_left(rdl)
    # rdr = reflect_diagonal_right(rdr)
    # rh = reflect_horizontal(rh)
    # rv = reflect_vertical(rv)

    # get the current length of the original game
    game_len = len(transposed_games[0]["transpose"])
    #print("game_len =", game_len)

    retransposed_games = []

    """ algorithm:
    1. traverse the list of transposed_games
    2. traverse the list of winning_games
    3. if the transposed game matches the winning game 
        (truncated to the length of the transposed game + 1)
    4. if the winning game is untransposed ("reverse": "original") append it unchanged 
        to the retransposed_games list
    5. otherwise, convert the string in the "reverse" value to its namesake function
    6. pass the truncated winning game to the reversing function to be reoriented
    7. append the reoriented game to the retransposed_games list
    8. return the retransposed_games list
    """
    for tx_game in transposed_games:
        for win_game in winning_games:
            #print("tx_game:", tx_game["transpose"], " win_game:", win_game["game"][: game_len])
            if tx_game["transpose"] == win_game["game"][: game_len]:
                if tx_game["reverse"] == "original":
                    retransposed_games.append(win_game["game"])
                else:    
                    win_game_retx = getattr(sys.modules[__name__], tx_game["reverse"])(win_game["game"])
                    retransposed_games.append(win_game_retx)

    return retransposed_games
