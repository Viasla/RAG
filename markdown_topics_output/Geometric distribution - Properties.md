# Properties
For j≥1, P(T=j)=q^{j-1}p, and consequently the sum of these probabilities over all j equals 1.

P(T>k)=q^k for any integer k≥0, implying the tail probability decays geometrically.

The distribution is memoryless: P(T>r+s|T>r)=q^s, meaning the remaining waiting time is independent of the elapsed time.

The most probable value of T is always 1, as P(T=1)=p > P(T=j) for j>1.

The random variable Y defined by Y=⌈log(1−rnd)/log q⌉ has the same geometric distribution as T, providing a simulation method whose runtime does not depend on p.

The sum of k independent geometric(p) variables yields a negative binomial distribution with parameters (k,p).

When k=1 in the negative binomial setting, the number of trials until the first success is geometrically distributed.

E(T)=1/p, independent of number of trials.

V(T)=q/p^2, which increases as p decreases.

Large values of p lead to small variance and a sharply peaked distribution, while small values of p produce a heavy‑tailed, spread‑out distribution.

