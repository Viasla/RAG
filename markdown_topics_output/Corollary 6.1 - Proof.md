# Proof
The corollary follows from the linearity of expectation and the variance of a sum of independent random variables.  Applying Theorem 6.10 (linearity of expectation) gives E(S_n)=∑_{i=1}^n E(X_i)=n μ, and then E(A_n)=E(S_n)/n = μ.  Applying Theorem 6.15 (variance of independent sums) gives V(S_n)=∑_{i=1}^n V(X_i)=n σ^2, and V(A_n)=V(S_n)/n^2 = σ^2 / n.  The standardized variable S_n^* is obtained by centering S_n at its mean n μ and scaling by its standard deviation sqrt(n σ^2), giving the stated mean 0 and variance 1.

