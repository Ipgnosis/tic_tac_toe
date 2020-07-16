
"""
# test calls
zero = board_cell(0, 'zero')

print(zero.position)
print(zero.node_name)
zero.move = 'X'
print(zero.p_x_wins())
print(zero.p_o_wins())
print(zero.p_draw())
print(zero.cell_contains())

"""

# returns:
# 0 * weight for empty
# 1 * weight for 'X' (cross)
# -1 * weight for 'O' (nought)

#cell_weights = [1, 1, 1, 1, 1, 1, 1, 1, 1]

# cell node for cell zero

def zero(this_board):
    this_cell = 0
    index = 0 # starting default value
    node_name = "zero"
    cell_weight = cell_weights[this_cell]

    if this_cell in this_board:
        index = this_board.index(this_cell)
        if index % 2 == 0 or index == 0:
            if print_cell_results:
                # cell contains "X"
                print("Cell", node_name, ":", 1 * cell_weight)
            return 1 * cell_weight
        else:
            # cell contains "O"
            if print_cell_results:
                print("Cell", node_name, ":", -1 * cell_weight)
            return -1 * cell_weight
    else:
        # cell is empty
        if print_cell_results:
            print("Cell", node_name, ":", 0 * cell_weight)
        return 0 * cell_weight

# cell node for cell 1


def one(this_board):
    this_cell = 1
    node_name = "one"
    cell_weight = cell_weights[this_cell]

    if this_cell in this_board:
        index = this_board.index(this_cell)
        if index % 2 == 0 or index == 0:
            if print_cell_results:
                # cell contains "X"
                print("Cell", node_name, ":", 1 * cell_weight)
            return 1 * cell_weight
        else:
            # cell contains "O"
            if print_cell_results:
                print("Cell", node_name, ":", -1 * cell_weight)
            return -1 * cell_weight
    else:
        # cell is empty
        if print_cell_results:
            print("Cell", node_name, ":", 0 * cell_weight)
        return 0 * cell_weight

# cell node for cell 2


def two(this_board):
    this_cell = 2
    node_name = "two"
    cell_weight = cell_weights[this_cell]

    if this_cell in this_board:
        index = this_board.index(this_cell)
        if index % 2 == 0 or index == 0:
            if print_cell_results:
                # cell contains "X"
                print("Cell", node_name, ":", 1 * cell_weight)
            return 1 * cell_weight
        else:
            # cell contains "O"
            if print_cell_results:
                print("Cell", node_name, ":", -1 * cell_weight)
            return -1 * cell_weight
    else:
        # cell is empty
        if print_cell_results:
            print("Cell", node_name, ":", 0 * cell_weight)
        return 0 * cell_weight

# cell node for cell 3


def three(this_board):
    this_cell = 3
    node_name = "three"
    cell_weight = cell_weights[this_cell]

    if this_cell in this_board:
        index = this_board.index(this_cell)
        if index % 2 == 0 or index == 0:
            if print_cell_results:
                # cell contains "X"
                print("Cell", node_name, ":", 1 * cell_weight)
            return 1 * cell_weight
        else:
            # cell contains "O"
            if print_cell_results:
                print("Cell", node_name, ":", -1 * cell_weight)
            return -1 * cell_weight
    else:
        # cell is empty
        if print_cell_results:
            print("Cell", node_name, ":", 0 * cell_weight)
        return 0 * cell_weight
# cell node for cell 4


def four(this_board):
    this_cell = 4
    node_name = "four"
    cell_weight = cell_weights[this_cell]

    if this_cell in this_board:
        index = this_board.index(this_cell)
        if index % 2 == 0 or index == 0:
            if print_cell_results:
                # cell contains "X"
                print("Cell", node_name, ":", 1 * cell_weight)
            return 1 * cell_weight
        else:
            # cell contains "O"
            if print_cell_results:
                print("Cell", node_name, ":", -1 * cell_weight)
            return -1 * cell_weight
    else:
        # cell is empty
        if print_cell_results:
            print("Cell", node_name, ":", 0 * cell_weight)
        return 0 * cell_weight

# cell node for cell 5


def five(this_board):
    this_cell = 5
    node_name = "five"
    cell_weight = cell_weights[this_cell]

    if this_cell in this_board:
        index = this_board.index(this_cell)
        if index % 2 == 0 or index == 0:
            if print_cell_results:
                # cell contains "X"
                print("Cell", node_name, ":", 1 * cell_weight)
            return 1 * cell_weight
        else:
            # cell contains "O"
            if print_cell_results:
                print("Cell", node_name, ":", -1 * cell_weight)
            return -1 * cell_weight
    else:
        # cell is empty
        if print_cell_results:
            print("Cell", node_name, ":", 0 * cell_weight)
        return 0 * cell_weight

# cell node for cell 6


def six(this_board):
    this_cell = 6
    node_name = "six"
    cell_weight = cell_weights[this_cell]

    if this_cell in this_board:
        index = this_board.index(this_cell)
        if index % 2 == 0 or index == 0:
            if print_cell_results:
                # cell contains "X"
                print("Cell", node_name, ":", 1 * cell_weight)
            return 1 * cell_weight
        else:
            # cell contains "O"
            if print_cell_results:
                print("Cell", node_name, ":", -1 * cell_weight)
            return -1 * cell_weight
    else:
        # cell is empty
        if print_cell_results:
            print("Cell", node_name, ":", 0 * cell_weight)
        return 0 * cell_weight

# cell node for cell 7


def seven(this_board):
    this_cell = 7
    node_name = "seven"
    cell_weight = cell_weights[this_cell]

    if this_cell in this_board:
        index = this_board.index(this_cell)
        if index % 2 == 0 or index == 0:
            if print_cell_results:
                # cell contains "X"
                print("Cell", node_name, ":", 1 * cell_weight)
            return 1 * cell_weight
        else:
            # cell contains "O"
            if print_cell_results:
                print("Cell", node_name, ":", -1 * cell_weight)
            return -1 * cell_weight
    else:
        # cell is empty
        if print_cell_results:
            print("Cell", node_name, ":", 0 * cell_weight)
        return 0 * cell_weight

# cell node for cell 8


def eight(this_board):
    this_cell = 8
    node_name = "eight"
    cell_weight = cell_weights[this_cell]

    if this_cell in this_board:
        index = this_board.index(this_cell)
        if index % 2 == 0 or index == 0:
            if print_cell_results:
                # cell contains "X"
                print("Cell", node_name, ":", 1 * cell_weight)
            return 1 * cell_weight
        else:
            # cell contains "O"
            if print_cell_results:
                print("Cell", node_name, ":", -1 * cell_weight)
            return -1 * cell_weight
    else:
        # cell is empty
        if print_cell_results:
            print("Cell", node_name, ":", 0 * cell_weight)
        return 0 * cell_weight

