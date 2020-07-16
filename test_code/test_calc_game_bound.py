# test calc_game_bound

from make_play import calc_game_bound

# game_history index range:
# x wins in 5 moves:             12,000 -      99,000
# o wins in 6 moves:            120,000 -     990,000
# x wins in 7 moves:          1,200,000 -   9,900,000
# o wins in 8 moves:         12,000,000 -  99,000,000
# x win or draw in 9 moves: 120,000,000 - 990,000,000

board0 = [0]
board1 = [8]
board2 = [0, 1]
board3 = [8, 7]
board4 = [0, 1, 2]
board5 = [8, 7, 6]
board6 = [0, 1, 2, 3]
board7 = [8, 7, 6, 5]
board8 = [0, 1, 2, 3, 4]
board9 = [8, 7, 6, 5, 4]
board10 = [0, 1, 2, 3, 4, 5]
board11 = [8, 7, 6, 5, 4, 3]
board12 = [0, 1, 2, 3, 4, 5, 6]
board13 = [8, 7, 6, 5, 4, 3, 2]
board14 = [0, 1, 2, 3, 4, 5, 6, 7]
board15 = [8, 7, 6, 5, 4, 3, 2, 1]

board_list = [board0, board1, board2, board3, board4, board5, board6, board7,
              board8, board9, board10, board11, board12, board13, board14, board15]

#board_list = [board14, board15]

for game in range(len(board_list)):
    #print("game =", game)
    if len(board_list[game]) % 2 == 1:
        agent = 'X'
    else:
        agent = 'O'
    #print("agent = ", agent)
    lower_copy = board_list[game].copy()
    upper_copy = board_list[game].copy()
    padded_game_lower = calc_game_bound(lower_copy, agent, 'L')
    padded_game_upper = calc_game_bound(upper_copy, agent, 'U')

    print("Agent: ", agent, " - Lower: ", board_list[game], " = ", padded_game_lower)
    print("Agent: ", agent, " - Upper: ", board_list[game], " = ", padded_game_upper)
