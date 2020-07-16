

from cell_nodes import zero, one, two, three, four, five, six, seven, eight

# order of weights for rank_file_weights
rank_file_weights = [1, 1, 1, 1, 1, 1, 1, 1]
print_rank_file_results = True
divisor = 3

def left_file(this_board):

    cell_1 = six(this_board)
    cell_2 = three(this_board)
    cell_3 = zero(this_board)
    node_name = "Left file:"
    this_weight = rank_file_weights[0]

    result = (cell_1 + cell_2 + cell_3) / divisor * this_weight

    if print_rank_file_results:
        print(node_name, result)

    return result

# the neural_node for the middle_file


def middle_file(this_board):

    cell_1 = seven(this_board)
    cell_2 = four(this_board)
    cell_3 = one(this_board)
    node_name = "Middle file:"
    this_weight = rank_file_weights[1]

    result = (cell_1 + cell_2 + cell_3) / divisor * this_weight

    if print_rank_file_results:
        print(node_name, result)

    return result

# the neural_node for the right_file


def right_file(this_board):

    cell_1 = eight(this_board)
    cell_2 = five(this_board)
    cell_3 = two(this_board)
    node_name = "Right file:"
    this_weight = rank_file_weights[2]

    result = (cell_1 + cell_2 + cell_3) / divisor * this_weight

    if print_rank_file_results:
        print(node_name, result)

    return result

# the neural_node for the bottom rank


def bottom_rank(this_board):

    cell_1 = zero(this_board)
    cell_2 = one(this_board)
    cell_3 = two(this_board)
    node_name = "Bottom rank:"
    this_weight = rank_file_weights[3]

    result = (cell_1 + cell_2 + cell_3) / divisor * this_weight

    if print_rank_file_results:
        print(node_name, result)

    return result

# the neural_node for the center rank


def center_rank(this_board):

    cell_1 = three(this_board)
    cell_2 = four(this_board)
    cell_3 = five(this_board)
    node_name = "Center rank:"
    this_weight = rank_file_weights[4]

    result = (cell_1 + cell_2 + cell_3) / divisor * this_weight

    if print_rank_file_results:
        print(node_name, result)

    return result

# the neural_node for the top rank


def top_rank(this_board):

    cell_1 = six(this_board)
    cell_2 = seven(this_board)
    cell_3 = eight(this_board)
    node_name = "Top rank:"
    this_weight = rank_file_weights[5]

    result = (cell_1 + cell_2 + cell_3) / divisor * this_weight

    if print_rank_file_results:
        print(node_name, result)

    return result

# the neural_node for the left diagonal


def left_diagonal(this_board):

    cell_1 = six(this_board)
    cell_2 = four(this_board)
    cell_3 = two(this_board)
    node_name = "Left diagonal:"
    this_weight = rank_file_weights[6]

    result = (cell_1 + cell_2 + cell_3) / divisor * this_weight

    if print_rank_file_results:
        print(node_name, result)

    return result

# the neural_node for the right diagonal


def right_diagonal(this_board):

    cell_1 = eight(this_board)
    cell_2 = four(this_board)
    cell_3 = zero(this_board)
    node_name = "Right diagonal:"
    this_weight = rank_file_weights[7]

    result = (cell_1 + cell_2 + cell_3) / divisor * this_weight

    if print_rank_file_results:
        print(node_name, result)

    return result

