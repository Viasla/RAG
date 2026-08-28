# Examples
In the simple case where a parent can have at most two children with probabilities $p_{0}=0.2$, $p_{1}=0.5$, $p_{2}=0.3$, the generating function is $h(z)=p_{0}+p_{1}z+p_{2}z^{2}=0.2+0.5z+0.3z^{2}$. Solving $z=h(z)$ yields the extinction probabilities $d=1$ and $d=p_{0}/p_{2}=2/3$.

When the offspring probabilities form a geometric series $p_{k}=bc^{k-1}$ ($k\ge1$) with $0<b\le1-c$, $0<c<1$, the generating function simplifies to $h(z)=1-\frac{b}{1-c}+\frac{bz}{1-cz}$. For this case $m=h'(1)=\frac{b}{(1-c)^{2}}$.

For the branching process of Example 10.10, with $h(z)=\tfrac12+\tfrac14z+\tfrac14z^{2}$, the second‑generation generating function is $h_{2}(z)=h(h(z))=\tfrac{11}{16}+\tfrac18z+\tfrac{9}{64}z^{2}+\tfrac{1}{32}z^{3}+\tfrac{1}{64}z^{4}$, matching the probabilities obtained directly from the family tree.

