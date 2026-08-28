# Proof
For Theorem 6.8, with a=E(X) and b=E(Y), V(X+Y)=E((X+Y)^2)−(a+b)^2=E(X^2)+2E(XY)+E(Y^2)−a^2−2ab−b^2. Because X and Y are independent, E(XY)=E(X)E(Y)=ab, which simplifies to V(X)+V(Y). 
Theorem 6.9 follows by induction from Theorem 6.8: V(S_n)=V(Σ_{j=1}^n X_j)=Σ_{j=1}^n V(X_j)=nσ^2. The expectations add similarly. For the average A_n=S_n/n, linearity of expectation gives E(A_n)=E(S_n)/n=nμ/n=μ, and V(A_n)=V(S_n/n)=V(S_n)/n^2=(nσ^2)/n^2=σ^2/n. Taking square roots yields the stated standard deviations.

The text indicates that Theorem 6.16 is proved in exactly the same manner as the corresponding theorem for discrete random variables in Section 6.2; the argument relies on the fact that independence allows the joint expectation of the product (X‑µ_X)(Y‑µ_Y) to equal zero, so that E((X+Y‑µ_X‑µ_Y)²) = E((X‑µ_X)²) + E((Y‑µ_Y)²).

