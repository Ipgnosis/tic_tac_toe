# class to calculate the probabilities of winning, losing and drawing
# for a given a board state and/or for a set of potential next moves
# written by Russell on 7/1/20

class TTTProbs:

    # initialize the class instance

    def __init__(self, x_win_pct=None, o_win_pct=None, draw_pct=None):

        # set up the priors from the stored game_history via instantiation params
        # if the game history is a new file, use the random game defaults
        # these values are dynamic throughout the game run
        # although the (modified) probs are stored in the game_history by default
        # the dynamic probs might not match them.  check this going forward.
        if x_win_pct is None:
            self.prior_x_win_pct = 0.584485
        else:
            self.prior_x_win_pct = x_win_pct

        if o_win_pct is None:
            self.prior_o_win_pct = 0.288464
        else:
            self.prior_o_win_pct = o_win_pct

        if draw_pct is None:
            self.prior_draw_pct = 0.127051
        else:
            self.prior_draw_pct = draw_pct

        """
        #### not currently in use ####
        # initialize the weights for the cell types
        # calculated as the number of cells in the win vectors (8 x 3 = 24)
        # divided by the number of vectors affected by each cell of that type
        # each corner cell affects 3 vectors: 2 / 24 = 1 / 8 = 0.125
        self.corner_val = 0.125
        # each edge affects 2 vectors: 2 / 24 = 1 / 12 = 0.083333...
        self.edge_val = 1 / 12
        # the center affects 4 vectors: 4 / 24 = 1 / 6 = 0.166666...
        self.center_val = 1 / 6

        # a list of cell weights for cells 0 - 8
        self.cell_weights = [self.corner_val, self.edge_val, self.corner_val,
                             self.edge_val, self.center_val, self.edge_val, self.corner_val,
                             self.edge_val, self.corner_val]

        """

        # set up the win vectors in a tuple of tuples
        self.win_vectors = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (6, 3, 0),
                            (7, 4, 1), (8, 5, 2), (6, 4, 2), (8, 4, 0))

        # set the vector states for a new game
        self.reset_vector_states()

    # calculate the probabilities of a win, loss and draw for a given game state for the 
    # MOVE that was JUST MADE and the PLAYER who JUST PLAYED - we are evaluating the move relative to
    # the current game state - these numbers should add up to 1
    def get_probs(self, game_board):

        # if no play has been made in the game so far, return the prior win percentages
        if len(game_board) == 0:
            # return the win/loss/draw percentages
            return (self.prior_x_win_pct, self.prior_o_win_pct, self.prior_draw_pct)

        # if at least one play has been made, calculate the probs for the game in progress
        else:

            # identify the players for the move just played
            players = self.id_players(game_board)
            last_player = players[0]
            next_player = players[1]

            # reset the vector states for the last move
            # note that vector state is preseverved and updated throughout the game until reset
            self.set_vector_states(game_board, last_player)

            # initialize the variables for the current move            
            p_win = p_draw = p_loss = 0
            possible_win_vectors = 8
            potential_loss_vectors = potential_win_vectors = draw_vectors = 0

            # existence of 'lost cause' value in a game vector eliminates that vector as a win candidate
            if last_player == "O":
                # note that "X" means 2 cells occupied by X and an empty cell;
                # "x" means 1 cell occupied and two empty cells
                lost_cause_set = {"D", "X", "x"}
            else:
                # note that "O" means 2 cells occupied by O and an empty cell; 
                # "o" means 1 cell occupied and two empty cells
                lost_cause_set = {"D", "O", "o"}

            # iterate through the vector states tallying the game state variables
            for vector_state in range(len(self.vector_states)):
                # if the vector is a lost cause or a low win probability (None)
                if self.vector_states[vector_state] in lost_cause_set or self.vector_states[vector_state] == None:
                    # reduce the possible_win_vectors by 1
                    possible_win_vectors -= 1

                # if the vector currently has 2 next_player plays and 1 open cell
                if self.vector_states[vector_state] == next_player:
                    potential_loss_vectors += 1
                # if the vector NOW has 2 last_player plays and 1 open cell
                elif self.vector_states[vector_state] == last_player:
                    potential_win_vectors += 1
                # if the vector is in a draw state: at least one cell occupied by both players
                elif self.vector_states[vector_state] == "D":
                    draw_vectors += 1

            # debugging statements
            #print("TTTProbs.set_vector_states =", self.vector_states)
            #print("TTTProbs: get_probs - agent {} - poss_win = {}, pot_loss = {}, pot_win = {}, draw = {}".format(
            #    last_player, possible_win_vectors, potential_loss_vectors, potential_win_vectors, draw_vectors))

            #### calculate the probabilities ####
            # if the last_player has a win_vector with 2+ occupied cells and an empty cell or
            # created a fork (potential wins on > 1 vectors) that opponent can't block
            if potential_win_vectors > 1:
                # last_player can win on the move after next
                p_win = 1
            # if the next_player has a 1+ win chances on the next play
            elif potential_loss_vectors >= 1:
                # last_player can't win
                p_loss = 1
            # all vectors have at least one play from each player
            # which means that a draw is the only possible outcome
            elif draw_vectors == 8:
                p_draw = 1
            # no impending wins, losses or draws;
            # possible_win_vectors > 0
            else:
                p_win = possible_win_vectors / 8
                p_draw = draw_vectors / 8
                p_loss = 1 - p_win - p_draw

            # debug warning on sum of probabilities being out of alignment
            sum_of_probs = p_win + p_loss + p_draw
            if sum_of_probs != 1:
                print("TTTProbs: get_probs ERROR = sum of probs != 1:", sum_of_probs)

            # return the current probabilities for the last player, based on the last move 
            return (last_player, p_win, p_loss, p_draw)

    # this method takes the game_board and analyzes the last move against the vector_states
    # and sets 'D', 'X', 'x', 'O' or 'o' as required - this keeps a running tally of the game state
    # no result is returned
    def set_vector_states(self, this_game, last_player):

        # note that the probabilities are calculated based on the last move made
        # therefore, 'last_player' is the player that just made a move
        # the opponent is the next player to make a move
        # set the variables
        if last_player == "O":
            opponent = "X"
            opponent_one_play = "x"
            one_play = "o"
        else:
            opponent = "O"
            opponent_one_play = "o"
            one_play = "x"

        # get the cell chosen in the last move
        last_play = this_game[-1]
        #print("set_vector_states: last_play = ", last_play)

        # iterate over the vector_states to set or reset the values
        for vector_state in range(len(self.vector_states)):
            # skip over any vector in the 'draw' state - nothing to do
            if self.vector_states[vector_state] != "D":
                # find the win_vectors containing the last move so far
                # note that the same cell can occur in up to 4 win_vectors...
                if last_play in self.win_vectors[vector_state]:
                    # if this vector_state has not yet been assigned a value
                    if self.vector_states[vector_state] is None:
                        # assign the value of the last player
                        self.vector_states[vector_state] = one_play
                    # if this vector_state already contains a move from the last player
                    # assign "X" or "O" to indicate impending win
                    elif self.vector_states[vector_state] == one_play:
                        self.vector_states[vector_state] = last_player
                    # if the vector_state contains at least one move of the opponent
                    elif self.vector_states[vector_state] == opponent or self.vector_states[vector_state] == opponent_one_play:
                        # assign a draw as there are now both players in cells in that vector
                        self.vector_states[vector_state] = "D"

    # this method resets the vector states for a new game
    # this eliminates the need to reinstantiate an object for a new game
    # no result is returned
    def reset_vector_states(self):

        # initialize 8 win vector variable states to None
        self.left_file = None
        self.center_file = None
        self.right_file = None
        self.bottom_rank = None
        self.middle_rank = None
        self.top_rank = None
        self.left_diagonal = None
        self.right_diagonal = None

        # set up a list of the win vector states
        # note that the list order is aligned with win_vectors tuple
        # possible values:
        #   None = no cells occupied
        #   "D" = at least two cells occupied, one for each player, therefore this vector is a local draw
        #   "x" = one cell is occupied by player X, so player O cannot win on this vector
        #   "X" = two cells are occupied by player X, so player O is in danger of losing on this vector
        #   "o" =  one cell is occupied by player O, so player X cannot win on this vector
        #   "O" =  two cells are occupied by player O, so player X is in danger of losing on this vector
        self.vector_states = [self.bottom_rank, self.middle_rank, self.top_rank,
                              self.left_file, self.center_file, self.right_file,
                              self.left_diagonal, self.right_diagonal]

        #print("reset_vector_states: reset")

    # determine which player moved last ahd which will move next
    #### need this now?
    def id_players(self, this_game):

        moves_made = len(this_game)
        #print("last_player: moves_made =", moves_made)

        # return a tuple: (last player, next player)
        if moves_made % 2 == 0:
            return ("O", "X")
        else:
            return ("X", "O")
