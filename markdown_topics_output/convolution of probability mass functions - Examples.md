# Examples
If $X$ and $Y$ are independent binomial$(n,p)$ variables, then $p_Z(j)=(p_X*p_Y)(j)=\binom{2n}{j}p^j q^{2n-j}$, i.e., $Z$ is binomial$(2n,p)$. This follows from $g_Z(t)=(pe^t+q)^{2n}$ or $h_Z(z)=(pz+q)^{2n}$.

If $X$ and $Y$ are independent geometric variables with $p_X(j)=p_Y(j)=q^j p$, then $p_Z$ is negative‑binomial: $h_Z(z)=\frac{p^2}{(1-qz)^2}=p^2\sum_{k=0}^{\infty}(k+1)q^k z^k$, so $p_Z(j)=(j+1)p^2 q^j$.

In general, for any independent discrete $X$ and $Y$, the text states $p_Z$ is the convolution $p_X*p_Y$, and although the direct calculation may be complicated, the generating‑function identities $g_Z(t)=g_X(t)g_Y(t)$ and $h_Z(z)=h_X(z)h_Y(z)$ provide a simpler route.

