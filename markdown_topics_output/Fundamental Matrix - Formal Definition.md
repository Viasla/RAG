# Formal Definition
For an absorbing Markov chain with canonical form \(P =\begin{pmatrix}Q & R\\ 0 & I\end{pmatrix}\), the fundamental matrix is defined as \(N = (I - Q)^{-1}\). The entry \(n_{ij}\) of \(N\) equals the expected number of times the chain visits transient state \(s_j\) when it starts in transient state \(s_i\), counting the initial visit when \(i=j\).

Let P be the transition matrix of a new absorbing Markov chain that is obtained from an original ergodic chain by making a particular state s_j an absorbing state (i.e., set p_{jj}=1). The fundamental matrix N is defined as the matrix whose (i,k)-entry equals the expected number of visits to state s_k before absorption when starting from state s_i. In other words, N_{ik} = E_i[# visits to s_k before absorption].

The fundamental matrix associated with an ergodic Markov chain with transition matrix $P$ and stationary row vector $mathbf{w}$ is defined as the inverse of the matrix $mathbf{I}-mathbf{P}+mathbf{W}$, where $mathbf{W}$ is the matrix whose rows are all equal to $mathbf{w}$.  In symbols, $mathbf{Z}=(mathbf{I}-mathbf{P}+mathbf{W})^{-1}$.  For a regular chain, the infinite series $mathbf{I}+(mathbf{P}-mathbf{W})+(mathbf{P}-mathbf{W})^2+cdots$ converges to $mathbf{Z}$, and one can show that $(mathbf{P}-mathbf{W})^n=mathbf{P}^n-mathbf{W}$ for every $nge1$.  Even when the chain is ergodic but not regular and $mathbf{P}^n
ot	omathbf{W}$, the matrix $mathbf{I}-mathbf{P}+mathbf{W}$ remains invertible, so $mathbf{Z}$ is well defined for all ergodic chains.

