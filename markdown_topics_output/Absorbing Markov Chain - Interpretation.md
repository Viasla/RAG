# Interpretation
Absorbing Markov Chains are discussed in section 11.2 of chapter 11 Markov Chains in Grinstead and Snell's 'Introduction to Probability'.

An absorbing Markov chain models situations where the system eventually settles into a permanent state, such as fixation of a single color in the stepping‑stone model or a drunkard eventually reaching home or a bar. The probability that a particular absorbing state is reached depends on the initial configuration and can be computed from the matrices $R$ and $Q$.

Each entry B_{ij} gives the probability that, starting from transient state i, the chain will be absorbed in absorbing state j.

The first row of B in the drunkard’s walk example states that starting from state 1 the probability of absorption in state 0 is 3/4 and in state 4 is 1/4.

The vector t (or the diagonal of N when multiplied by c) gives the expected number of steps before absorption from each transient state.

The program “Absorbing Chain” automates the computation of Q,R,N,t and B for any given absorbing chain matrix.

The entry b_{ik} of matrix B gives the probability that a chain starting in transient state i will be absorbed in absorbing state k.

The expected time to absorption from transient state i is the sum of the i‑th row of the fundamental matrix N.

The absorbing Markov chain model is interpreted as a casino game: each gambler contributes $1 (the casino’s intake T^B) and only those who arrive during the occurrence of the target pattern B receive a payout equal to BB. Because the bets are fair, the expected intake equals the expected payout, which is precisely the expected time to absorption of the underlying Markov chain.

In the Penney‑ante game, the absorbing states correspond to the first occurrence of pattern A or pattern B; the probabilities p_A and p_B of absorption in each state determine the odds of winning for the first player.

In the context of the index, 'absorbing state' (page 416) refers to a state that, once entered, cannot be left, which is a key feature of an absorbing Markov chain.

