# Properties
The transition matrix is stochastic: every row sums to 1 and all entries are non‑negative.

The $n$‑step transition probabilities are obtained by matrix powers: $(\mathbf P^n)_{ij}=p^{(n)}_{ij}=\sum_{k=1}^r p_{ik}p^{(n-1)}_{kj}$.

Theorem 11.1 states that the $(i,j)$ entry of $\mathbf P^n$ gives the probability of being in state $s_j$ after $n$ steps when starting from $s_i$.

If the chain is regular (some power of $\mathbf P$ has all positive entries), the rows of $\mathbf P^n$ converge to the same limiting probability vector, making long‑range predictions independent of the starting state.

