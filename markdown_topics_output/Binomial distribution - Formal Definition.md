# Formal Definition
The probability mass function of the binomial distribution is $m(i|x)=b(n,x,i)=inom{n}{i}x^{i}(1-x)^{j}$ where $i$ is the number of successes, $j=n-i$ is the number of failures, $xin[0,1]$ is the success probability, and $inom{n}{i}$ is the binomial coefficient. The notation $b(n,x,i)$ or $m(i|x)$ is used in the text to denote this function. When the parameter $x$ is random with a beta density $B(alpha,eta,x)$, the marginal probability of observing $i$ successes is $m(i)=inom{n}{i}rac{B(alpha+i,eta+j)}{B(alpha,eta)}$, a beta‑binomial distribution.

The binomial distribution with parameters n, p, and k is defined by the probability mass function

b(n,p,k)=\binom{n}{k} p^k q^{n-k}, where q=1-p.

It gives the probability that a binomial random variable equals k.

This is the distribution of the random variable which counts the number of heads that occur when a coin is tossed n times, assuming that on any one toss the probability of a head occurs is p.

For integer n≥0, success probability 0≤p≤1, and k=0,1,…,n, the probability mass function of the binomial distribution is b(n,p,k)=C(n,k) p^k (1-p)^{n-k}.

In the text the binomial probability is denoted by b(n,p,k), and the expected number of successes is λ= np.

The binomial distribution with parameters n and p is denoted b(n,p,x) in the text, especially in the limit statement of problem 39.  The probability mass function is given by the limit relation: 

b(n,p,x)=lim_{N→∞, k/N→p} h(N,k,n,x), where h is the hypergeometric probability.  In applied problems the probability of exactly x successes is often written implicitly as 

P(X=x)=\binom{n}{x}p^x(1-p)^{,n-x}.

Although the explicit formula is not printed in the excerpt, it is implied in the usage of binomial probabilities.

