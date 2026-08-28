# Intuition
The moment generating function $g(t)$ is the expected value of the exponential $e^{tX}$, thus it encodes information about the distribution of $X$ in a way that moments appear as coefficients in its Taylor expansion.

Because $e^{tX}$ expands as $1+tX+t^2X^2/2!+\dots$, taking expectations yields $g(t)=\sum_{k=0}^\infty \mu_k t^k/k!$, so the moments $\,\mu_k=E(X^k)\,$ are directly readable from $g(t)$.

When the support of $X$ consists of non‑negative integers, writing $z=e^t$ transforms $g(t)$ into an ordinary generating function $h(z)=\sum_{j\ge0}p(j)z^j$, linking the two perspectives.

