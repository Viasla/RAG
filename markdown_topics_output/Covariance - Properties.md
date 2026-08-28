# Properties
Covariance can be expressed as cov(X,Y)=E(XY) E(X)E(Y) according to Exercise 17(a).

If X and Y are independent then cov(X,Y)=0, but a zero covariance does not imply independence (Exercise 17(b)).

The variance of a sum satisfies V(X+Y)=V(X)+V(Y)+2\,cov(X,Y) (Exercise 17(c)).

Using the variance formula, one obtains 0\le V\big(\frac{X}{\sigma(X)}+\frac{Y}{\sigma(Y)}\big)=2(1+\rho(X,Y)) and 0\le V\big(\frac{X}{\sigma(X)}-\frac{Y}{\sigma(Y)}\big)=2(1-\rho(X,Y)), which together give the bounds -1\le \rho(X,Y)\le 1 (Exercise 18).

For the bivariate normal density f_{X,Y}(x,y)=\frac{1}{2\pi\sqrt{1-\rho^2}}\,e^{-(x^2-2\rho xy + y^2)/[2(1-\rho^2)]}, each marginal is standard normal and the correlation of X and Y equals the parameter \rho (Exercise 20).

