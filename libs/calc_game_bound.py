# refactored by Russell on 3/5/21
# is this vestigial?  can't find any calls

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
                # print(padded_game)
                break

    #print('calc_game_bound: padded game = ', padded_game)
    return padded_game
