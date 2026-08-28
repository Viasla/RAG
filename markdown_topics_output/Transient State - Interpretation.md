# Interpretation
A transient state represents a phase of the process that is temporary. While the chain may linger in a transient state for several steps, the long‑run behavior is dominated by the absorbing states. The presence of transient states guarantees that, starting from any transient state, the process will be absorbed with probability one in an absorbing Markov chain.

Each entry n_{ij} of the fundamental matrix \mathbf{N} counts how many times, on average, the chain will be in transient state j when it starts in transient state i, before it is absorbed.

The first row of \mathbf{B} (0\; 4) in the text tells us that a process beginning in transient state 1 is absorbed in state 0 with probability 3/4 and in state 4 with probability 1/4.

The vector \mathbf{t} = (3,4,3)^{T} (as stated in the opening sentence) gives the expected number of steps until absorption when the chain starts in states 1, 2, 3 respectively; these values are obtained as the row sums of \mathbf{N}.

