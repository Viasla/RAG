# Properties
An absorbing Markov chain must contain at least one absorbing state and every state must have a path to some absorbing state.

Transient states are those that are not absorbing; they are visited only finitely many times with probability 1 in an absorbing chain.

The transition matrix of an absorbing chain can be put into canonical form by ordering transient states first and absorbing states last, yielding a block matrix $\begin{bmatrix} Q & R \\ 0 & I \end{bmatrix}$ where $Q$ governs transitions among transient states and $I$ is the identity on absorbing states.

From any starting state, the probability of eventual absorption is 1 for finite absorbing chains (as implied by the theorem referenced in the stepping‑stone example).

For an absorbing Markov chain the matrix I‑Q is nonsingular, guaranteeing that the fundamental matrix N exists.\nThe absorption‑probability matrix B satisfies B=NR and its rows are stochastic (each row sums to 1).\nThe expected time to absorption t=N\mathbf{1} is finite for every transient state.\nIf a state is absorbing, its corresponding row in the transition matrix is a unit vector with a 1 in the diagonal position and zeros elsewhere.\nChanging a non‑absorbing state to absorbing (as in the Land of Oz and Example 11.8 exercises) replaces its row in P with the appropriate unit vector and modifies Q, R, N, B, and t accordingly.

transient, 416

transient state, 416

