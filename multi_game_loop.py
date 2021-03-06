# run a series of games, set by variable 'limit': see below
# written by Russell on 4/9/20
# modified on 5/4/20 to include matplotlib results
# modified on 5/5/20 to create the game_record dictionary
# modified on 3/10/21 to start to integrate TTTProbs into algorithm

from typing import TypedDict
from libs.plot_results import results_plot
from libs.print_board import tty_print
from libs.compare import duplicate_game
from libs.move_utils import next_player
from libs.make_play import agent_x, agent_o
from libs.game_over import win_loss
from classes.calculate_probabilities import TTTProbs
from classes.ttt_base import TTTBase
from typing_extensions import TypedDict
from typing import List, Tuple
from pathlib import Path
import time
import sys
import os

CURRENT_DIR = os.path.dirname(__file__)
sys.path.append(CURRENT_DIR)

# start the run timer
start_time = time.time()

# set the number of games to be played
limit = 10000

# set game file name
#file_name = 'rand_best_game_record.txt'
FILE_NAME = 'test_new_file4.txt'

# set the progress report frequency - only used for long, non-interactive runs
report_interval_percent = 0.1
report_frequency = limit * report_interval_percent
# this assignment can be commented out and is just a switch to disable reporting
#report_frequency = False

# mode_flip allows both agents to be trained in a balanced way when a game history is being created
# if mode flip is disabled, one agent will never get trained because it is being overwhelmed by the other
#mode_flip = True
mode_flip = False

# set the move selection modes for each agent
mode_x = "random"
mode_o = "random"
#mode_x = "human"
#mode_o = "human"
#mode_x = "best"
#mode_o = "best"

# matplotlib result set lists
agentX_x_axis = []
agentX_y_axis = []
agentO_x_axis = []
agentO_y_axis = []
draw_x_axis = []
draw_y_axis = []

# game tally variables
x_in_5 = x_in_7 = x_in_9 = o_in_6 = o_in_8 = d_in_9 = 0
X_wins = O_wins = Draws = 0
error_count = game_count = 0

# set up game_history from TTTBase class
##########################################################################

file_path = os.path.join(CURRENT_DIR, 'game_files', FILE_NAME)
DATA_FILE = Path(file_path)
print("main file_path type =", type(DATA_FILE))

print("Game file = ", DATA_FILE)

# instantiate TTTBase - game history
game_history = TTTBase(DATA_FILE)

# instantiate TTTProbs
#pct_tuple = game_history.outcome_pct()
# print("game_loop: game_history %'ages: P(X win) = {}, P(O win) = {}, P(Draw) = {}".format(
#    pct_tuple[0], pct_tuple[1], pct_tuple[2]))
#probs_obj = TTTProbs(pct_tuple[0], pct_tuple[1], pct_tuple[2])
probs_obj = TTTProbs()

new_games_stored = 0

print("Games currently in game history:", game_history.num_records())

if mode_flip:
    print("Playing in mode_flip mode")
else:
    print("Agent Cross is playing in {} mode.".format(mode_x))
    print("Agent Nought is playing in {} mode.".format(mode_o))

if not report_frequency:
    print("Report frequency disabled")

