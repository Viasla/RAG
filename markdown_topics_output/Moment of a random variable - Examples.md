# Examples
Example 10.1 (Uniform): For (X) on ({1,dots ,n}) with equal probabilities, (g(t)=rac{1}{n}sum_{j=1}^{n}e^{tj}=rac{e^t(e^{nt}-1)}{n(e^t-1)}); (mu_1=(n+1)/2), (mu_2=(n+1)(2n+1)/6), and (sigma^2=(n^2-1)/12). 
Example 10.2 (Binomial): For (Xsim	ext{Bin}(n,p)) on ({0,dots ,n}) with pmf (inom{n}{j}p^j q^{n-j}), (g(t)=(pe^t+q)^n); (mu_1=np), (mu_2=n(n-1)p^2+np), (sigma^2=np(1-p)). 
Example 10.3 (Geometric): For (X) on ({1,2,dots}) with (p_X(j)=q^{j-1}p), (g(t)=rac{pe^t}{1-qe^t}); (mu_1=1/p), (mu_2=(1+q)/p^2), (sigma^2=q/p^2). 
Example 10.4 (Poisson): For (X) on ({0,1,2,dots}) with (p_X(j)=e^{-lambda}lambda^j/j!), (g(t)=e^{lambda(e^t-1)}); (mu_1=lambda), (mu_2=lambda^2+lambda), (sigma^2=lambda). 
Illustration of non‑uniqueness of mean and variance: Two different pmfs (p_X) and (p_Y) on ({1,dots,6}) have identical mean (7/2) and variance (9/4) yet differ in other moments.

Uniform on [0,1]: μ_n = \int_0^1 x^n dx = 1/(n+1); g(t) = (e^t-1)/t. Exponential with rate λ on [0,∞): μ_n = n!/λ^n; g(t) = λ/(λ-t) for |t|<λ. Standard normal N(0,1): μ_n = (2m)!/(2^m m!) for n=2m and 0 for odd n; g(t) = e^{t^2/2}. General normal N(μ,σ^2): g(t) = e^{tμ + (σ^2/2)t^2}. These illustrate the computation of moments and the construction of g(t) for common distributions.

