# a set of move utility functions required to be imported by several different files
# written by Russell on 4/9/20
# rewritten by Russell on 5/6/20 for new game data structure

import random

# determine which player moves next


def next_player(this_game):

    moves_made = len(this_game)
    #print("next_player: moves_made =", moves_made)

    if moves_made % 2 == 0 or moves_made == 0:
        return "X"
    else:
        return "O"

# get list of open cells


def get_open_cells(this_game):

    open_cell_list = []
    all_cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # a list of the cells

    for cell in range(len(all_cells)):
        if all_cells[cell] not in this_game:
            open_cell_list.append(cell)

    return open_cell_list

# randomly select move on board from open cells


def random_move(this_game):

    open_cells = get_open_cells(this_game)

    chosen = random.choice(open_cells)

    #print("random_move: chosen = ", type(chosen), chosen)

    return chosen


# queries input from the user based on a game state and returns the chosen move


def human_move(this_board, player):

    valid_move = False

    open_moves = get_open_cells(this_board)

    while not valid_move:

        move = int(input("Your move: enter an int 0:8 in an empty space - "))

        if move not in open_moves:
            print("Invalid move...choose any of the following:", open_moves)
        else:
            valid_move = True

    return move
