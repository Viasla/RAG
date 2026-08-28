# Examples
In the Land of Oz weather model, the states are Rain (R), Nice (N), and Snow (S). The transition matrix is \mathbf{P}=\begin{pmatrix} 1/2 & 1/4 & 1/4 \\ 1/2 & 0 & 1/2 \\ 1/4 & 1/4 & 1/2 \end{pmatrix}, so p_{13}=1/4 is the probability of going from Rain today to Snow tomorrow.

The two‑step transition probability from Rain to Snow is computed as p_{13}^{(2)} = p_{11}p_{13} + p_{12}p_{23} + p_{13}p_{33}, which corresponds to the (1,3) entry of \mathbf{P}^2.

Table 11.1 shows the successive powers \mathbf{P}, \mathbf{P}^2, …, \mathbf{P}^6 for the same weather chain, illustrating how the transition probabilities evolve over multiple steps and converge to .4, .2, .4 for R, N, S respectively after six steps.

