# Interpretation
The standard normal CDF $F_Z(z)$ gives the probability that a standard normal variable lies below the threshold $z$, i.e., $F_Z(z)=P(Z\le z)$. This interpretation allows any normal probability to be expressed via $F_Z$ after standardization.

In simulation, the Box‑Muller transformation interprets two uniform random draws as polar coordinates; the resulting radius and angle generate Gaussian coordinates, providing a concrete probabilistic mechanism for producing standard normal samples.

Standardization interprets a generic normal measurement $X$ in terms of its distance, measured in units of standard deviation, from its mean; this dimensionless quantity $Z$ follows the standard normal distribution.

Each standard normal variable represents a centred, unit‑variance measurement; probabilities such as $P(Z\leq a)$ are obtained from the standard normal CDF $\Phi(a)$.

In the correlated bivariate normal model, the statement “$X$ and $Y$ each have standard normal densities” means that, although $X$ and $Y$ may be dependent, their individual behaviour is indistinguishable from a $N(0,1)$ variable.

The linear combination $Y=\rho X+\sqrt{1-\rho^{2}}V$ can be interpreted as rotating the independent standard normal vector $(X,V)$ in the plane; the rotation preserves the marginal standard normal distribution.

