# tic_tac_toe
This is a work in progress.

The goal is to figure out how a software process can learn how to resolve a problem space from first principles.  This was inspired by Google's AlphaZero.

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

The metric for success is that, after training, the 'Nought' agent ('O'), must consistently exceed the random win rate (~28.9%) against a human player playing as Agent 'X'.

Current Status:

The game loop (multi_game_loop.py) executes a series of games defined by a game limit variable.

The game loop can be run in 3 different modes for each of the 2 agents (X/O):
- Random - the agent randomly selects a move from the available spaces (see also 'error avoidance' below)
- Best - the agent selects the best move from available choices based on an algorithm (see also 'best move algorithm' below)
- Human - the agent delegates the play selection to a human interlocutor.

After each move made by the agent, probabilities of win/lose/draw are calculated for the game state as it exists at the completion of that move.

Each game record is saved in a game history file, assuming that the game is unique, i.e. is not a duplicate of a game that has been played before.  Note that 'uniqueness' is evaluated against a transposition algorithm that considers all rotations and reflections of a given game state (see also 'transposition' below).  The game data stored is:
- Result - x win, o win, draw
- Game - a list of the moves made
- Probs - a list of the outcome probabilities for each corresponding move from the perspective of the agent (X/O) that made the move (P(win), P(loss), P(draw))

If the game doesn't require human intervention, there is the option to report progress on the game loop run to the terminal along with an estimate of time remaining in the game loop.  This is currently set to every 10% of the game loop, but that is a variable.

At the end of the game loop execution, the following data is output to the terminal:
- Score data (X wins, O wins, draws)
- Execution time data
- a matplotlib graph of the game tally throughout the run


