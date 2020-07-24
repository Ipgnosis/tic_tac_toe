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
  
These results are the average of 3 runs of 1m games each.  This establishes the approximate baseline probability for each of the 3 outcomes.

The metric for success is that, after training, the 'Nought' agent ('O'), must consistently exceed the random win rate (~28.9%) against a human player playing as Agent 'X'.
