# Examples
In the drug‑effect experiment, the researcher treats the probability that the drug is effective as a random variable $x$. For each of $n$ subjects, the outcome is a success if the drug is effective, and failures otherwise; the number of successes $i$ follows a binomial distribution with parameter $x$. After observing $i$ successes, the posterior density for $x$ is $f(x|i)=rac{x^{alpha+i-1}(1-x)^{eta+j-1}}{B(alpha+i,eta+j)}$, showing the binomial as the likelihood component.

In the two‑armed bandit problem, the number of wins on each machine is modeled by a binomial distribution. For machine $i$, with $w_i$ wins and $ell_i$ losses, the estimated probability of winning $p(i)=rac{w_i+1}{w_i+ell_i+2}$ is derived from a beta prior and binomial likelihood.

The number of heads observed when a fair coin is tossed n times has a binomial distribution with n trials and p=1/2.

If a coin has probability p=0.6 of landing heads, then the number of heads in 10 independent tosses follows a binomial distribution with n=10 and p=0.6.

Example 5.3: A typesetter makes on average one mistake per 1000 words; with 100 words on a page, the number of mistakes S_100 follows a binomial distribution with n=100 and p=1/1000. The exact probability is b(100,1/1000,j), while the Poisson approximation gives e^{-0.1} 0.1^j / j!.

Example 5.4: In a 10×10 block district with 100 squares and 400 bombs, the number of hits on a particular square follows a binomial distribution with n=400 and p=1/100; the Poisson approximation uses λ=4.

Example 5.5: In a sample of blood containing A units, the number of white blood cells X can be modeled as binomial with n equal to total white blood cells and p equal to the ratio of the sample size to total blood volume; for an average human with 40 cells per A, this leads to λ=40 and a Poisson approximation.

1. Nuclear power plant accident: With probability p=0.001 per plant and n=100 plants, the probability of at least one accident is 1−(1−p)^n=1−(0.999)^{100}.  This is a binomial calculation.

2. Airline no‑show: 100 reserved seats, 4% no‑show, so the number of passengers who show up Y∼Bin(100,0.96).  The probability that everyone who shows up finds a seat is P(Y≤98).

3. Coin testing: 500 boxes each with one counterfeit coin among 500; testing one coin per box leads to a binomial model with n=500, p=1/500 for finding a counterfeit.  The probability of at least one counterfeit found is 1−(1−1/500)^{500}.

4. Convergence example: Problem 44 demonstrates that as N and k become large with fixed ratio k/N=p, the hypergeometric distribution h(N,k,n,x) tends to the binomial distribution b(n,p,x).

