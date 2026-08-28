# Proof
Starting from the definition h(z)=E(z^{S_N}), condition on the value of N: h(z)=\sum_{k=0}^{\infty}E(z^{S_N}\mid N=k)P(N=k). Since the X_i are independent and identically distributed, E(z^{S_N}\mid N=k)=\big(E(z^{X_1})\big)^k = f(z)^k. Hence h(z)=\sum_{k=0}^{\infty}f(z)^k P(N=k)=g(f(z)), which is exactly the composition of the two generating functions.

