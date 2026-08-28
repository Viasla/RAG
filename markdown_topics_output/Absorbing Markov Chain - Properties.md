# Properties
Every absorbing Markov chain has at least one absorbing state and every state can reach an absorbing state (reachability).

Transient states are those that are not absorbing; they are visited only finitely many times with probability 1.

The canonical form separates absorbing and transient states, allowing explicit formulas for (a) absorption probabilities, (b) expected time to absorption, and (c) expected number of visits to each transient state.

If the chain starts in a transient state, the probability that it will eventually be absorbed equals 1 (the chain is absorbing in the probabilistic sense).

The matrix $(I_t-Q)^{-1}$, called the fundamental matrix, yields the expected number of times the process visits each transient state before absorption and can be used to compute the quantities listed above.

The fundamental matrix satisfies N = (I-Q)^{-1}.

Absorption probabilities satisfy B = N R.

Expected times to absorption satisfy t = Nc.

If the chain has m transient states, N is an m\times m matrix whose i,j entry equals the expected number of visits to transient state j when starting from transient state i.

The rows of B sum to 1, reflecting that absorption must occur in some absorbing state.

The probability of absorption in a particular absorbing state equals the proportion of the corresponding type in the initial state (gene example).

For a simple symmetric random walk on {0,…,n} starting at x the expected time to absorption is x(n−x).

In a fair gambler’s ruin (p=q=½) the probability of reaching the upper absorbing state T from x is x/T; for biased odds p≠q the formula w_x=((q/p)^x−1)/((q/p)^T−1) holds.

Harmonic functions satisfy f=P f; for absorbing chains this implies f=P^∞ f, showing that the expected fortune remains unchanged up to absorption (martingale property).

For any pattern B, the expected time to reach B for the first time equals the total payout BB, i.e., E(T^B)=BB; this is the expected absorption time of the associated Markov chain started from the empty state.

When starting from a pattern A that is not a subpattern of B, the expected additional time to reach B is BB−AB, reflecting the difference between the payout at absorption and the amount already earned while A was present.

If f(i) is harmonic on the transient states of an absorbing chain, then f(i) equals the probability of absorption in a particular absorbing state when starting from i; this links harmonic functions to absorption probabilities (Exercise 31).

For the random walk with absorbing endpoints, the harmonic functions f(i)=i (when p=q) and f(i)=(q/p)^i (when p≠q) yield explicit formulas for absorption probabilities b_{iN} as i/N or ((q/p)^i−1)/((q/p)^N−1).

The matrix relation B = N R follows from the first‑step analysis b_{ij}=p_{ij}+∑_k p_{ik}b_{kj} for transient states, providing a compact way to compute absorption probabilities (Exercise 34).

The expected absorption time can be expressed as the sum of tail probabilities: E(T)=∑_{n≥0}P(T>n); applying this to pattern HTH gives E(T)=10, confirming the BB calculation (Exercise 30).

An absorbing Markov chain contains at least one absorbing state (page 416).

Absorption probabilities, mentioned on page 420, quantify the likelihood of eventual absorption in each absorbing state.

