# Examples
In a sequence of Bernoulli trials with success probability \(p\), letting \(X_i = 1\) for a success and \(0\) otherwise gives \(\mu = p\). The weak law states that \(P\bigl(|\frac{S_n}{n} - p| < \epsilon\bigr) \to 1\) as \(n\to\infty\), meaning the proportion of successes converges in probability to \(p\).

For repeated fair coin tosses, \(S_n/n\) is the fraction of heads. The weak law predicts that as the number of tosses grows, the distribution of \(S_n/n\) becomes increasingly concentrated near \(0.5\), and the probability of the fraction lying between .45 and .55 approaches 1.

When rolling a six‑sided die \(n\) times, each roll has expectation \(7/2\). The weak law gives \(P\bigl(|\frac{S_n}{n} - \frac{7}{2}| < \epsilon\bigr) \to 1\) as \(n\to\infty\), so the average roll approaches \(3.5\) with high probability.

Coin‑toss example: a fair coin tossed n times; the weak law predicts that the proportion of heads S_n/n will be within 0.01 of 1/2 with probability exceeding 0.99 for sufficiently large n.

Biased‑coin example in Exercise 11: with a coin that lands heads with probability 3/4, the weak law guarantees that the observed proportion of heads converges in probability to 3/4, although the exercise also asks how many tosses are needed to be 95 % confident of identifying the coin.

Continuous‑distribution example: if X₁,X₂,… are independent with a common continuous density, finite mean μ and variance σ², then Theorem 8.4 applies and yields the weak law for the sample average of those continuous variables.

