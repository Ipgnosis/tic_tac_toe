# class definition for TTTBase
# this is a class that stores the game history as a file of dict, in json format
# written by Russell on 5/9/20

import pathlib
import json

class TTTBase:

# data_records = [
#    {"result": "X", "game": [0, 6, 1, 4, 2]},
#    {"result": "O", "game": [8, 7, 0, 1, 6, 4]},
#    {"result": "X", "game": [0, 2, 8, 4, 6, 1, 3]},
#    {"result": "O", "game": [6, 1, 3, 0, 2, 4, 8, 7]},
#    {"result": "X", "game": [3, 0, 4, 1, 2, 8, 6, 7, 5]},
#    {"result": "D", "game": [1, 8, 7, 4, 0, 2, 5, 3, 6]}
# ]

    # initialize the class instance with the file name, populate file_path
    def __init__(self, file_path):
        self.file_path = file_path
        self.game_struct = {}

        # check if file exists, if True then open and load into game_struct
        #print("File exists?:", self.file_path.exists())
        if self.file_path.exists():
            self.read_file()
        else:
            print('__init__ : file missing')    

    # return the number of records in the game_struct
    def num_records(self):
        return len(self.game_struct)

    # return the percentages of records in the game_struct, by outcome (X, O, D)
    def outcome_pct(self):

        rec_count = 0
        x_wins = 0
        o_wins = 0
        draws = 0

        for game in self.game_struct:
            rec_count += 1
            if self.game_struct[game]["result"] == "X":
                x_wins += 1
            elif self.game_struct[game]["result"] == "O":
                o_wins += 1
            elif self.game_struct[game]["result"] == "D":
                draws += 1

        all_results = x_wins + o_wins + draws

        if all_results != rec_count:
            print("ML_base: outcome_pct ERROR - sum of results = {}, record count = {}".format(all_results, rec_count))

        pct_tuple = (x_wins / rec_count, o_wins / rec_count, draws / rec_count)

        return pct_tuple

    # calculate the index of a game
    def game_index(self, moves_list):
        #print('game_index:', moves_list)
        # calculate the power of n
        game_play_idx = len(moves_list) - 1
        rec_index = 0

        for i in range(len(moves_list)):
            # preserve a leading zero
            move_plus_1 = moves_list[i] + 1
            # calculate the game index = move * 10 ** n
            rec_index += move_plus_1 * 10 ** game_play_idx
            # decrement the power of n
            game_play_idx -= 1

        #print("game_index = ", rec_index)
        return(str(rec_index))

    # add a game record to the data_struct dictionary with an index
    def add_record(self, game_rec):
        # get an index for the game list
        game_idx = self.game_index(game_rec['game'])
        #print('add_record: game_idx type =', type(game_idx))
        # double check that this game_rec is not a duplicate
        if game_idx not in self.game_struct.keys():
            # insert the game_rec into the game_struct
            self.game_struct[game_idx] = game_rec
            return True
        else:
            # this game_rec is a duplicate
            return False

    # get a game record from the data_struct
    def fetch_record(self, game_rec):

        game_idx = self.game_index(game_rec['game'])

        if game_idx in self.game_struct.keys():
            #print("fetch record: idx =", game_idx)
            #print("fetch record: game =", game_rec)
            return self.game_struct[game_idx]
        else:
            return False

    # search data_struct for match of a game
    def find_match(self, game_rec):

        game_idx = 0

        #print("find_match", type(game_rec))

        if type(game_rec) == list:
            game_idx = self.game_index(game_rec)
        else:
            game_idx = self.game_index(game_rec['game'])

        #print("game_rec = ", game_rec, " game_idx =", game_idx)
        if game_idx in self.game_struct.keys():
            return True
        else:
            return False

    # find matches for a list of tuples of lower and upper bounded transposed games
    def get_games_list(self, bounds_list):

        candidate_games = []

        #print('get_games_list: bounds_list =', bounds_list)
        #print('get_games_list: type(bounds_list) =', type(bounds_list))
        
        # ensure we get the right number of moves after changing the game_index to str
        game_len = len(bounds_list[0][0])

        for game_bound in bounds_list:
            lower_idx = self.game_index(game_bound[0])
            #print('lower_idx:', lower_idx)
            #print('lower_idx: type', type(lower_idx))
            upper_idx = self.game_index(game_bound[1])
            #print('upper_index:', upper_idx)
            #print('upper_index: type', type(upper_idx))
            this_game_list = list(val for key, val in self.game_struct.items() if key >= lower_idx and key <= upper_idx and len(key) == game_len)
            #print('get_games_list: this_game_list -', this_game_list)
            candidate_games.extend(this_game_list)

        #print('get_games_list: candidate_games = ', candidate_games)

        # check to see if any games found: if not, return False
        if not candidate_games:
            return False
        else:
            return candidate_games
    
    # read file data into data_struct
    def read_file(self):
        with open(self.file_path, 'r') as f:
            self.game_struct = json.load(f)

    # write file from data in data_struct
    def write_file(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.game_struct, f)
        f.close()
