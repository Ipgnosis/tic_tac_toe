# tic_tac_toe
This is a work in progress.

## Goal: 

To explore how a software process can learn how to resolve a problem space from first principles. This was inspired by [Google's AlphaZero](https://deepmind.com/blog/article/alphazero-shedding-new-light-grand-games-chess-shogi-and-go).  However, AlphaZero's learning process is opaque, and this doesn't expand **my** knowlege of how software can learn the problem space.  This project iterates towards a process by which a human * *(specifically me)* * can understand the computer learning process.

### Sidebar:

Humans don't learn games such as Tic Tac Toe, Chess or Go/Paduk/Weiqi by doing any of the following:
1.  Exhaustively studying all the great games played by past masters
2.  Exhaustively studying rules, strategies or tactics

What they actually do is learn enough to start playing the first game, then playing and learning as they go along.  During early game play, humans do not:

1.  Start a game with a proven strategy in mind (e.g. Sicilian Defense, Ruy Lopez, etc.)
2.  Conduct an exhaustive, breadth first search of all possible moves (note even in Tic Tac Toe, there are 9! or 362,880 possible moves)
3.  Calculate win/loss probabilities for any given move
4.  Explore the history of great games played in the past, looking for similarities
  
The goal of this project is to get the computer to learn Tic Tac Toe as a young human learns: starting with just enough information to play and then learn by experience of play; basing their decisions on their memory of what worked or didn't work in the past.


## Approach: 

The game 'tic tac toe' is used as an experiment to explore machine learning from a human perspective.  Although computer TTT has been implemented many times before, it was chosen because the action space is small enough to be readily understandable at first glance and the necessary compute resources can be provided by a laptop.

The process must self-learn via competing against itself.  No human interaction or pre-programmed rules (beyond how to make a move and the definition of win/loss) are permissable.

By convention:
- Agent 'X' always makes the first move
- Agent 'O' always makes the second move

If you set the program to play itself in 'random mode' (i.e. both agents will randomly select the next move from the available cells) then the results are as follows:
- Win - Agent 'X':              58.4485%
- Win - Agent 'O':              28.8464%
- Draw - 9 moves, no winner:    12.0751%
  
These results are the average of 3 runs of 1 million games each.  This establishes the approximate baseline probability for each of the 3 outcomes.  The higher probability of Agent X winning is a result of the first-mover advantage which also results in Agent X potentially having 5 moves (cf. only 4 for Agent O) in a game that is not won before move 9.


## Success metric:

The metric for success is that, after training, the win rate of the trained agent exceeds:
1.  The success rate of random play (see below)
2.  The win rate of a reasonably adept human (i.e. consistenty beat a human)

For example, the 'Nought' agent ('O'), should consistently exceed the random win rate (~28.9%) against a human player playing as Agent 'X'.


## Current Status:

The game loop (multi_game_loop.py) executes a series of games defined by a game limit variable.

The game loop can be run in 3 different modes for each of the 2 agents (X/O):
- Random - the agent randomly selects a move from the available spaces (see also 'Error avoidance' below)
- Best - the agent selects the best move from available choices based on an algorithm (see also 'Best move algorithm' below)
- Human - the agent delegates the play selection to a human interlocutor.

When training the agents, running both agents in Best mode means they tend to fixate on a small number of game states, rather than exploring the larger action space.  So it is (currently) better to run in Best-Random mode: which forces the Best agent to have to react to the full range of plays from the Random agent.  However, this creates a problem because one agent gets trained and then when you flip the modes, the other agent is dominated by the first and can't find a way to win.  Therefore enabling 'flip_mode' allows the agents to alternate between Best and Random and thereby gain experience and explore the action space in parallel.

After each move made by the agent, probabilities of win/lose/draw are calculated for the game state as it exists at the completion of that move.

Each game record is saved in a game history file (see 'game history' below), assuming that the game is unique, i.e. is not a duplicate of a game that has been played before.  Note that 'uniqueness' is evaluated against a transposition algorithm that considers all rotations and reflections of a given game state (see also 'Transposition' below).  The game data stored is:
- Result - x win, o win, draw
- Game - a list of the moves made
- Probs - a list of the outcome probabilities for each corresponding move from the perspective of the agent (X/O) that made the move (P(win), P(loss), P(draw))

If the game doesn't require human intervention, there is the option to report progress on the game loop run to the terminal along with an estimate of time remaining in the game loop.  This is currently set to every 10% of the game loop, but that is a variable.

At the end of the game loop execution, the following data is output to the terminal:
- Score data (X wins, O wins, Draws)
- Execution time data
- A matplotlib graph of the game tally throughout the run


## Game History:

The game history is handled by the TTTBase class.  Each game record (see above) is stored with a unique index in a dictionary which effectively provides an indexed file, searchable on the game moves.  The game history file is read into memory at the start of the game loop and written (along with new unique games that have been discovered during the loop) to file at the end of the game loop.


## Best Move Algorithm:

Per above on the goal of the project to mimic human learning, therefore the algorithm is as follows:

1.  Assess the board for potential wins (two moves in a vector with an open space): if one exists, make that play to take the win.
2.  Assess the board for impending losses (two opponent's moves in a vector with an open space): if one exists, take it to prevent the loss.
3.  Assess the board for recognizable patterns, based on memory of past games.  Optimize move selection as follows:
    -   Choose the move most likely to win.  If there are several moves with equal weight, choose the move least likely to lose.
    -   If losing seems more likely, chose the move most likely to draw.
4.  Record the expectation of a win / loss / draw for that move by estimating the probability of each.
5.  At the end of the game, store the recollection of that game.
6.  For each of the outcomes (win/loss/draw) adjust the probabilities (expectation) of those results for all relevant stored games.  This is done for the each of the patterns followed, up to the point that the game deviated from the pattern.  The degree of upgrade/downgrade is a variable that will be tuned to produce an optimal result.


## Ultimate goal:

Implement the concept of 'hindsight experience replay' which allows the software to learn by storing and updating its base of experience based on new experience.  This (IMHO) seems to match the human process of learning and is more sophisticated than merely having a search tree (the traditional approach) or a database of optimal moves (calculated algoritmically) for every game state.  This would be one approach to achieving the ultimate goal.  The other, of course, is neural networks.  That may be tackled later.

## Current status: 

Error avoidance: the vector states are searched for a win that can be achieved in the current move or a loss that could be achieved in the next (opponent) move.  If a win can be achieved, or a loss can be blocked, that move is selected.  !!! This is a kluge that will be removed later. !!! Prior to the probability calculation code being created, the game history was filled with games containing randomly selected moves that missed easy wins or imminent losses.  This filled the training data with poor choices that were being repeated over and over.  When probability is integrated into 'best move' the game history will (hopefully) avoid storing poor training data.  See more about probability below.

For a given game state, the game history is searched for matching games (see also 'Transposition' below).  If no matches are found, the next move is random: this is to ensure that the algorithm explores the solution space (i.e. tries everything that hasn't been tried, such that new moves can be explored).  If matches are found, then the most common next move is selected.  The rationale for 'most common' being selected is that this is the move which improves the chance of winning.  However, per above, the combination of questionable game data and the lack of a probabilities function means that this algorithm is weak and often results in the same poor move being made over and over again (thus the error avoidance kluge).

Next steps = integrate the probability calculation method (TTTProbs class) to allow the best next move (rather than the most common move) to be selected.  Once the probabilities have been integrated, training will tune the probabilities to upgrade/downgrade the base probability estimates based on training outcomes.  This will (hopefully) result in optimal performance once training is complete.


## Calculating probability:

In the original problem statement it was asserted that humans do not play, or improve their play, by a brute-force search of all remaining move options and a methodical calculation of the sucess probability of a given move.  What humans actually do is scan the current situation, and make an almost subconscious assessment of risk/reward before selecting the next move most likely to win; if winning is less likely, then they are playing for a draw.  This has been confirmed by Garry Kasparov's book: 'Deep Thinking: Where Machine Intelligence Ends and Human Creativity Begins'. The TTTProbs class was written to attempt to mimic this thought process and does not implement a tree search.
 [] Say more on this.


## Transposition:

In order to minimize the game history search space, an algorithm ensures that any game stored is unique.  Note that the following games are not unique:

(Note that this 'ascii art' is not rendering well in the browser, but can be seen clearly in VS Code/IDE of choice)


 X |   | O       
-----------      
   | X | O        
-----------       
   |   | X        



   |   | X
-----------
   | X |  
-----------
 X | O | O


The transpositions are as follows:

- Rotate 90 degrees right (see above)
- Rotate 180 degrees
- Rotate 270 degrees right (90 degrees left)
- Reflect vertical (flip on the horizonal axis)
- Reflect horizonal (flip on the vertial axis)
- Reflect diagonal left to right (flip on the diagonal axis, top left corner to bottom right corner)
- Reflect diagonal right to left (flip on the diagonal axis, top right corner to bottom left corner) 
