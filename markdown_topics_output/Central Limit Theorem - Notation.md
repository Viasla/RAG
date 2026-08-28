# Notation
No specific notation for the Central Limit Theorem is introduced in this text.

n! – factorial of n.

Stirling’s formula: n!∼√(2πn)(n/e)^n.

c – circumference of a unit circle (c=2π).

B – infinite series constant found by de Moivre, equal to √c.

2/√(n c) – expression for the relative size of the central term of the binomial distribution.

CLT – abbreviation for Central Limit Theorem

S_n denotes the sum of n Bernoulli trials: S_n=X_1+…+X_n, where each X_i∈{0,1} with P(X_i=1)=p and P(X_i=0)=q=1−p.  S_n^*=(S_n−np)/√(npq) is the standardized sum with mean 0 and variance 1.  φ(x)=1/√(2π)e^{‑x^2/2} is the standard normal density.  ε=1/√(npq) is the spacing between consecutive standardized points x_j.  ⟨a⟩ denotes the nearest integer to a.

S_n: total number of successes in n Bernoulli trials;
p: probability of success on a single trial;
q=1-p: probability of failure;
np: expected number of successes;
\sqrt{npq}: standard deviation of the binomial distribution;
\frac{S_n-np}{\sqrt{npq}}: standardized version of S_n;
\phi(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}: standard normal density;
NA(a,b)=\int_a^b\phi(x)\,dx: area under the standard normal density from a to b.

(S_n) denotes the number of successes in (n) Bernoulli trials with success probability (p); (q=1-p).  The standardized variable is (S_n^*=rac{S_n-np}{sqrt{npq}}).  The cumulative distribution function of a random variable (X) is (F(x)=P(Xle x)).  The standard normal cumulative distribution is denoted (N(x)).  For a binomial distribution the mean is (np) and the variance is (npq).  The notation (sqrt{2pi}) appears in Stirling’s approximation for factorials used by De Moivre.

The theorem uses the following notation:  *X_n* denotes the nth independent discrete random variable; *μ_n* and *σ_n^2* are respectively the mean and variance of *X_n*; *S_n = X_1 + X_2 + ··· + X_n* is the sum of the first n variables; *m_n* and *s_n^2* denote the mean and variance of *S_n*; *A* is a constant that bounds each |X_n| uniformly (i.e., |X_n| ≤ A for all n); and the standardized form (S_n − m_n)/s_n is the variable whose distribution converges to the standard normal distribution.

S_n denotes the sum of n independent random variables.

S_n^* denotes the standardized form of S_n used in the central limit theorem.

X_i represents individual random components contributing to a sum.

H = X_1 + X_2 + ⋯ + X_n + W represents a phenotypic trait expressed as the sum of genetic (X_i) and environmental (W) influences.

(X_i) – individual independent random variables.
(S_n = X_1 + X_2 + dots + X_n) – the sum of the first (n) variables.
(mu = E[X_i]) – common mean of each (X_i).
(sigma^2 = Var[X_i]) – common variance of each (X_i).
(S_n^* = rac{S_n - nmu}{sqrt{n}sigma}) – the standardized sum.
(E(S_n^*) = 0,; Var(S_n^*) = 1) – properties of the standardized sum.


S_n = X_1 + X_2 + … + X_n is the sum of n independent random variables.  S_n^* = S_n/√n = √n A_n is the standardized sum when each X_k has mean 0 and variance 1; more generally, S_n^* = (S_n−nμ)/(σ√n).  A_n = S_n/n is the average of the n observations.  T_n denotes the sum of standardized variables Y_k = (X_k−μ)/σ.  The normal density used in the approximations is φ(x) = (1/(σ√{2π})) e^{−(x−μ)²/(2σ²)}.

S_n denotes the sum X_1 + X_2 + ... + X_n of independent random variables.

μ = E(X_1) is the common mean.

σ^2 = Var(X_1) is the common variance.

t is an integer.

u = (t - n μ)/ sqrt(σ^2 n) is the standardized deviation.

The theorem involves the limit of sqrt(σ^2 n) P(S_n = u sqrt(σ^2 n) + μ n).

