# Formal Definition
For a Markov chain with a finite state space $S=\{s_1,\dots,s_r\}$, the transition matrix $\mathbf P$ is the $r\times r$ array whose $(i,j)$‑entry $p_{ij}$ equals $\Pr\{\text{next state}=s_j\mid\text{current state}=s_i\}$; the entries satisfy $0\le p_{ij}\le1$ and $\sum_{j=1}^r p_{ij}=1$ for each $i$. The $n$‑step transition probabilities are given by $(\mathbf P^n)_{ij}=p^{(n)}_{ij}=\sum_{k=1}^r p_{ik}p^{(n-1)}_{kj}$, and in particular $p^{(2)}_{ij}=\sum_{k=1}^r p_{ik}p_{kj}$.

