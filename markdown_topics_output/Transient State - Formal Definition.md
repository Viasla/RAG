# Formal Definition
In a Markov chain, a state s_i is called transient if it is not absorbing; equivalently, the probability of ever returning to s_i after leaving it is strictly less than 1. Formally, letting f_{ii}=\sum_{n=1}^{\infty}P\{X_n=i\mid X_0=i\} be the total return probability, s_i is transient when f_{ii}<1. In the special context of an absorbing Markov chain, every non‑absorbing state is classified as transient.

A state i of a finite Markov chain is transient if the probability of ever returning to i after leaving it is strictly less than one; equivalently the expected number of visits to i, starting from i, is finite. In the canonical form of an absorbing chain the transient states are listed before the absorbing states and the sub‑matrix Q contains the transition probabilities among the transient states.

