# Properties
Each row of the transition matrix \mathbf{P} consists of non‑negative numbers that sum to 1, reflecting that from any current state the chain must move to some (possibly the same) state in the next step.

The n‑step transition probabilities satisfy the Chapman‑Kolmogorov relation p_{ij}^{(n+m)} = \sum_{k=1}^r p_{ik}^{(n)} p_{kj}^{(m)}, which for n=m=1 reduces to p_{ij}^{(2)} = \sum_{k=1}^r p_{ik} p_{kj}.

Theorem 11.1 states that the (i,j) entry of \mathbf{P}^n equals p_{ij}^{(n)}, linking matrix powers to multi‑step transition probabilities.

For a regular Markov chain (e.g., the Oz weather chain), the powers \mathbf{P}^n converge to a matrix whose rows are identical, giving a limiting distribution independent of the starting state.

The transition probabilities are time‑homogeneous in the presented chains: the same matrix \mathbf{P} applies at every step.

