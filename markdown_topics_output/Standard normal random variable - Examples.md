# Examples
Box‑Muller simulation: Let $U$ and $V$ be independent $\text{Uniform}(0,1)$ variables; then $X = \sqrt{-2\log U}\,\cos(2\pi V)$ and $Y = \sqrt{-2\log U}\,\sin(2\pi V)$ are independent standard normal random variables.

Standardization in probability calculation: For $X\sim N(10,3^{2})$, the probability $P(4\le X\le 16)$ is computed as $F_Z(2) - F_Z(-2)$, where $Z=(X-10)/3$ is the standardized version of $X$ and $F_Z$ values are read from a standard normal table.

In a dart‑throwing experiment, the $x$ and $y$ coordinates are taken as independent standard normal variables; the distance $r=\sqrt{x^{2}+y^{2}}$ then follows a Rayleigh distribution, illustrating the use of standard normals as building blocks for multivariate models.

In Exercise 23 the variables $X$ and $V$ are stipulated to be two standard normal random variables; each therefore satisfies $E(X)=E(V)=0$ and $V(X)=V(V)=1$ and has the density $\frac{1}{\sqrt{2\pi}}e^{-x^{2}/2}$.

The marginal densities of the correlated bivariate normal density 
$$f_{X,Y}(x,y)=\frac{1}{2\pi\sqrt{1-\rho^{2}}}\,e^{-(x^{2}-2\rho xy+y^{2})/[2(1-\rho^{2})]}$$ 
are each standard normal, so both $X$ and $Y$ are standard normal random variables.

Define $Y=\rho X+\sqrt{1-\rho^{2}}\,V$ where $X$ and $V$ are independent standard normal variables.  Using linearity of expectation and independence, $E(Y)=0$ and $V(Y)=\rho^{2}+ (1-\rho^{2})=1$, so $Y$ is again standard normal.

