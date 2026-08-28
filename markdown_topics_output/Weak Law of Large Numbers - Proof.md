# Proof
Since the \(X_i\) are independent and identically distributed, \(V(S_n) = n\sigma^2\) and therefore \(V\left(\frac{S_n}{n}\right) = \frac{\sigma^2}{n}\). The expected value of the sample average is \(E\left(\frac{S_n}{n}\right) = \mu\). Applying Chebyshev's Inequality, for any \(\epsilon>0\) we have \[P\left(\left|\frac{S_n}{n} - \mu\right| \ge \epsilon\right) \le \frac{\sigma^2}{n\epsilon^2}.\] Because the right‑hand side tends to zero as \(n\to\infty\), the probability that the sample average deviates from \(\mu\) by at least \(\epsilon\) also tends to zero, establishing the weak law.

The proof proceeds by applying Chebyshev’s inequality: for each n, P\big(|\tfrac{S_n}{n}-\mu|\ge ε\big)\le \frac{\operatorname{Var}(S_n)}{n^2 ε^2}=\frac{σ^2}{n ε^2}, which tends to 0 as n\to\infty, establishing the weak law for i.i.d. variables. (Theorem 8.4)

For the non‑identical case, Chebyshev gives P\big(|\tfrac{S_n}{n}-\tfrac{M_n}{n}|\ge ε\big)\le \frac{\sum_{k=1}^n\sigma_k^2}{n^2 ε^2}\le \frac{nR}{n^2 ε^2}=\frac{R}{n ε^2}, which again vanishes as n\to\infty, proving the statement in Exercise 12.

