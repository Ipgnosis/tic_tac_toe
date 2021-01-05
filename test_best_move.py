# test best_move in make_play

import pathlib

from libs.make_play import best_move
from classes.ml_base import ML_base

# test game data

game1 = [0]
game2 = [0, 2]
game3 = [0, 2, 3] # X starts up the left file
game4 = [0, 2, 3, 6] # O blocks at 6
game5 = [0, 2, 3, 6, 4]  # X blocks at 4
game6 = [0, 2, 3, 6, 4, 8] # O blocks at 8
game7 = [0, 2, 3, 6, 4, 8, 1] # X makes a mistake at 1
game8 = [0, 2, 3, 6, 4, 8, 1, 7] # O wins along the top rank
game9a = [1, 5]
game9b = [1, 5, 7, 8]

win_game = [1, 5, 7, 8, 4]

# set up game_history

file_dir = pathlib.Path(
    "C:\\Users\\Ipgnosis\\Documents\\Github\\Python\\tic_tac_toe\\game_files")

file_name = 'master_game_file2_test.txt'

file_path = file_dir / file_name

print("Game file = ", file_path)

# instantiate ML_base
game_history = ML_base(file_path)

move = best_move(game9a, "X", game_history)

print("success: best_move =", move)

#########################################################################################
# write the game_history to file
# need to do this after we get the number of records stored
game_history.write_file()
