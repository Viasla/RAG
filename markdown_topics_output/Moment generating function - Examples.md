# Examples
If the moments satisfy $\mu_0=1$ and $\mu_k=\frac12+\frac{2^k}{4}$ for $k\ge1$, then $g(t)=\frac14+\frac12e^t+\frac14e^{2t}$, a polynomial in $e^t$.

For a binomial $\operatorname{Bin}(n,p)$ variable $X$, $g_X(t)= (pe^t+q)^n$ where $q=1-p$. The sum of two independent binomials with the same $n$ and $p$ has $g_Z(t)=(pe^t+q)^{2n}$.

For a geometric distribution with $p_X(j)=pq^j$, $g_X(t)=\frac{p}{1-qe^t}$, and the sum of two independent such variables yields $g_Z(t)=\frac{p^2}{1-2qe^t+q^2e^{2t}}$.

Using limits, the largest support point $x_n$ can be recovered as $x_n=\lim_{t\to\infty}\frac{g'(t)}{g(t)}$, and $p(x_n)$ follows from $\lim_{t\to\infty}\frac{g(t)}{e^{t x_n}}$.

