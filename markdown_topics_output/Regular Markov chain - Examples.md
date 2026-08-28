# Examples
The weather model for the Land of Oz (states R, N, S) provides an example: after six steps the rows of P^6 are all approximately (0.4, 0.2, 0.4), so the probability of rain, nice weather, or snow is .4, .2, .4 regardless of the initial weather. This demonstrates a regular Markov chain.

Example 11.16: For the two‑state chain with transition matrix P = (1/2)[[0,1],[1,0]], the chain is ergodic but not regular because odd powers cannot return to the original state and even powers cannot reach the opposite state.

Example 11.17 (Ehrenfest urn): The transition matrix shown leads to the property that after any even number of steps the chain is in states 0,2,4 and after any odd number of steps it is in states 1,3; thus the chain is ergodic but not regular.

Land of Oz example (Section 11.1): Although the original matrix contains a zero entry (p_{NN}=0), the second power P^{2} has no zeros, making the chain regular.

Absorbing chain example: With P = [[1,0],[1/2,1/2]] every power of P retains a zero in the upper‑right corner, showing that an absorbing chain is not regular.

Example 11.18: For the Land of Oz chain, the sixth power P^{6} already has identical rows (≈[0.4,0.2,0.4]), illustrating rapid convergence of a regular chain to its limiting matrix.

