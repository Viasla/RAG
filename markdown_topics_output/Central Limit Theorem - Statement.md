# Statement
The Central Limit Theorem is a fundamental result that describes the approximation of standardized binomial distributions to the normal curve.

De Moivre established the celebrated central limit theorem by applying Stirling’s approximation to the binomial distribution.

When n is relatively large (say at least 30), the Central Limit Theorem (see Chapter 9) implies that the binomial distribution is well-approximated by the corresponding normal density function with parameters μ = np and σ = √(npq).

A very general theorem, called the Central Limit Theorem, explains why distributions of sums of independent random variables become bell‑shaped as the number of terms increases.

For any sequence of independent, identically distributed random variables with finite mean and variance, the sum S_n is approximately normally distributed with mean nµ and variance nσ², i.e. the distribution function of S_n can be well approximated by the normal density f_{µ,σ}(x).

Theorem 9.1 (Central Limit Theorem for Binomial Distributions): ∞_{n→∞} sqrt{npq},b(n,p,langle np+xsqrt{npq}angle)=phi(x), where phi(x)=rac{1}{sqrt{2pi}}e^{-x^2/2} is the standard normal density.

For a sequence of n independent Bernoulli trials each having probability of success p, let S_n be the total number of successes. Fix two real numbers a and b. Then 
\lim_{n\to\infty}\;P\left(a\le\frac{S_n-np}{\sqrt{npq}}\le b\right)\;=\int_a^b\phi(x)\,dx,\nwhere q=1-p and \phi(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2} is the standard normal density.

The Central Limit Theorem states that for independent Bernoulli trials with success probability p, the standardized sum S_n^*=(S_n−np)/√(npq) converges in distribution to a standard normal random variable as the sample size n increases.

In the college acceptance problem, the CLT is applied to approximate the probability that the number of accepted students who matriculate exceeds a threshold, using a normal approximation to the binomial distribution of the sum of Bernoulli trials.

In polling, the CLT justifies treating the sample proportion ar{p}=S_n/n as approximately normally distributed with mean p and variance pq/n when n is large and the population is effectively infinite relative to the sample.

The CLT provides a basis for constructing confidence intervals for the unknown population proportion p by replacing the true parameters in the standardized form with their sample estimates.

The CLT underlies the use of polling simulation to demonstrate that about 95% of intervals of the form (ar{p}−2√(pq/n),ar{p}+2√(pq/n)) contain the true p.

The CLT also explains why the margin of error in large‑sample polls is essentially independent of the population size.

For a sequence of independent and identically distributed random variables ({X_i}) with finite mean (mu) and finite non‑zero variance (sigma^2), let (S_n=sum_{i=1}^n X_i).  Then as (n	oinfty), the standardized sum (displaystyle rac{S_n-nmu}{sigmasqrt{n}}) converges in distribution to the standard normal distribution (N(0,1)).  In particular, for Bernoulli trials with success probability (p), the binomial random variable (S_n) satisfies (displaystyle rac{S_n-np}{sqrt{npq}}stackrel{d}	o N(0,1)), where (q=1-p).

For a sequence of independent discrete random variables {X_n} with means μ_n and variances σ_n^2, let S_n = X_1 + X_2 + ··· + X_n, and let m_n and s_n^2 be the mean and variance of S_n, respectively.  Assume that the sequence is uniformly bounded so that there exists a constant A with |X_n| ≤ A for every n, and assume that s_n → ∞.  Then for any real numbers a < b, the limit of the probability that the standardized sum lies between a and b equals the integral of the standard normal density over that interval: lim_{n→∞} P(a < (S_n − m_n)/s_n < b) = (1/√(2π)) ∫_a^b e^{−x^2/2} dx.

For independent random variables X_1,…,X_n with finite mean μ and variance σ², the standardized sum (S_n−nμ)/(σ√n) converges in distribution to a standard normal variable as n→∞.

The theorem extends to non‑identically distributed variables under conditions such as the Lindeberg or Lyapunov criteria, yielding the same normal limit after appropriate centering and scaling.

For a sequence of independent random variables (X_1,X_2,dots ,X_n) each having finite mean (mu) and variance (sigma^2), the sum (S_n=sum_{i=1}^n X_i) has a distribution that approaches a normal distribution with mean (nmu) and variance (nsigma^2) as (n	oinfty).  Equivalently, the standardized sum (S_n^*=rac{S_n-nmu}{sqrt{n}sigma}) tends to a standard normal distribution as (n) grows.

1. The Central Limit Theorem states that if {X_k} are independent random variables with common mean μ and variance σ², then the standardized sum S_n^* = (X_1+…+X_n−nμ)/(σ√n) converges in distribution to the standard normal distribution as n→∞.  2. More generally, for independent variables with possibly different means and variances, the normalized sum (∑X_k−∑μ_k)/√∑σ_k² tends to N(0,1).  3. In the text, the CLT is phrased as “the sums of independent random variables tend to look normal, no matter what crazy distribution the individual variables have.”  4. The CLT gives better estimates of tail probabilities for averages than Chebyshev’s inequality; e.g., the probability that the average of 25 independent uniform(0,20) variables lies within 1 foot of its mean is estimated more accurately using normal approximations than using g(x)=4/(3x²).

The Central Limit Theorem for sums of independent integer‑valued random variables is stated as: if S_n = X_1 + X_2 + ... + X_n, with mean μ and variance σ^2, and u = (t - n μ) / sqrt(σ^2 n), then as n → ∞, sqrt(σ^2 n) P(S_n = u sqrt(σ^2 n) + μ n) → (1/√(2π)) e^{-u^2/2}.

The Central Limit Theorem for bounded continuous random variables states that if $X$ is a continuous random variable with density $f_X$, mean $mu=0$ and variance $sigma^2=1$, and $g(t)$ is its moment generating function defined for all $t$, then for an independent trials process $X_1,dots ,X_n$ each with density $f_X$, the standardized sum $S_n^*=S_n/sqrt n$ converges in distribution to the standard normal distribution $N(0,1)$.  A corresponding theorem holds for bounded discrete random variables with integer values, where the same convergence of $S_n^*$ to $N(0,1)$ occurs.

Theorem 9.6 (continuous case) and Theorem 9.4 (discrete case) formalise this convergence of distribution functions and densities to the normal law.

The text mentions that a Central Limit Theorem for Markov Chains will be stated (but not proved), and that its statement involves the fundamental matrix of the chain. No explicit statement of the theorem is provided in the excerpt.

Central Limit Theorem is referenced in the index as applicable to Bernoulli trials (page 325), to binomial distributions (page 330), to continuous independent trials processes (page 328), to discrete independent random variables (page 357), to discrete independent trials processes (page 345), and to Markov chains (page 343).

The theorem is discussed under sections titled 'Central Limit Theorem' and associated program references such as CLTGeneral, CLTBernoulliGlobal, CLTBernoulliLocal, CLTIndTrialsLocal, and CLTIndTrialsPlot.

Central Limit Theorem for Markov chains is mentioned in the index at page 464.

The index lists a reference to the Central Limit Theorem under the heading "statistics applications of the Central Limit Theorem to," directing the reader to page 333.  This indicates that the text contains a section devoted to applying the theorem in statistical contexts.

