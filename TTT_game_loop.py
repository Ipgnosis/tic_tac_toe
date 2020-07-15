# initial game loop
# written by Russell on 4/9/20
# rewritten by Russell on 5/6/20 for new game data structure
# modified by Russell on 7/14 to tune the TTTProbs class

from libs.make_play import agent_x, agent_o
from classes.calculate_probabilities import TTTProbs
from libs.print_board import tty_print
import datetime
import sys
sys.path.append('tic_tac_toe')


from libs.move_utils import next_player
from libs.game_over import win_loss

print("Start the game with a blank board, with the cells numbered as follows")
example_board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
tty_print(example_board)

print("Each player makes a random play, with 'X' starting first...")

game_record = {"result": "D", "game": []}

while not win_loss(game_record["game"]):

    # decide who is next to play
    next_up = next_player(game_record["game"])

    if next_up == "X":
        x_choice = agent_x(game_record["game"])

        # record the move in the game
        game_record["game"].append(x_choice)

    elif next_up == "O":
        o_choice = agent_o(game_record["game"])

        # record the move in the game
        game_record["game"].append(o_choice)

    tty_print(game_record["game"])

result = win_loss(game_record["game"])

if result[0] == "X" or result[0] == "O":
    print("Player " + result[0] + " wins!")

    # flip the result value to the game winner (defaults to 'D')
    game_record["result"] = result[0]

else:
    print("No-one wins, it's a draw...")

print("Game record =", game_record)

print("Game result:", game_record["result"],
      "wins in", len(game_record["game"]), "moves")
print("Game moves = " + str(game_record["game"]))

print("Game over, insert coin")
