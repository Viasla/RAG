# Properties
For independent integer‑valued random variables $X_{1},\dots,X_{n}$ with common generating function $k(z)$, the generating function of their sum $S_{n}=\sum_{j=1}^{n}X_{j}$ is $k_{n}(z)=(k(z))^{n}$.

In a Galton–Watson process, the generating functions satisfy the recursion $h_{n+1}(z)=h_{n}(h(z))$; equivalently $h_{n}=h\circ h\circ\dots\circ h$ ($n$ times).

The mean of the $n^{\text{th}}$ generation is $m_{n}=h'_{n}(1)=m^{n}$, where $m=h'(1)$ is the mean number of offspring of a single individual.

The extinction probability $d$ is the smallest non‑negative solution of $z=h(z)$. If $m\le1$, the only solution in $[0,1]$ is $d=1$; if $m>1$, there is a unique solution $d<1$ representing the probability that the branching process eventually dies out.

