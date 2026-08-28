# Proof
By definition of geometric distribution, P(T > k) = q^k. Hence P(T > r + s | T > r) = P(T > r + s)/P(T > r) = q^{r+s}/q^r = q^s, which depends only on s.

For the exponential density, let T ~ Exp(λ). Then \(P(T > r + s \mid T > r) = \frac{P(T>r+s)}{P(T>r)} = \frac{e^{-\lambda(r+s)}}{e^{-\lambda r}} = e^{-\lambda s}\). On the other hand, \(P(T > s) = 1 - F(s) = e^{-\lambda s}\), so the two sides are equal, proving the property for the exponential distribution. The same algebraic manipulation shows that the geometric distribution also satisfies the equality.

