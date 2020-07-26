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

        # initialize a set of probabilities that we can tune later
        self.impossible = 0
        self.low = 0.1
        self.possible = 1 / 3
        self.probable = 2 / 3
        self.likely = 0.999
        self.win = 1
        """

        # set up the win vectors in a tuple of tuples
        self.win_vectors = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (6, 3, 0),
                            (7, 4, 1), (8, 5, 2), (6, 4, 2), (8, 4, 0))

        # set the vector states for a new game
        self.reset_vector_states()

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

    # calculate the probabilities of a win, loss and draw for a given game state
    # these numbers should add up to 1
    def get_probs(self, game_board):

        self.set_vector_states(game_board)

        p_win = p_draw = p_loss = 0
        possible_win_vectors = 8
        potential_loss_vectors = impending_win_vectors = draw_vectors = 0

        player = self.this_player(game_board)

        # existence of lost_cause_set values in vector_state eliminates
        # that vector as a win candidate
        if player == "O":
            # note that "X" means 2 cells occupied by X and an empty cell;
            # "x" means 1 cell occupied and two empty cells
            lost_cause_set = {"D", "X", "x"}
            opponent = "X"
        else:
            # note that "O" means 2 cells occupied by O and an empty cell; 
            # "o" means 1 cell occupied and two empty cells
            lost_cause_set = {"D", "O", "o"}
            opponent = "O"

        draw_state_set = {"D", None}

        # iterate through the vector states tallying the game state variables
        for vector_state in range(len(self.vector_states)):
            # if the vector is a lost cause, reduce the possible_win_vectors by 1
            if self.vector_states[vector_state] in lost_cause_set:
                possible_win_vectors -= 1

            # if the vector has 2 opponent plays and 1 open cell
            if self.vector_states[vector_state] == opponent:
                potential_loss_vectors += 1

            # if the vector has 2 player plays and 1 open cell
            if self.vector_states[vector_state] == player:
                impending_win_vectors += 1

            # if the vector is in a draw state: either at least one cell occupied by both players
            # or all empty cells - note that an empty vector is neither a won or lost vector, 
            # therefore it must be viewed as a draw vector for the purposes of calculating probabilities
            if self.vector_states[vector_state] in draw_state_set:
                draw_vectors += 1

        # debugging statements
        print("TTTProbs.set_vector_states =", self.vector_states)
        print("TTTProbs: get_probs - agent {} - poss_win = {}, pot_loss = {}, imp_win = {}, draw = {}".format(
            player, possible_win_vectors, potential_loss_vectors, impending_win_vectors, draw_vectors))

        # if the player has a win_vector with 2 occupied cells and an empty cell or
        # created a fork (pending wins on > 1 vectors) opponent can't block
        if impending_win_vectors >= 1:
            # player can win on next move
            p_win = 1

        # if the opponent has a fork (impending loss on > 1 vectors)
        elif potential_loss_vectors > 1:
            # player can't win
            p_loss = 1

        # there are no win vectors available and no impending wins/losses
        # which means that a draw is the only possible outcome
        elif possible_win_vectors == 0:
            p_draw = 1

        # no impending wins, losses or draws;
        # possible_win_vectors > 0
        else:
            p_win = possible_win_vectors / 8
            p_draw = draw_vectors / 8
            p_loss = 1 - p_win - p_draw

        """
        #p_win = self.calc_p_win(game_board)
        #p_loss = self.calc_p_loss(game_board)
        #p_draw = self.calc_p_draw(game_board)

        if p_win == 1:
            p_draw = 0
            p_loss = 0
        
        if p_draw == 1:
            p_win = 0
            p_loss = 0
        """

        # debug check on sum of probabilities
        sum_of_probs = p_win + p_loss + p_draw
        if sum_of_probs != 1:
            print("TTTProbs: get_probs ERROR = sum of probs != 1:", sum_of_probs)

        return (p_win, p_loss, p_draw)

    # this method takes the game_board and analyzes the last move against the vector_states
    # and sets 'D', 'X' or 'O' as required - this keeps a running tally of the game state
    # no result is returned
    def set_vector_states(self, game_board):

        # get the identity of the player of the last move
        player = self.this_player(game_board)
        #print("set_vector_states: player = ", player)
        if player == "O":
            opponent = "X"
            opponent_one_play = "x"
            one_play = "o"
        else:
            opponent = "O"
            opponent_one_play = "o"
            one_play = "x"

        # get the cell chosen in the last move
        last_play = game_board[-1]
        #print("set_vector_states: last_play = ", last_play)

        # iterate over the vector_states to set or reset the values
        for vector_state in range(len(self.vector_states)):
            # skip over any vector in the 'draw' state - skip over - nothing to do
            if self.vector_states[vector_state] != "D":
                # find the win_vectors containing the last move so far
                # note that the same cell can occur in up to 4 win_vectors...
                if last_play in self.win_vectors[vector_state]:
                    # if this vector_state has not yet been assigned a value
                    if self.vector_states[vector_state] is None:
                        # assign the value of the current player
                        self.vector_states[vector_state] = one_play
                    # if this vector_state already contains a move from the player
                    # assign "X" or "O" to indicate impending win
                    elif self.vector_states[vector_state] == one_play:
                        self.vector_states[vector_state] = player
                    # if the vector_state contains at least one move of the opponent
                    elif self.vector_states[vector_state] == opponent or self.vector_states[vector_state] == opponent_one_play:
                        # assign a draw as there are now both players in cells in that vector
                        self.vector_states[vector_state] = "D"

    """
    # calculate the win probability for a given board state
    # note that we are actually calculating the vector_states that are
    # set to 'D' or the opponent, since those are 'lost causes'
    # P(won't win) = sum(lost causes) / 8
    # EXCEPT:
    #   IF there is a winning move for the opponent P(win)= 0
    #   OR the opponent is in a FORK P(win) = 1
    def calc_p_win(self, game_board):

        p_win = 0
        possible_win_vectors = 8
        impending_loss = False
        pending_win_vectors = 0

        player = self.this_player(game_board)

        # existence of bad_state_set values in vector_state eliminates
        # that vector as a win candidate
        if player == "O":
            # note that "X" means 2 cells occupied by X; "x" means 1 cell
            bad_state_set = {"D", "X", "x", None}
            opponent = "X"
        else:
            # note that "O" means 2 cells occupied by O; "o" means 1 cell
            bad_state_set = {"D", "O", "o", None}
            opponent = "O"

        for vector_state in range(len(self.vector_states)):
            # if the vector is a lost cause, reduce the win_vectors by 1
            if self.vector_states[vector_state] in bad_state_set:
                possible_win_vectors -= 1

            # if the vector has 2 opponent plays and 1 open cell
            # player is about to lose
            if self.vector_states[vector_state] == opponent:
                impending_loss = True

            # count the vectors that player has 2 plays and 1 open cell
            if self.vector_states[vector_state] == player:
                win_vectors += 1

        print("calc_p_win: agent {} - poss_win_vectors = {}, imp_loss = {}, win_vectors = {}".format(
            player, possible_win_vectors, impending_loss, win_vectors))

        # if next move produces an opponent win, or if all the vectors are "D" or opponent
        if impending_loss or possible_win_vectors == 0:
            # player can't win
            p_win = 0

        # if the player has created a fork (wins on > 1 vectors) opponent can't block
        if win_vectors > 0:
            p_win = 1

        # no impending wins, losses or draws
        if not impending_loss and possible_win_vectors > 0:
            p_win = possible_win_vectors / 8

        return p_win