### start multi-game loop ###
for game_count in range(1, limit + 1):

    # declare the game record dictionary
    Game_Record = TypedDict(
        'Game_Record', {"result": str, "game": List[int], "probs": List[Tuple]})
    game_record = Game_Record(result="D", game=[], probs=[])

    # calculate game probabilities that exist prior to the upcoming play
    # as this is the first play of the first game, this will be the cumulative probabilities
    game_probs = probs_obj.get_probs(game_record["game"])

    # run a single game
    while not win_loss(game_record["game"]):

        # decide who is next to play
        next_up = next_player(game_record["game"])
        #print("game_loop: next_up =", next_up)

        # output the game state for a human player to see
        if mode_o == 'human' or mode_x == 'human':

            if len(game_record["game"]) > 0:
                tty_print(game_record["game"])
            else:
                tty_print()

            if len(game_record["game"]) == 0:
                # game probs are from the cumulative probabilities
                print("game_loop: current game probabilities: P(X win) = {}, P(O win) = {}, P(Draw) = {}".format(
                    game_probs[0], game_probs[1], game_probs[2]))
            else:  # a game is in progress
                # game probs are from the player that just moved
                print("game_loop: player {} probabilities: P(win) = {}, P(loss) = {}, P(Draw) = {}".format(
                    game_probs[0], game_probs[1], game_probs[2], game_probs[3]))

        # invoke the agent of the next player
        if next_up == "X":

            cell = agent_x(game_record["game"], game_history, mode_x)

            #print("agent_x - recommended move:", cell)

        else:

            cell = agent_o(game_record["game"], game_history, mode_o)

            #print("agent_o - recommended move:", cell)

        #print("Game {} state = {}".format(game_count, game_record["game"]))

        # record the move in the game
        game_record["game"].append(cell)

        # calculate game probabilities as a result of the last play
        game_probs = probs_obj.get_probs(game_record["game"])

        game_record["probs"].append(
            (game_probs[1], game_probs[2], game_probs[3]))

    # end of single game loop

    # reset the probabilty object
    probs_obj.reset_vector_states()

    # flip the modes to enable agent training to be balanced
    if mode_flip:
        if mode_x == "random":
            mode_x = "best"
            mode_o = "random"
        else:
            mode_x = "random"
            mode_o = "best"

    # tally up the result
    result = win_loss(game_record["game"])

    if result[0] == "X":
        if result[1] == 5:
            x_in_5 += 1
        elif result[1] == 7:
            x_in_7 += 1
        elif result[1] == 9:
            x_in_9 += 1
        X_wins += 1

    elif result[0] == "O":
        if result[1] == 6:
            o_in_6 += 1
        elif result[1] == 8:
            o_in_8 += 1
        O_wins += 1

    elif result[0] == "D":
        d_in_9 += 1
        Draws += 1

    else:
        error_count += 1

    # flip the result value to the game winner (defaults to 'D')
    game_record["result"] = result[0]

    # take a peek at the game record - comment this out?
    #print("game_record =", game_record)

    # output the result in non-automated games
    if mode_x == "human" or mode_o == "human":
        print("\n")
        tty_print(game_record["game"])
        if game_record["result"] == "D":
            print("This game results in a draw")
        elif game_record["result"] == "X":
            print("Player X wins!")
        elif game_record["result"] == "O":
            print("Player O wins!")

        print("Score so far: X has {} wins; O has {} wins; {} games drawn; {} games complete; {} games remaining.".format(
            X_wins, O_wins, Draws, game_count, limit - game_count))

    # check the game record to see if we have seen this game before in any orientation
    if not duplicate_game(game_record["game"], game_history):
        # if not, store the game record in the game_history
        stored = game_history.add_record(game_record)
        if stored:
            new_games_stored += 1

    # add the win data for the game to the result sets
    agentX_x_axis.append(game_count)
    agentX_y_axis.append(X_wins)

    agentO_x_axis.append(game_count)
    agentO_y_axis.append(O_wins)

    draw_x_axis.append(game_count)
    draw_y_axis.append(Draws)

    # output the progress counter
    if report_frequency:
        if game_count % report_frequency == 0:
            elapsed = time.time() - start_time
            game_duration = elapsed / game_count
            etc = round(game_duration * limit)
            time_left = round((limit - game_count) * game_duration)
            print("Game: {}...Estimated total completion time = {} seconds; time left = {} seconds.".format(
                game_count, etc, time_left))

### end of game loop ###

# report the results

total_x_wins = x_in_5 + x_in_7 + x_in_9
total_o_wins = o_in_6 + o_in_8

print("Game count = ", game_count)
print("Errors = ", error_count)

print("New games added to game history =", new_games_stored)
print("Games now in game history:", game_history.num_records())

# write the game_history to file
# need to do this after we get the number of records stored
game_history.write_file()

# delete the instantiated classes (take out the garbage)
del game_history
del probs_obj

# proceed with reporting results now game file is closed
print("X wins in 5 moves = {} or {}%".format(
    str(x_in_5), str(round(x_in_5 / game_count * 100, 1))))
print("X wins in 7 moves = {} or {}%".format(
    str(x_in_7), str(round(x_in_7 / game_count * 100, 1))))
print("X wins in 9 moves = {} or {}%".format(
    str(x_in_9), str(round(x_in_9 / game_count * 100, 1))))
print("Total X wins = {} or {}%\n".format(str(total_x_wins),
                                          str(round(total_x_wins / game_count * 100, 1))))

print("O wins in 6 moves = {} or {}%".format(
    str(o_in_6), str(round(o_in_6 / game_count * 100, 1))))
print("O wins in 8 moves = {} or {}%".format(
    str(o_in_8), str(round(o_in_8 / game_count * 100, 1))))
print("Total O wins = {} or {}%\n".format(str(total_o_wins),
                                          str(round(total_o_wins / game_count * 100, 1))))

print("Draws = {} or {}%\n".format(str(d_in_9),
                                   str(round(d_in_9 / game_count * 100, 1))))

# stop the run timer before we invoke matplotlib
end_time = time.time()
print("Game loop took: {} seconds".format(round(end_time - start_time, 2)))

# package up the result set and send to matplotlib, assuming game limit > 1 (no meaningful output)
if limit > 1:
    plot_title = "Results for {} games".format(str(limit))
    subtitle = "Player modes: Agent Cross {} mode; Agent Nought = {} mode.".format(
        agent_x, agent_o)
    result_set = [agentX_x_axis, agentX_y_axis, agentO_x_axis,
                  agentO_y_axis, draw_x_axis, draw_y_axis]

    results_plot(plot_title, mode_x, mode_o, result_set)
