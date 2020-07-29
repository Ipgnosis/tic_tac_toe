# makes a play on the board for the next player
# includes agent_x and agent_o
# written by Russell on 4/9/20
# rewritten by Russell on 5/6/20 for new game data structure
# takes the board (list) as a parameter
import sys
sys.path.append('tic_tac_toe')

from libs.compare import get_transposed_games, reorient_games
from libs.game_over import win_loss
from libs.print_board import tty_print
from libs.move_utils import get_open_cells, random_move

# look for 2 agent moves in a win vector
def can_win(board, agent):

    ### note that if len(board) == 8, then either:
    ### A. the winning move will be revealed OR
    ### B. an impending draw will return False
    ### however, the game_history will reveal the winning move or, if not,
    ### best_move() will default to a random move, of which there is only 1

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

# pad out a game to a win length for a given agent, calcualting the lower and upper game index
def calc_game_bound(this_game, agent, bound):

    lower_play_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    upper_play_list = [8, 7, 6, 5, 4, 3, 2, 1, 0]

    padded_game = this_game.copy()
    num_moves = len(this_game)
    win_in = 0

    # are we padding a lower bound or an upper bound?
    if bound == 'L':
        play_list = lower_play_list
    else:
        play_list = upper_play_list

    #print('calc_game_bound: play list =', play_list)

    # calculate the amount of 'padding' to be applied
    if num_moves <= 4 and agent == 'X':
        win_in = 5
    elif num_moves <= 5 and agent == 'O':
        win_in = 6
    else:
        win_in = num_moves + 1

    #print('win_in:', win_in)

    #print('this_game =', this_game)
    # pad out the game moves so we can get a lower or upper bound index
    while len(padded_game) < win_in:

        for play in play_list:
            if play not in padded_game:
                padded_game.append(play)
                #print(padded_game)
                break

    #print('calc_game_bound: padded game = ', padded_game)
    return padded_game

# find the best move for this agent, based on prior games in the game_history
def best_move(this_board, agent, ttt_base):
    
    candidate_games = []
    lower_bound = 0
    upper_bound = 0
    num_moves = len(this_board)
    bounds_list = []

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

    # TRANSPOSE the current game state into 9 different games and store in a list
    # the returned value is a list of dictionaries that contain the transposed game
    # and the source function, to allow the game to be transposed back
    tg_list = get_transposed_games(this_board)

    #print("best_move: tg_list =", tg_list)

    # build a list of lower and upper bound tuples for the tg_list using calc_game_bound
    for tgame in tg_list:
        lower_bound = calc_game_bound(tgame["transpose"], agent, 'L')
        upper_bound = calc_game_bound(tgame["transpose"], agent, 'U')
        bounds_tuple = (lower_bound, upper_bound)
        bounds_list.append(bounds_tuple)
        #print("best_move: bounds_tuple =", bounds_tuple)

    # fetch the list of candidate winning games from the game history
    candidate_games = ttt_base.get_games_list(bounds_list)

    #print("best_move: candidate_games =", candidate_games)

    if candidate_games != False:

        # de-transpose the candidate games to get the right cell for the next move
        reoriented_candidates = reorient_games(tg_list, candidate_games)

        #print("RO candidates = ", reoriented_candidates)
        
        # build a dict of the frequency of the winning next moves
        candidate_moves = {}

        ###################################################################################
        ### this probably needs to be rewritten as it just perpetuates bad play choices ###
        for game in range(len(reoriented_candidates)):
            if reoriented_candidates[game][num_moves] not in candidate_moves:
                candidate_moves[reoriented_candidates[game][num_moves]] = 1
            else:
                candidate_moves[reoriented_candidates[game][num_moves]] += 1

        #print("candidate_moves =", candidate_moves)
        
        # calculate the best move from the candidate_moves dict
        recommended_move = max(candidate_moves, key=candidate_moves.get)
        ####################################################################################
        
        #print("best_move: move = ", recommended_move)

        return recommended_move

    else:  # there are no matching games in the game history
        #print("best_move: random choice...")
        return random_move(this_board)

# agent cross - this allows each agent to play differently
def agent_x(board, ml_base, mode, curr_probs):

    #### note that curr_probs not being used, but will be used soon to calculate best move

    # select random mode
    if mode == 'random':

        move = random_move(board)

    # select human interaction
    elif mode == 'human':

        move = human_move(board, "X")
    
    # select best mode
    elif mode == 'best':
        
        # use best_move agency to select move choice
        move = best_move(board, "X", ml_base)

    else:
        print("agent_x error: invalid move mode")
        move = False

    #worst_move = can_lose(next_move)

    #print("agent_x: move type = " + str(type(move)))
    #print("agent_x selected cell: " + str(move))

    # return move so that it can be recorded in the game log
    return move

# agent nought - this allows each agent to play differently
def agent_o(board, ml_base, mode, curr_probs):

    #### note that curr_probs not being used, but will be used soon to calculate best move

    # select random mode
    if mode == 'random':

        move = random_move(board)

    # select human interaction
    elif mode == 'human':

        # select human interaction
        move = human_move(board, "O")

    # select best mode
    elif mode == 'best':

        # use best_move agency to select move choice
        move = best_move(board, "O", ml_base)
    
    else:
        print("agent_o error: invalid move mode")
        move = False

    #worst_move = can_lose(next_move)

    #print("agent_o: move type = " + str(type(move)))
    #print("agent_o selected cell: " + str(move))

    # return move so that it can be recorded in the game log
    return move