################################################ might not need this ######################################
    # calculate the loss probability for a given board state
    def calc_p_loss(self, game_board):

        p_loss = 0
        no_win_vectors = 0
        impending_loss_vectors = 0

        player = self.this_player(game_board)

        if player == "X":
            bad_state_set = {"D", "o", None}
            loss_vector = "O"
        else:
            bad_state_set = {"D", "x", None}
            loss_vector = "X"

        for vector_state in range(len(self.vector_states)):
            if self.vector_states[vector_state] in bad_state_set:
                no_win_vectors += 1
            elif self.vector_states[vector_state] == loss_vector:
                impending_loss_vectors += 1

        if impending_loss_vectors > 1:
            p_loss = 1
        else:
            p_loss = no_win_vectors / 8

        return p_loss

    # calculate the draw probability for a given board state
    def calc_p_draw(self, game_board):

        draw_vectors = 0
        #moves_made = len(game_board)
        #moves_left = 9 - moves_made
        draw_state_set = {"D", None}

        for vector_state in range(len(self.vector_states)):
            if self.vector_states[vector_state] in draw_state_set:
                draw_vectors += 1

        p_draw = draw_vectors / 8

        return p_draw
    """
    # this method resets the vector states for a new game
    # this eliminates the need to reinstantiate an object for a new game
    # no result is returned
    def reset_vector_states(self):

        # initialize 8 win vector variable states

        self.left_file = None
        self.center_file = None
        self.right_file = None
        self.bottom_rank = None
        self.middle_rank = None
        self.top_rank = None
        self.left_diagonal = None
        self.right_diagonal = None

        print("reset_vector_states: reset")

    # determine which player made the last move
    def this_player(self, this_game):

        moves_made = len(this_game)

        if moves_made % 2 == 0:
            return "O"
        else:
            return "X"
