# Intuition
A standard normal random variable serves as the canonical member of the normal family; any other normal variable can be obtained by shifting (adding $\mu$) and scaling (multiplying by $\sigma$) this baseline variable.

Standardization converts an arbitrary normal variable $X\sim N(\mu,\sigma^2)$ into a standard normal $Z$ by subtracting its mean and dividing by its standard deviation: $Z = (X-\mu)/\sigma$.

In simulation, generating two independent uniform(0,1) variables $U$ and $V$ and applying the Box‑Muller transformation $Z = \sqrt{-2\log U}\,\cos(2\pi V)$ (or $\sin$) produces a standard normal variate, reflecting the intuition that random angles and radii in polar coordinates yield Gaussian coordinates.

The standard normal random variable is the prototypical normal variable: it is centred at zero and spread so that its variance equals one.  Consequently any other normal variable can be obtained by shifting and scaling a standard normal, and many theoretical results are expressed most simply in terms of the standard normal.

In a bivariate normal model with correlation ρ, each coordinate behaves like a standard normal when examined alone, even though the pair may be dependent.

