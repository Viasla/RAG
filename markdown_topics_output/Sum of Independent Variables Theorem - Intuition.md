# Intuition
When two independent random variables X and Y are summed to produce Z = X + Y, the density of Z at a particular point z must account for all pairs (x,y) such that x + y = z. Because X and Y are independent, the joint density of (X,Y) factorizes as f_X(x)f_Y(y). Integrating this product over all y that satisfy x = z – y gives the contribution to f_Z(z). This integral is exactly the convolution of f_X and f_Y, illustrating intuitively how the distribution of the sum is built from the individual distributions.

