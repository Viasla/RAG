# Intuition
The waiting time until a specific sequence of outcomes appears in a stochastic experiment can be interpreted as the absorption time in a Markov chain whose states record the current longest suffix of the observed sequence that matches a prefix of the target pattern.  When the chain reaches a state representing the full pattern, the process is absorbed.  This perspective turns the problem of computing expected waiting times into a linear‐algebra problem involving the fundamental matrix of an absorbing Markov chain.

In the case of a run of k identical outcomes, the state is simply the current run length; the chain has absorbing state k.  The expected time to absorption from state 1 is the expected number of trials needed to obtain k consecutive successes.  The linear equations for the expectations reduce to a simple recurrence that yields the closed form (m^k−1)/(m−1).

