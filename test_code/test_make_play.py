# test the make_play functions

import pathlib
from print_board import tty_print
from game_over import win_loss
from make_play import agent_x, agent_o, next_player
from ml_base import ML_base

print("test_make_play")

file_dir = pathlib.Path(
    "C:\\Users\\Ipgnosis\\Documents\\Github\\Python\\tic_tac_toe\\game_files")

file_name = 'master_game_record.txt'

file_path = file_dir / file_name

print("Game file = ", file_name)

# instantiate ML_base
game_history = ML_base(file_path)

# declare the game record dictionary

next_up = "O"
game_record = [0, 2, 3]

if next_up == "X":
    cell = agent_x(game_record)
else:
    cell = agent_o(game_record, game_history)

print("test_make_play: best move = ", cell)