# test the Board_cell object

from cell_nodes import Board_cell
from game_status import Game_state
from rank_file_nodes import Win_triplet

# instantiate cell nodes
cell_zero = Board_cell(0, "zero")
cell_one = Board_cell(1, "one")
cell_two = Board_cell(2, "two")
cell_three = Board_cell(3, "three")
cell_four = Board_cell(4, "four")
cell_five = Board_cell(5, "five")
cell_six = Board_cell(6, "six")
cell_seven = Board_cell(7, "seven")
cell_eight = Board_cell(8, "eight")

# input = ["X", "O", "X", "O", " ", "X", "O", " ", " "]
# moves_list = [2, 6, 5, 3, 0, 1]

#  O |   |
# -----------
#  O |   | X
# -----------
#  X | O | X

#instantiate game_state
node_list = [cell_zero, cell_one, cell_two, cell_three, cell_four, cell_five, cell_six, cell_seven, cell_eight]
game_state = Game_state(node_list)

print(cell_two.node_name)
cell_two.move = "X"
print(cell_two.position)
print(cell_two.move)
print(cell_two.p_x_wins())
print(cell_two.p_o_wins())
print(cell_two.p_draw())
print("\n")

print("num moves: ", game_state.num_moves())
print("moves list: ", game_state.moves_list())
print("next up:", game_state.next_up())
print("proportion of game remaining: ", game_state.game_prop_remaining())
print("\n")

print(cell_six.node_name)
cell_six.move = "O"
print(cell_six.position)
print(cell_six.move)
print(cell_six.p_x_wins())
print(cell_six.p_o_wins())
print(cell_six.p_draw())
print("\n")

print("num moves: ", game_state.num_moves())
print("moves list: ", game_state.moves_list())
print("next up:", game_state.next_up())
print("proportion of game remaining: ", game_state.game_prop_remaining())
print("\n")

print(cell_five.node_name)
cell_five.move = "X"
print(cell_five.position)
print(cell_five.move)
print(cell_five.p_x_wins())
print(cell_five.p_o_wins())
print(cell_five.p_draw())
print("\n")

print("num moves: ", game_state.num_moves())
print("moves list: ", game_state.moves_list())
print("next up:", game_state.next_up())
print("proportion of game remaining: ", game_state.game_prop_remaining())
print("\n")

print(cell_three.node_name)
cell_three.move = "O"
print(cell_three.position)
print(cell_three.move)
print(cell_three.p_x_wins())
print(cell_three.p_o_wins())
print(cell_three.p_draw())
print("\n")

print("num moves: ", game_state.num_moves())
print("moves list: ", game_state.moves_list())
print("next up:", game_state.next_up())
print("proportion of game remaining: ", game_state.game_prop_remaining())
print("\n")

print(cell_zero.node_name)
cell_zero.move = "X"
print(cell_zero.position)
print(cell_zero.move)
print(cell_zero.p_x_wins())
print(cell_zero.p_o_wins())
print(cell_zero.p_draw())
print("\n")

print("num moves: ", game_state.num_moves())
print("moves list: ", game_state.moves_list())
print("next up:", game_state.next_up())
print("proportion of game remaining: ", game_state.game_prop_remaining())
print("\n")

print(cell_one.node_name)
cell_one.move = "O"
print(cell_one.position)
print(cell_one.move)
print(cell_one.p_x_wins())
print(cell_one.p_o_wins())
print(cell_one.p_draw())
print("\n")

print("num moves: ", game_state.num_moves())
print("moves list: ", game_state.moves_list())
print("next up:", game_state.next_up())
print("proportion of game remaining: ", game_state.game_prop_remaining())
print("\n")



