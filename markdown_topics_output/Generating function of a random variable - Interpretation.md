# Interpretation
The coefficient of $z^{k}$ in $h(z)$ is exactly $P\{X=k\}$, so the generating function provides a compact algebraic representation of the distribution. Composition $h_{n+1}(z)=h_{n}(h(z))$ reflects the fact that the $(n+1)^{\text{st}}$ generation is obtained by replacing each individual of generation $n$ with an independent copy of the offspring distribution. Differentiating at $z=1$ extracts moments: $h'(1)=\mathbb{E}[X]=m$ and, by induction, $h'_{n}(1)=m^{n}$, showing exponential growth of the mean when $m>1$.

