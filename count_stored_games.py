
import pathlib

from ttt_base import TTT_base


file_dir = pathlib.Path(
    "C:\\Users\\Ipgnosis\\Documents\\Github\\Python\\tic_tac_toe\\game_files")

file_name = 'new_game_record.txt'

file_path = file_dir / file_name

# instantiate ML_base
game_history = TTT_base(file_path)

print("Count stored games for:", file_name)

game_count = game_history.num_records()

print("Games stored in {} = {}".format(file_name, game_count))