# tic_tac_toe
This is a work in progress.

Goal: 

To figure out how a software process can learn how to resolve a problem space from first principles. This was inspired by Google's AlphaZero.  However, AlphaZero's decision making appears be opaque, and this (IMHO) doesn't expand our knowlege of the problem space.  This project has to produce a process by which a human can understand the learning and decision process.

Approach: 

The game 'tic tac toe' is used as an experiment.  Although this has been done many times before, it was chosen because the action space is small enough to be readily understandable at first glance and the necessary compute resources can be provided by a laptop.

The process must self-learn via competing against itself.  No human interaction or pre-programmed rules (ideally) are permissable.

By convention:
- Agent 'X' always makes the first move
- Agent 'O' always makes the second move

If you set the program to play itself in 'random mode' (i.e. both agents will randomly select the next move from the available cells) then the results are as follows:
- Win - Agent 'X':  58.4485%
- Win - Agent 'O':  28.8464%
- Draw:             12.0751%
  
These results are the average of 3 runs of 1m games each.  This establishes the approximate baseline probability for each of the 3 outcomes.  The higher probability of Agent X winning is a result of the first-mover advantage which also results in Agent X potentially having 5 moves (cf. only 4 for Agent O) in a game that is not won before move 9.

Success metric:

The metric for success is that, after training, the 'Nought' agent ('O'), must consistently exceed the random win rate (~28.9%) against a human player playing as Agent 'X'.

Current Status:

The game loop (multi_game_loop.py) executes a series of games defined by a game limit variable.

The game loop can be run in 3 different modes for each of the 2 agents (X/O):
- Random - the agent randomly selects a move from the available spaces (see also 'Error avoidance' below)
- Best - the agent selects the best move from available choices based on an algorithm (see also 'Best move algorithm' below)
- Human - the agent delegates the play selection to a human interlocutor.

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

Game History:

The game history is handled by the TTTBase class.  Each game record (see above) is stored with a unique index in a dictionary which effectively provides an indexed file, searchable on the game moves.  The game history file is read into memory at the start of the game loop and written (along with new unique games that have been discovered during the loop) to file at the end of the game loop.

Best Move Algorithm:

This is a work in progress.

Ultimate goal:

Implement the concept of 'hindsight experience replay' which allows the software to learn by storing and updating its base of experience based on new experience.  This (IMHO) seems to match the human process of learning and is more sophisticated than merely having a database of optimal moves (calculated algoritmically) for every game state.  This would be one approach to achieving the ultimate goal.  The other, of course, is neural networks.  That may be tackled later.

Current status = 
Error avoidance: the vector states are searched for a win that can be achieved in the current move or a loss that could be achieved in the next (opponent) move.  If a win can be achieved, or a loss can be blocked, that move is selected.  !!! This is a kluge that will be removed later. !!! Prior to the calc_probs class being created, the game history was filled with games containing randomly selected moves that missed easy wins or imminent losses.  This filled the training data with poor choices that were being repeated over and over.  When calc_probs is integratedd into 'best move' the game history will be recreated to remove this poor training data.
The game history is then searched for matching games (see also 'Transposition' below).  If no matches are found, the next move is random: this is to ensure that the algorithm explores the solution space (i.e. tries everything that hasn't been tried, such that the game history can be expanded to try new moves).  If matches are found, then the most common next move is selected.  The rationale being that this is the move which maximizes the probability of winning.  However, per above, the combination of the questionable game data and the lack of a probabilities function means that this algorithm is weak and often results in the same poor move being made over and over again.

Next steps = integrate the calc_probs method (TTTProbs class) to allow the best next move (rather than the most common move) to be selected.  Once the probabilities have been integrated, more training will be run to tune the probabilities to upgrade/downgrade the base probability estimates based on training outcomes.

Transposition:

In order to minimize the game history search space, an algorithm ensures that any game stored is unique.  Note that the following games are not unique:

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
