# a function to calculate the optimum (maximum and minimum) probabilities
# written by Russell on 7/8
# work in progress

# the param for minimax is a list of tuples
# each tuple contains 3 probabilities, each adding up to 1
# probs[n] = (p1, p2, p3); p1 = probabity of winning; 
# p2 = probability of losing; p3 = probability of drawing
def minimax(probs):

    choice = probs.sort( lambda x: selector)
    
    probs = [
        (0.6, 0.3, 0.1),
        (0.45, 0.35, 0.2),
        (0.25, 0.55, 0.2),
        (),
        (),
        ()
    ]

    """
    w > l > d = w
    w > d > l = w

    l > w > d = w
    l > d > w = d
    
    d > w > l = w
    d > l > w = d

    w > (l + d) = w
    
    l > (w + d) = d
    
    d > (w + l) = d


    


    for prob in probs:
        p_win = prob[0]
        p_lose = prob[1]
        p_draw = prob[2]
    
    
    """

    if p_win > (p_lose + p_draw):
        return p_win


    elif p_win < p_lose:
        resort on p_draw


    elif p_draw > (p_win + p_lose): 
        resort on p_draw
