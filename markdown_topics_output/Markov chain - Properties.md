# Properties
Each row of the transition matrix $P$ consists of non‑negative numbers that sum to 1, reflecting that the chain must move to some state at the next step. The $n$‑step probabilities satisfy $p^{(n)}_{ij}=\sum_{k=1}^r p_{ik}p^{(n-1)}_{kj}$, which is exactly the $(i,j)$ entry of $P^n$; this is the content of Theorem 11.1. The two‑step formula $p^{(2)}_{ij}=\sum_k p_{ik}p_{kj}$ can be seen as a dot product of the $i$th row of $P$ with the $j$th column of $P$. A Markov chain is called regular if some power $P^m$ has all positive entries; regular chains have a unique stationary distribution that is approached regardless of the initial state, as illustrated by the Land of Oz example.

For any absorbing Markov chain, the vector of absorption probabilities satisfies β = NR where N=(I‑Q)^{-1} and R contains the transition probabilities from transient to absorbing states (Exercise 34).

If a function f is harmonic (f(i)=∑_j p_{ij}f(j)) on transient states, then its value at an absorbing state equals the expected value of f at the time of absorption; this yields the proportion‑of‑genes result in Exercise 31.

When p=q in the gambler’s‑ruin walk, the linear function f(i)=i is harmonic, giving absorption probability b_{iN}=i/N; when p≠q, the exponential function f(i)=(q/p)^i is harmonic, giving b_{iN}=((q/p)^i‑1)/((q/p)^N‑1).

The sum of tail probabilities equals the expectation: E(T)=∑_{n≥0}P(T>n); applying this to the pattern‑avoidance recurrence yields E(T)=10 for HTH (Exercise 30).

Fundamental Limit Theorem for Regular Markov Chains is cited on page 448.

The fundamental matrix associated with a Markov chain is mentioned on page 419.

Mean first passage matrix is noted on page 455.

Mean first passage time is noted on page 453.

Mean recurrence matrix is noted on page 455.

Mean recurrence time is noted on page 454.

Central Limit Theorem for Markov Chains is referenced on page 464.

For an ergodic Markov chain see page 458.

