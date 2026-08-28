# Properties
The mean first passage times satisfy the linear recursions
$$m_{ij}=p_{ij}+sum_{k
eq j}p_{ik}(m_{kj}+1)=1+sum_{k
eq i}p_{ik}m_{kj},\[4pt]$$
which is Equation (11.2).

In matrix form the mean first passage matrix $mathbf{M}$ obeys
$$mathbf{M}=\mathbf{P}\mathbf{M}+\mathbf{C}-\mathbf{D},\[4pt]$$
or equivalently
$$(\mathbf{I}-\mathbf{P})\mathbf{M}=\mathbf{C}-\mathbf{D},$$
where $\mathbf{C}$ is the all‑ones matrix and $\mathbf{D}$ is diagonal with $d_{ii}=r_i$ (the mean recurrence times).

The mean recurrence time $r_i$ for state $s_i$ is related to $m_{ij}$ by
$$r_i=1+\sum_{k}p_{ik}m_{ki},$$
which follows from conditioning on the first step (Equation (11.4)).

For an ergodic chain the mean recurrence time satisfies $r_i=1/w_i$, where $w_i$ is the $i$th component of the stationary distribution $\mathbf{w}$ (Theorem 11.15).  Consequently the stationary probabilities are strictly positive (Corollary 11.1).

The fundamental matrix $\mathbf{N}$ of an absorbing chain can be used to compute $m_{ij}$ for the corresponding ergodic chain: the $i$th entry of $\mathbf{N}\mathbf{c}$ gives the mean first passage time from state $s_i$ to the absorbing state.

The mean first passage times can be computed directly from the fundamental matrix Z via m_{ij}= (z_{jj}-z_{ij})/w_j.  The stationary‑weighted average of the first‑passage times from any state i equals the Kemeny constant K: \sum_j m_{ij} w_j = K.  The mean recurrence time for state i is a special case given by m_{ii}=1/w_i.  In a reversible chain the mean time from i to j need not equal the mean time from j to i; Exercise 14 asks to test this symmetry.  For a simple symmetric random walk on a circle of size n with step probability p=1/2, the mean first passage time satisfies m_{ij}=d\,(n-d), where d is the clockwise distance from i to j.  In a fair die‑rolling process the mean time between occurrences of a particular face is 6, illustrating that the mean first passage time equals the reciprocal of the face’s stationary probability (1/6).

