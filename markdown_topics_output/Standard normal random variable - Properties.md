# Properties
Mean and variance: For a standard normal $Z$, the mean is $0$ and the variance is $1$, because $\mu=0$ and $\sigma=1$ in its definition.

Linear transformation property: If $Z$ is standard normal and $X=\sigma Z+\mu$, then $X$ follows a normal distribution with mean $\mu$ and standard deviation $\sigma$, and conversely $Z=(X-\mu)/\sigma$.

Density symmetry: The pdf $f_Z(z)=\frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}$ is symmetric about $z=0$, implying $F_Z(-z)=1-F_Z(z)$ for all $z$.

Lack of closed form: Neither $F_Z$ nor its inverse $F_Z^{-1}$ can be expressed using elementary functions, necessitating numerical methods or tabulated values.

Independence in Box‑Muller: The variables $X$ and $Y$ produced by the Box‑Muller formulas are independent standard normal random variables.

Standard normal tables: Values of $F_Z(z)$ for various $z$ (e.g., $F_Z(2)=0.9772$, $F_Z(-2)=0.0228$) are tabulated, allowing rapid evaluation of normal probabilities without recomputing integrals.

Mean and variance: $E(Z)=0$, $V(Z)=1$.

Symmetry: the density satisfies $f_Z(z)=f_Z(-z)$, so the distribution is symmetric about zero.

Standardisation: if $W\sim N(\mu,\sigma^{2})$, then $Z=(W-\mu)/\sigma$ is standard normal.

Stability under orthogonal linear transformations: if $(X,V)$ are independent standard normal, then any linear combination $aX+bV$ with $a^{2}+b^{2}=1$ is also standard normal (as demonstrated by $Y=\rho X+\sqrt{1-\rho^{2}}V$).

Marginals of the bivariate normal with correlation $\rho$ are standard normal, and the correlation coefficient of the pair equals $\rho$.

Independence implication: if two standard normal variables are independent, their covariance and correlation are zero; the converse need not hold.

