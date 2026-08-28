# Proof
The joint density of (X,Y) is f_X(x)f_Y(y) by independence. The density of the sum Z at z is the probability that X+Y falls in an infinitesimal interval around z, which equals the integral of the joint density over all pairs satisfying x+y=z. Changing variables to y gives

f_Z(z) = \int_{-\infty}^{+\infty} f_X(z - y) f_Y(y) \,dy,

which is precisely the definition of the convolution f_X * f_Y. Thus f_Z = f_X * f_Y, establishing the theorem.