"""

print(cell_four.node_name)
print(cell_four.move)
print(cell_four.p_x_wins())
print(cell_four.p_o_wins())
print(cell_four.p_draw())
print("\n")

print("num moves: ", game_state.num_moves())
print("moves list: ", game_state.moves_list())
print("next up:", game_state.next_up())
print("proportion of game remaining: ", game_state.game_prop_remaining())
print("\n")

print(cell_seven.node_name)
print(cell_seven.move)
print(cell_seven.p_x_wins())
print(cell_seven.p_o_wins())
print(cell_seven.p_draw())
print("\n")

print("num moves: ", game_state.num_moves())
print("moves list: ", game_state.moves_list())
print("next up:", game_state.next_up())
print("proportion of game remaining: ", game_state.game_prop_remaining())
print("\n")

print(cell_eight.node_name)
print(cell_eight.move)
print(cell_eight.p_x_wins())
print(cell_eight.p_o_wins())
print(cell_eight.p_draw())
print("\n")

print("num moves: ", game_state.num_moves())
print("moves list: ", game_state.moves_list())
print("next up:", game_state.next_up())
print("proportion of game remaining: ", game_state.game_prop_remaining())
print("\n")

# input = ["X", "O", "X", "O", " ", "X", "O", " ", " "]

#  O |   |
# -----------
#  O |   | X
# -----------
#  X | O | X

# left file
left_file = Win_triplet(cell_six, cell_three, cell_zero, "left file")
# P(X_wins) = 0, 0, 1
# P(O_wins) = 1, 1, 0
# P(draw)   = 0, 0, 0

print("left file: p_x_wins:", left_file.p_x_wins())
print("left file: p_o_wins:", left_file.p_o_wins())
print("left file: p_draw:", left_file.p_draw())
print("\n")

# center file
center_file = Win_triplet(cell_seven, cell_four, cell_one, "center file")
# P(X_wins) = 0, 0, 0
# P(O_wins) = 0, 0, 1
# P(draw)   = 1, 1, 0

print("center file: p_x_wins:", center_file.p_x_wins())
print("center file: p_o_wins:", center_file.p_o_wins())
print("center file: p_draw:", center_file.p_draw())
print("\n")

# right file
right_file = Win_triplet(cell_eight, cell_five, cell_two, "right file")
# P(X_wins) = 0, 1, 1
# P(O_wins) = 0, 0, 0
# P(draw)   = 1, 0, 0

print("right file: p_x_wins:", right_file.p_x_wins())
print("right file: p_o_wins:", right_file.p_o_wins())
print("right file: p_draw:", right_file.p_draw())
print("\n")

# bottom rank
bottom_rank = Win_triplet(cell_zero, cell_one, cell_two, "bottom rank")
# P(X_wins) = 1, 0, 1
# P(O_wins) = 0, 1, 0
# P(draw)   = 0, 0, 0

print("bottom rank: p_x_wins:", bottom_rank.p_x_wins())
print("bottom rank: p_o_wins:", bottom_rank.p_o_wins())
print("bottom rank: p_draw:", bottom_rank.p_draw())
print("\n")

# middle rank
middle_rank = Win_triplet(cell_three, cell_four, cell_five, "middle rank")
# P(X_wins) = 0, 0, 1
# P(O_wins) = 1, 0, 0
# P(draw)   = 0, 1, 0

print("middle rank: p_x_wins:", middle_rank.p_x_wins())
print("middle rank: p_o_wins:", middle_rank.p_o_wins())
print("middle rank: p_draw:", middle_rank.p_draw())
print("\n")

# top rank
top_rank = Win_triplet(cell_six, cell_seven, cell_eight, "top rank")
# P(X_wins) = 0, 0, 0
# P(O_wins) = 1, 0, 0
# P(draw)   = 0, 1, 1

print("top rank: p_x_wins:", top_rank.p_x_wins())
print("top rank: p_o_wins:", top_rank.p_o_wins())
print("top rank: p_draw:", top_rank.p_draw())
print("\n")

# left diagonal
left_diagonal = Win_triplet(cell_six, cell_four, cell_two, "left diagonal")
# P(X_wins) = 0, 0, 1
# P(O_wins) = 1, 0, 0
# P(draw)   = 0, 1, 0

print("left diagonal: p_x_wins:", left_diagonal.p_x_wins())
print("left diagonal: p_o_wins:", left_diagonal.p_o_wins())
print("left diagonal: p_draw:", left_diagonal.p_draw())
print("\n")

# right diagonal
right_diagonal = Win_triplet(cell_eight, cell_four, cell_zero, "right diagonal")
# P(X_wins) = 0, 0, 1
# P(O_wins) = 0, 0, 0
# P(draw)   = 1, 1, 0

print("right diagonal: p_x_wins:", right_diagonal.p_x_wins())
print("right diagonal: p_o_wins:", right_diagonal.p_o_wins())
print("right diagonal: p_draw:", right_diagonal.p_draw())
print("\n")
"""