# Proof
The proof uses Theorem 6.1 (expectation of a function of a random variable). By writing X+Y as the function φ(x,y)=x+y applied to the joint random variable (X,Y), one obtains E(X+Y)=∑_j∑_k (x_j+y_k)P(X=x_j,Y=y_k). Splitting the double sum yields ∑_j x_jP(X=x_j)+∑_k y_kP(Y=y_k), which are precisely E(X) and E(Y). For a constant c, E(cX)=∑_j c x_j P(X=x_j)=c∑_j x_jP(X=x_j)=cE(X). The argument extends by induction to any finite sum, showing that mutual independence is not required.

