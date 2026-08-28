# Formal Definition
The (k)th moment of a random variable (X) with finite or countable support is (mu_k = E(X^k)=sum_{j=1}^{infty}x_j^k,p(x_j)) provided the sum converges.  The mean and variance are (mu=mu_1) and (sigma^2=mu_2-mu_1^2).  The moment generating function (mgf) is defined by (g(t)=E(e^{tX})=sum_{k=0}^{infty}rac{mu_k,t^k}{k!}=sum_{j=1}^{infty}e^{t x_j},p(x_j)).  Differentiation of (g(t)) at (t=0) yields (mu_n=g^{(n)}(0)).

For a continuous random variable X with density f_X, the n-th moment is defined by \mu_n = E(X^n) = \int_{-\infty}^{+\infty} x^n f_X(x) dx, provided the integral \int |x|^n f_X(x) dx converges and is finite. The moment generating function is defined as g(t) = \sum_{k=0}^{\infty} \frac{\mu_k t^k}{k!} = E(e^{tX}) = \int_{-\infty}^{+\infty} e^{tx} f_X(x) dx, where the series must converge for the given t. Differentiating g(t) at zero yields the moments: g^{(n)}(0) = \mu_n.

