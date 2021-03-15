# refactored from make_play to simplify
# by Russell on 3/5/21

from libs.move_utils import get_open_cells, random_move
from libs.compare import get_transposed_games, reorient_games
from libs.calc_game_bound import calc_game_bound

# look for 2 agent moves in a win vector


def can_win(board, agent):

    # note that if len(board) == 8, then either:
    # A. the winning move will be revealed OR
    # B. an impending draw will return False
    # however, the game_history will reveal the winning move or, if not,
    # best_move() will default to a random move, of which there is only 1

    game_len = len(board)

    open_cells = get_open_cells(board)

    agent_moves = []

    if agent == "X":

        # compile a list of moves made by agent "X"
        for move in range(0, game_len, 2):
            agent_moves.append(board[move])

    else:  # agent == "O"

        # compile a list of moves made by agent "O"
        for move in range(1, game_len, 2):
            agent_moves.append(board[move])

    # all win vectors in a tuple of tuples
    win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (6, 3, 0),
                  (7, 4, 1), (8, 5, 2), (6, 4, 2), (8, 4, 0))

    # evaluate each win vector and return the missing move if there are 2 agent moves in a vector
    for combo in win_combos:
        if combo[0] in agent_moves and combo[1] in agent_moves and combo[2] in open_cells:
            return (True, combo[2])

        if combo[1] in agent_moves and combo[2] in agent_moves and combo[0] in open_cells:
            return (True, combo[0])

        if combo[0] in agent_moves and combo[2] in agent_moves and combo[1] in open_cells:
            return (True, combo[1])

    # if no near-win vectors are found, send False
    return (False, None)


# find the best move for this agent, based on prior games in the game_history


def best_move(this_board, agent, ttt_base):

    candidate_games = []
    lower_bound = 0
    upper_bound = 0
    num_moves = len(this_board)
    bounds_list = []

    #### this is a kluge and needs to be removed when the probability function is working ####
    #### right now, it is just stopping bad moves from being recorded in the game history ####

    # check to see if a quick win can be achieved
    if num_moves >= 4:
        quick_win = can_win(this_board, agent)

        if quick_win[0] == True:
            return quick_win[1]

    # since no quick wins, check for an impending loss that must be blocked
    # agent O could win on moves 6 or 8
    if agent == "X" and num_moves >= 4:
        block_loss = can_win(this_board, "O")
    # agent X could win on moves 5, 7, 9
    elif agent == "O" and num_moves >= 3:
        block_loss = can_win(this_board, "X")
    else:
        block_loss = (False, None)

    if block_loss[0]:
        return block_loss[1]

    #### end of kluge ####

    # TRANSPOSE the current game state into 8 different games and store in a list
    # the returned value is a list of dictionaries that contain the transposed game
    # and the source function, to allow the game to be transposed back
    tg_list = get_transposed_games(this_board)

    #print("best_move: tg_list =", tg_list)

    # for each of the 8 transposed versions of the current game in question
    # build a list of lower and upper bound tuples for the tg_list using calc_game_bound
    for tgame in tg_list:
        lower_bound = calc_game_bound(tgame["transpose"], agent, 'L')
        upper_bound = calc_game_bound(tgame["transpose"], agent, 'U')
        bounds_tuple = (lower_bound, upper_bound)
        bounds_list.append(bounds_tuple)
        #print("best_move: bounds_tuple =", bounds_tuple)

    # fetch the list of candidate WINNING games from the game history
    candidate_games = ttt_base.get_games_list(bounds_list)

    #print("best_move: candidate_games =", candidate_games)

    # if there is at least one game that matches the current game state
    if candidate_games != False:

        # this is the list of games that match the transposed game list
        # de-transpose the candidate games to get the right cell for the next move
        reoriented_candidates = reorient_games(tg_list, candidate_games)

        #print("RO candidates = ", reoriented_candidates)
        print("best_move: number of candidate games = ",
              len(reoriented_candidates))

        #high_prob_game = ""
        high_prob_move = 0
        high_prob_prob = 0.0

        # iterate though the game candidates
        for game in range(len(reoriented_candidates)):

            if candidate_games[game]["probs"][num_moves][0] > high_prob_prob:
                #high_prob_game = candidate_games[game]
                high_prob_move = candidate_games[game]["game"][num_moves]
                high_prob_prob = candidate_games[game]["probs"][num_moves][0]

            print("best_move: move {}, new move choice = {}, P(win) = {}".format(
                num_moves, high_prob_move, high_prob_prob))

        recommended_move = high_prob_move
        """
        ###################################################################################
        ### this needs to be rewritten as it just perpetuates bad play choices ###
        ### use game_history["probs"] to caculate the probability of success ###

        # build a dict of the frequency of the winning next moves
        candidate_moves = {}
        
        for game in range(len(reoriented_candidates)):
            if reoriented_candidates[game][num_moves] not in candidate_moves:
                candidate_moves[reoriented_candidates[game][num_moves]] = 1
            else:
                candidate_moves[reoriented_candidates[game][num_moves]] += 1

        print("candidate_moves =", candidate_moves)
        
        # the best move is the most frequently made move in the candidate_moves dict
        # logic = if this is the move that most often works, then this move (probably) can't be countered
        recommended_move = max(candidate_moves, key=candidate_moves.get)
        ####################################################################################
        """
        #print("best_move: move = ", recommended_move)

        return recommended_move

    else:  # there are no matching games in the game history
        #print("best_move: random choice...")
        return random_move(this_board)
