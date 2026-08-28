# Formal Definition
A sequence of random variables \(S_1,S_2,\dots,S_n\) is called a martingale with respect to the natural filtration if for every \(k\ge 2\) \[E\bigl(S_k\mid S_{k-1}=a_{k-1},\dots,S_1=a_1\bigr)=a_{k-1}.\] In words, the conditional expectation of the next fortune given the entire past equals the current fortune.

A martingale is a stochastic process for which, at each step, the conditional expectation of the next value given the entire past history equals the current value; in the text this is illustrated by the fact that, after each play, the expected sum of the nominal values of player A's counters equals his current sum, and similarly for player B.

In de Moivre's construction, the new counter values are chosen so that the player's expected fortune after a game equals his fortune before the game, thereby satisfying the martingale property.

