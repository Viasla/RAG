# Properties
(Duplicate? omitted.)

The binomial distribution can be simulated by summing n independent Bernoulli(p) random variables, requiring n random number generator calls.

For n>=30, the Central Limit Theorem allows approximation by a normal random variable Y with mean μ=np and standard deviation σ=\sqrt{npq}; if -1/2 <= Y < n+1/2, then floor(Y+1/2) can be used as a binomial sample.

The distribution is discrete with support {0,1,…,n}.

When n is large and p is small such that λ=np remains moderate, the binomial distribution can be approximated by the Poisson distribution: P(X=k)≈λ^k e^{-λ}/k!.

Exact binomial probabilities are given by b(n,p,k) and satisfy P(X=0)=(1-p)^n and the recursive ratio b(n,p,k)/b(n,p,k-1)=[(λ-(k-1)p)/(kq)] where q=1-p.

In Table 5.1, the exact binomial values for various n and p are compared with the Poisson approximations, illustrating the closeness of the approximation when λ is small.

The mean of the binomial distribution is μ= np, and its variance is σ^2 = np(1-p).

- The binomial distribution models the number of successes in n independent Bernoulli trials with success probability p.

- The probability of at least one success in n trials is 1−(1−p)^n.

- When the number of trials is large and the probability per trial is small, a binomial distribution may be approximated by a Poisson distribution; this is hinted at in the earlier discussion of Poisson approximation in problems 26 and 31.

- The binomial distribution is the limiting case of the hypergeometric distribution as the population size goes to infinity with the proportion of successes fixed, as explicitly stated in Problem 44.

