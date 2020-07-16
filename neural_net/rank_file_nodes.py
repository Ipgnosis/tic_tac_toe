# the neural nodes for the ranks, files and diagonals
# written by Russell on 5/9/20
# rewritten on 5/15 to convert to class

# input = 3 cell objects making up the rank, file, diagonal; plus the node_name

# returns:
# prob(x_wins)
# prob(o_wins)
# prob(draw)

# instantiated for:
# left_file
# middle_file
# right_file
# bottom_rank
# center_rank
# top_rank
# left_diagonal
# right_diagonal

# the neural_node for a rank, file or diagonal
class Win_triplet():

    node_weight = 1
    # node_bias = 1 # not going to use this for now, but may need it later

    print_node_results = False  # we can change this for all nodes for debugging

    def __init__(self, node_1, node_2, node_3, node_fgs, node_name):

        self.f1 = node_1
        self.f2 = node_2
        self.f3 = node_3
        self.fgs = node_fgs
        self.node_name = node_name
        # self.rank_file_type = rank_file_type # might need this later: options = 'rank', 'file', 'diagonal'

    def calc_prob(self, p1, p2, p3):
        # this needs more work

        next_up = self.fgs.next_up()
        avg = (p1 + p2 + p3) / 3

        return avg

    def p_x_wins(self):
        # get the P(x_wins) inputs from the cell nodes
        px1 = self.f1.p_x_wins()
        px2 = self.f2.p_x_wins()
        px3 = self.f3.p_x_wins()

        pxw = self.calc_prob(px1, px2, px3)

        if self.print_node_results:
            print("Node", self.node_name, ":", pxw * self.node_weight)

        return pxw * self.node_weight

    def p_o_wins(self):
        # get the P(o_wins) inputs from the cell nodes
        po1 = self.f1.p_o_wins()
        po2 = self.f2.p_o_wins()
        po3 = self.f3.p_o_wins()

        pow = self.calc_prob(po1, po2, po3)

        if self.print_node_results:
            print("Node", self.node_name, ":", pow * self.node_weight)

        return pow * self.node_weight

    def p_draw(self):
        # get the P(draw) inputs from the cell nodes
        pd1 = self.f1.p_draw()
        pd2 = self.f2.p_draw()
        pd3 = self.f3.p_draw()

        pd = self.calc_prob(pd1, pd2, pd3)

        if self.print_node_results:
            print("Node", self.node_name, ":", pd * self.node_weight)

        return pd * self.node_weight
