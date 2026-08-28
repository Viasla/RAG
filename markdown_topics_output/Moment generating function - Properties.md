# Properties
Shift: If $Y=X+a$, then $g_Y(t)=e^{ta}g_X(t)$.

Scaling: If $Y=bX$, then $g_Y(t)=g_X(bt)$.

Standardization: For $X^*=(X-\mu)/\sigma$, $g_{X^*}(t)=e^{-\mu t/\sigma}\,g_X(t/\sigma)$.

Independence and addition: If $X$ and $Y$ are independent, $g_{X+Y}(t)=g_X(t)g_Y(t)$.

Corresponding ordinary generating functions satisfy $h_{X+Y}(z)=h_X(z)h_Y(z)$.

Differentiability: $g(t)$ is differentiable for all $t$ because it is a finite sum of exponentials.

Limit identification of support: $x_n=\lim_{t\to\infty}\frac{g'(t)}{g(t)}$ for the largest support point when $X$ has finite range.

