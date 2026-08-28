# Interpretation
The matrix $B$ provides, for every transient state, the probabilities of eventual absorption in each absorbing state.  Its rows sum to one because in an absorbing Markov chain every trajectory starting from a transient state is guaranteed to be absorbed eventually (Theorem 11.3).  Thus $B$ encapsulates the long‑run behaviour of the chain: given a starting point in the transient region, $B$ tells exactly which absorbing state will be reached and with what probability.

