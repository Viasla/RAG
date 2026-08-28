# Properties
For an ergodic chain, r_i = 1 / w_i, where w_i is the i‑th component of the stationary distribution vector w; consequently all r_i are finite and positive.

The stationary probabilities w_i are strictly positive (Corollary 11.1), ensuring that each r_i is well defined.

The mean recurrence time can be expressed in terms of the mean first passage times: r_i = \sum_k p_{ik}(m_{ki}+1) = 1 + \sum_k p_{ik} m_{ki}.

In matrix form, letting M be the mean first passage matrix (with zero diagonal) and C the all‑ones matrix, the relation (I - P)M = C - D holds, linking the transition matrix P, the mean first passage matrix M, and the mean recurrence matrix D.

Because the chain is ergodic, the return to the starting state occurs with probability one, guaranteeing that r_i exists for every state.

For any ergodic Markov chain, the mean recurrence time satisfies m_{ii}=z_{ii}/w_i.  The average mean recurrence time over all states weighted by the stationary distribution is Kemeny’s constant: κ=sum_j m_{ij} w_j=sum_j z_{jj}-1, which is independent of the starting state i.  In an ergodic chain that is also reversible, the mean first passage time from i to j equals that from j to i when weighted by stationary probabilities, but the mean recurrence time m_{ii} remains 1/w_i.

