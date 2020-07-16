
import sys
sys.path.append('tic_tac_toe')

from classes.calculate_probabilities import TTTProbs
from libs.print_board import tty_print

game1 = [0]
game2 = [0, 2]
game3 = [0, 2, 3]  # X starts up the left file
game4 = [0, 2, 3, 6]  # O blocks at 6
game5 = [0, 2, 3, 6, 4]  # X blocks at 4
game6 = [0, 2, 3, 6, 4, 8]  # O blocks at 8
game7 = [0, 2, 3, 6, 4, 8, 1]  # X makes a mistake at 1
game8 = [0, 2, 3, 6, 4, 8, 1, 7]  # O wins along the top rank
game9a = [1, 5]
game9b = [1, 5, 7, 8]

win_game = [1, 5, 7, 8, 4]

calc_probs = TTTProbs()

print("X leads off")
tty_print(game1)
probs1 = calc_probs.get_probs(game1)
print("X probs: p_win = {}, p_loss = {}, p_draw = {}".format(
    probs1[0], probs1[1], probs1[2]))
sum_probs = probs1[0] + probs1[1] + probs1[2]
if sum_probs != 1:
    print("ERROR: sum of probs != 1: {}".format(sum_probs))
print("\n")

print("O responds with a block")
tty_print(game2)
probs2 = calc_probs.get_probs(game2)
print("O probs: p_win = {}, p_loss = {}, p_draw = {}".format(
    probs2[0], probs2[1], probs2[2]))
sum_probs = probs2[0] + probs2[1] + probs2[2]
if sum_probs != 1:
    print("ERROR: sum of probs != 1: {}".format(sum_probs))
print("\n")

print("X starts up the left file")
tty_print(game3)
probs3 = calc_probs.get_probs(game3)
print("X probs: p_win = {}, p_loss = {}, p_draw = {}".format(
    probs3[0], probs3[1], probs3[2]))
sum_probs = probs3[0] + probs3[1] + probs3[2]
if sum_probs != 1:
    print("ERROR: sum of probs != 1: {}".format(sum_probs))
print("\n")

print("O blocks at 6")
tty_print(game4)
probs4 = calc_probs.get_probs(game4)
print("O probs: p_win = {}, p_loss = {}, p_draw = {}".format(
    probs4[0], probs4[1], probs4[2]))
sum_probs = probs4[0] + probs4[1] + probs4[2]
if sum_probs != 1:
    print("ERROR: sum of probs != 1: {}".format(sum_probs))
print("\n")

print("X blocks at 4")
tty_print(game5)
probs5 = calc_probs.get_probs(game5)
print("X probs: p_win = {}, p_loss = {}, p_draw = {}".format(
    probs5[0], probs5[1], probs5[2]))
sum_probs = probs5[0] + probs5[1] + probs5[2]
if sum_probs != 1:
    print("ERROR: sum of probs != 1: {}".format(sum_probs))
print("\n")

print("O blocks at 8")
tty_print(game6)
probs6 = calc_probs.get_probs(game6)
print("O probs: p_win = {}, p_loss = {}, p_draw = {}".format(
    probs6[0], probs6[1], probs6[2]))
sum_probs = probs6[0] + probs6[1] + probs6[2]
if sum_probs != 1:
    print("ERROR: sum of probs != 1: {}".format(sum_probs))
print("\n")

print("X makes a mistake at 1")
tty_print(game7)
probs7 = calc_probs.get_probs(game7)
print("X probs: p_win = {}, p_loss = {}, p_draw = {}".format(
    probs7[0], probs7[1], probs7[2]))
sum_probs = probs7[0] + probs7[1] + probs7[2]
if sum_probs != 1:
    print("ERROR: sum of probs != 1: {}".format(sum_probs))
print("\n")

print("O wins along the top rank")
tty_print(game8)
probs8 = calc_probs.get_probs(game8)
print("O probs: p_win = {}, p_loss = {}, p_draw = {}".format(
    probs8[0], probs8[1], probs8[2]))
sum_probs = probs8[0] + probs8[1] + probs8[2]
if sum_probs != 1:
    print("ERROR: sum of probs != 1: {}".format(sum_probs))
print("\n")
