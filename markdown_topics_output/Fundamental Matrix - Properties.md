# Properties
The matrix \(I - Q\) is invertible for any absorbing Markov chain, guaranteeing the existence of \(N\).

The fundamental matrix can be expressed as a convergent Neumann series: \(N = I + Q + Q^{2} + \dots\), because \(Q^{n}\to 0\) as \(n\to\infty\).

For any transient state \(s_i\), the expected time to absorption is \(t_i = \sum_{j} n_{ij}\), i.e., the row sum of \(N\).

The matrix of absorption probabilities satisfies \(B = N R\), linking transient dynamics (\(N\)) and the chances of ending in each absorbing state (\(R\)).

If \(x\) satisfies \((I - Q)x = 0\), then \(x = 0\); this uniqueness result underpins the invertibility of \(I - Q\).

• Each entry of N is non‑negative because it counts expected visits. 
• The rows of N sum to the expected total number of visits before absorption for each starting state. 
• For an absorbing Markov chain with transition matrix in canonical form 
  P = (egin{pmatrix}I & R \ 0 & Qend{pmatrix}), the fundamental matrix is (N = (I-Q)^{-1}).

