# Examples
The stepping‑stone model illustrated in Figures 11.1 and 11.2 is described as an absorbing Markov chain; the theorem guarantees that with probability 1 the stones will eventually all be the same colour, i.e., the chain is absorbed.

Example 11.13 (Drunkard’s Walk): A man walks on a four‑block street with corners 0–4; corners 0 (home) and 4 (bar) are absorbing states because once reached the man stays there. Corners 1, 2, 3 are transient.

In the first numerical example the matrix R contains the rows \[1/2\;0\] for state 1 and \[0\;1/2\] for state 3, indicating that states 0 and 4 are absorbing; the first row of the resulting B matrix shows that starting from state 1 the chain is absorbed in state 0 with probability 3/4 and in state 4 with probability 1/4.\nExercise 9 explicitly declares state 5 to be an absorbing state in a process that moves only to larger integers.\nExercise 6 modifies the Land of Oz chain by making the state R absorbing, replacing the original transition probabilities with a row that has a 1 in the R‑column and zeros elsewhere.\nExercise 7 asks the reader to make states 0 and 4 absorbing in Example 11.8 and then compute the fundamental matrix and absorption probabilities.

time to absorption, 419

