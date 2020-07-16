# the neural nodes for the individual cells
# written by Russell on 5/9/20
# modified on 5/10/20 to align board data structure with rest of project
# rewritten on 5/15/20 to convert to class

# sets:
# move = 'X' - P(x_wins) = 1 * weight; else 0
# move = 'O' - P(o_wins) = 1 * weight; else 0
# move = empty - P(draw) = 1 * weight; else 0

# class definition for a board cell node
class Board_cell():

    cell_weight = 1  # this will get set later when we start training
    # cell_bias = 1 # not going to use this for now, but may need it later
    move = ''  # this is set to empty by default, but gets set in a later move to either "X" or "O"
    # move_num = int # not going to use this for now, but may need it later
    print_cell_results = False  # we can change this for all cells for debugging

    def __init__(self, position, name):
        self.position = position
        self.node_name = name
        # self.cell_type = cell_type # not sure if this is needed: options = 'corner', 'edge', 'center'

    def cell_contains(self):
        return self.move

    def p_x_wins(self):
        if self.move == 'X':
            if self.print_cell_results:
                print("Cell", self.node_name, ":", 1 * self.cell_weight)
            return 1 * self.cell_weight
        else:
            if self.print_cell_results:
                print("Cell", self.node_name, ":", 0)
            return 0

    def p_o_wins(self):
        if self.move == 'O':
            if self.print_cell_results:
                print("Cell", self.node_name, ":", 1 * self.cell_weight)
            return 1 * self.cell_weight
        else:
            if self.print_cell_results:
                print("Cell", self.node_name, ":", 0)
            return 0

    def p_draw(self):
        if self.move == '':
            if self.print_cell_results:
                print("Cell", self.node_name, ":", 1 * self.cell_weight)
            return 1 * self.cell_weight
        else:
            if self.print_cell_results:
                print("Cell", self.node_name, ":", 0)
            return 0
