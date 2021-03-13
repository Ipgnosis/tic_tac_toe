# makes a play on the board for the next player
# includes agent_x and agent_o
# written by Russell on 4/9/20
# rewritten by Russell on 5/6/20 for new game data structure
# refactored by Russell on 3/5/21 to simplify - moved functions to other files
# takes the board (list) as a parameter
from libs.move_utils import random_move, human_move
from libs.best_move import best_move


# agent cross - this allows each agent to play differently


def agent_x(board, ttt_base, mode):

    # select random mode
    if mode == 'random':

        move = random_move(board)

    # select human interaction
    elif mode == 'human':

        move = human_move(board, "X")

    # select best mode
    elif mode == 'best':

        # use best_move agency to select move choice
        move = best_move(board, "X", ttt_base)

    else:
        print("agent_x error: invalid move mode")
        move = False

    #worst_move = can_lose(next_move)

    #print("agent_x: move type = " + str(type(move)))
    #print("agent_x selected cell: " + str(move))

    # return move so that it can be recorded in the game log
    return move

# agent nought - this allows each agent to play differently


def agent_o(board, ttt_base, mode):

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
        move = best_move(board, "O", ttt_base)

    else:
        print("agent_o error: invalid move mode")
        move = False

    #worst_move = can_lose(next_move)

    #print("agent_o: move type = " + str(type(move)))
    #print("agent_o selected cell: " + str(move))

    # return move so that it can be recorded in the game log
    return move
