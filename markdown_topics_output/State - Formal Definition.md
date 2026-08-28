# Formal Definition
A Markov chain is defined by a finite set of states $S=\{s_1,s_2,\dots,s_r\}$.

At each discrete time step the chain occupies exactly one state $s_i\in S$.

If the chain is in state $s_i$ at time $t$, it moves to state $s_j$ at time $t+1$ with probability $p_{ij}$, where the collection $\{p_{ij}\}$ forms the transition matrix $P$.

The probabilities satisfy $p_{ij}\ge0$ for all $i,j$ and $\sum_{j=1}^r p_{ij}=1$ for each $i$ (the rows of $P$ are probability distributions).

An initial probability distribution (a probability vector) on $S$ specifies the starting state.

