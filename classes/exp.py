# work in progress

cell_probs = [0, 0, 0, 0, 0, 0, 0, 0, 0]

empty = get_open_cells(board)

win_vectors = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (6, 3, 0),
               (7, 4, 1), (8, 5, 2), (6, 4, 2), (8, 4, 0))

# each corner affects 3 vectors: 3 / 24 = 1 / 8 = 0.125...
corner_val = 0.125
# each edge affects 2 vectors: 2 / 24 = 1 / 12 = 0.083333...
edge_val = 1 / 12
# the center affects 4 vectors: 4 / 24 = 1 / 6 = 0.166666...
center_val = 1 / 6

# a list of cell weights for cells 0 - 8
cell_weights = [corner_val, edge_val, corner_val,
                edge_val, center_val, edge_val,
                corner_val, edge_val, corner_val]
