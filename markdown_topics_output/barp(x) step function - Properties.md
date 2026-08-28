# Properties
The function $\bar{p}(x)$ is defined for every real $x$, and satisfies $\bar{p}(j)=p(j)$ for every integer $j$.

Its graph consists of a series of horizontal line segments (steps) of width 1 and heights given by the probabilities $p(j)$; outside the union of the intervals $[j-\tfrac12, j+\tfrac12)$ the function equals zero.

The moment‑generating function of $\bar{p}(x)$ can be expressed in terms of the original $g(t)$ as $\bar{g}(t)=g(t)\frac{\sinh(t/2)}{t/2}$.

Similarly, $\bar{g}_n(t)=g_n(t)\frac{\sinh(t/2)}{t/2}$ and $\bar{g}_n^{*}(t)=g_n^{*}(t)\frac{\sinh(t/(2\sqrt{n}))}{t/(2\sqrt{n})}$.

As $n\to\infty$, $\bar{g}_n^{*}(t)$ converges to $e^{t^{2}/2}$, the moment‑generating function of the standard normal distribution, because $\frac{\sinh(t/(2\sqrt{n}))}{t/(2\sqrt{n})}\to 1$.

Consequently, the standardized step functions $\bar{p}_n^{*}(x)$ converge pointwise to the normal density $\frac{1}{\sqrt{2\pi}}e^{-x^{2}/2}$ for all $x$.

The step‑function construction eliminates the problem that the original discrete pmf $p(x)$ is defined only at integer points, allowing the use of analytic tools that require functions defined on the whole real line.

