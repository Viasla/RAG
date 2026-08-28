# Properties
For any absorbing Markov chain, the matrix \(I-Q\) is invertible; its inverse \(N=(I-Q)^{-1}\) gives the expected number of visits to each transient state before absorption. The row sums of \(N\) give the expected time to absorption from each transient starting state. The probability of eventual absorption into a particular absorbing state is given by the product \(NR\). Moreover, the probability of ever returning to a transient state is less than one, so the total expected number of returns is finite.

The fundamental matrix exists because I-\mathbf{Q} is invertible for any absorbing chain; \mathbf{N}= (I-\mathbf{Q})^{-1}.

The expected time to absorption from a transient state i is the sum of the i‑th row of \mathbf{N}, i.e., t_i = \sum_j n_{ij}.

The absorption probability matrix \mathbf{B}=\mathbf{N}\mathbf{R} satisfies \mathbf{B}=\mathbf{N}\mathbf{R} and each row of \mathbf{B} sums to one, reflecting that the chain must eventually be absorbed.

If the chain starts in a transient state, the probability of ever returning to that same state is less than one; consequently the total expected number of visits to any transient state is finite, which is precisely the content of the entries of \mathbf{N}.

Transient state is mentioned alongside absorbing state in the context of a Markov chain (page 416).

The index includes an entry "transient" on page 405.

Related concepts such as transition matrix (page 406) and transition probability (page 406) appear near the transient state entries, indicating relevance to its analysis.

