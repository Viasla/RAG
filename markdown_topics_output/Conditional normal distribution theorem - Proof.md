# Proof
Given the joint density f_{X,Y}(x,y)=\frac{1}{2π\sqrt{1-ρ^2}}\exp\!Big[-\frac{x^2-2ρxy+y^2}{2(1-ρ^2)}\Big] and the marginal f_Y(y)=\frac{1}{\sqrt{2π}}\exp(-y^2/2), the conditional density is f_{X|Y}(x|y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}.  Simplifying the exponential exponent yields \!\exp\!Big[-\frac{(x-ρy)^2}{2(1-ρ^2)}\Big], which is the kernel of a normal density with mean ρy and variance 1-ρ^2.  The normalization constant is 1/\sqrt{2π(1-ρ^2)}, confirming that f_{X|Y}(x|y) is a proper normal density.

