# calculate the current probable outcome

from rank_file_nodes import left_file, middle_file, right_file, bottom_rank, center_rank, top_rank, left_diagonal, right_diagonal


def outcome(this_board):

    outcome_weight = 1
    print_outcome = True

    leftfile = left_file(this_board)
    middlefile = middle_file(this_board)
    rightfile = right_file(this_board)
    bottomrank = bottom_rank(this_board)
    centerrank = center_rank(this_board)
    toprank = top_rank(this_board)
    leftdiagonal = left_diagonal(this_board)
    rightdiagonal = right_diagonal(this_board)

    file_probs = leftfile + middlefile + rightfile
    rank_probs = bottomrank + centerrank + toprank
    diag_probs = leftdiagonal + rightdiagonal

    sum_of_probs = file_probs + rank_probs + diag_probs

    evidence_avg = sum_of_probs / 8

    if print_outcome:
        print("Sum of probabilities:", sum_of_probs)
        print("Current probable outcome =", evidence_avg * outcome_weight)

    return evidence_avg * outcome_weight

