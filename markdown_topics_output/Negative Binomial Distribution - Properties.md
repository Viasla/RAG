# Properties
Support: x\in\{k,k+1,k+2,\dots\}.

Probability mass function: \(P(X=x)=\binom{x-1}{k-1}p^{k}q^{x-k}\).

Simulation: X can be generated as the sum of k independent geometric variables, e.g., \(\sum_{j=1}^{k}\left\lceil\frac{\log\,rnd_{j}}{\log\,q}\right\rceil\).

Shape: The distribution is asymmetric with a long right tail, as illustrated for k=2 and p=0.25 in Figure 5.2.

Relation to geometric distribution: When k=1 the pmf reduces to the geometric pmf, which has the memoryless property; for k>1 the memoryless property no longer holds.

