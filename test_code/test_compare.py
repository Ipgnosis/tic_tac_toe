# test compare.py and transpose.py
# uncomment test code in compare.py

import pathlib
from compare import duplicate_game
from ml_base import ML_base

file_dir = pathlib.Path(
    "C:\\Users\\Ipgnosis\\Documents\\Github\\Python\\tic_tac_toe\\game_files")

file_name = "test_game_record.txt"

file_path = file_dir / file_name

print("Game file = ", file_path)

# instantiate ML_base
test_obj = ML_base(file_path)

# print(test_obj.file_path)
# print(test_obj.file_name)

dict1 = {"result": "X", "game": [0, 6, 1, 4, 2]}
dict2 = {"result": "O", "game": [8, 7, 0, 1, 6, 4]}
dict3 = {"result": "D", "game": [1, 8, 7, 4, 0, 2, 5, 3, 6]}

# this will be inserted
game1 = {"result": "O", "game": [2, 4, 5, 8, 6, 7]}
# this will find a match against dict1 (rotate90) and will not be inserted
r90_game2 = {"result": "X", "game": [2, 0, 5, 4, 8]}
# this will be inserted
game3 = {"result": "X", "game": [0, 2, 8, 4, 6, 1, 3]}

test_obj.add_record(dict1)
test_obj.add_record(dict2)
test_obj.add_record(dict3)

game_list = [game1, r90_game2, game3]

# should be 3
print("Number of records:", test_obj.num_records())

for game in game_list:
    print("check loop:", game)
    if not duplicate_game(game["game"], test_obj):
        test_obj.add_record(game)

# should be 5
print("Number of records:", test_obj.num_records())

print("dict1:", test_obj.fetch_record(dict1))
print("dict2", test_obj.fetch_record(dict2))
print("dict3", test_obj.fetch_record(dict3))
print("game1", test_obj.fetch_record(game1))
print("r90_game2:", test_obj.fetch_record(r90_game2))
print("game3:", test_obj.fetch_record(game3))

print("Number of records:", test_obj.num_records())

# write the game_history to file
# need to do this after we get the number of records stored
test_obj.write_file()
