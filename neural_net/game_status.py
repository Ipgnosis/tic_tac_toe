# node to capture and communicate game status
# written by Russell on 5/18


class Game_state():

    node_weight = 1
    # node_bias = 1 # not going to use this for now, but may need it later
    list_of_moves = []

    def __init__(self, node_list):

        self.node_list = node_list

    def num_moves(self):

        moves = 0

        for i in range(len(self.node_list)):
            if self.node_list[i].cell_contains() != "":
                moves += 1
        
        return moves

    def moves_list(self):

        #if len(self.list_of_moves) < self.num_moves():
        for i in range(len(self.node_list)):
            if self.node_list[i].move != "" and self.node_list[i].position not in self.list_of_moves:
                self.list_of_moves.append(self.node_list[i].position)

        ret_val = self.list_of_moves        
        
        #print('list of moves: type =', type(self.list_of_moves))
        return ret_val

    def next_up(self):

        if self.num_moves() % 2 == 0 or self.num_moves() == 0:
            return "X"
        else:
            return "O"

    def game_prop_remaining(self):

        moves = self.num_moves()
        
        return 1 - moves / 9 
