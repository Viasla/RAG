# Statement
Let \(X_1, X_2, \dots, X_n\) be an independent trials process with common finite expected value \(\mu = E(X_j)\) and finite variance \(\sigma^2 = V(X_j)\). Define \(S_n = X_1 + X_2 + \cdots + X_n\). Then for any \(\epsilon > 0\), \[P\left(\left|\frac{S_n}{n} - \mu\right| \ge \epsilon\right) \to 0\] as \(n \to \infty\), equivalently \[P\left(\left|\frac{S_n}{n} - \mu\right| < \epsilon\right) \to 1\] as \(n \to \infty\).

For a sequence of independent random variables X₁,…,X_n with common finite mean μ and finite variance σ², the weak law asserts that for every ε>0, \lim_{n\to\infty} P\big(|\tfrac{S_n}{n}-\mu|\ge ε\big)=0, equivalently \lim_{n\to\infty} P\big(|\tfrac{S_n}{n}-\mu|<ε\big)=1, where S_n=\sum_{k=1}^n X_k. (Theorem 8.4)

A more general version allowing non‑identical distributions with uniformly bounded variances (σ_k²<R) is proved in Exercise 12: for any ε>0, \lim_{n\to\infty} P\big(|\tfrac{S_n}{n}-\tfrac{M_n}{n}|<ε\big)=1, where M_n=\sum_{k=1}^n m_k and m_k=E(X_k).

In the concrete coin‑toss setting, letting S_n be the number of heads in n tosses of a fair coin, the weak law gives A_n=S_n/n\to 1/2 in probability; i.e., for any ε>0, P(|A_n-1/2|<ε)\to1 as n\to\infty.

