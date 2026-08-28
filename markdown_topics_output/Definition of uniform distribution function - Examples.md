# Examples
For a six‑sided die each face \(1,2,\dots,6\) has probability \(1/6\); the probability of rolling an even number is \(3/6=1/2\). A fair coin toss has two outcomes each with probability \(1/2\). The text also notes that a uniform distribution cannot be defined on a countably infinite space such as \(\Omega=\{1,2,3,\dots\}\) because assigning the same positive probability to each outcome would make the total sum diverge.

A fair six‑sided die has a uniform distribution m(k)=1/6 for k=1,…,6.

A fair coin has a uniform distribution m(H)=m(T)=1/2.

Attempting to assign m(k)=c for each integer k∈ℕ fails: if c>0 then ∑_{k=1}^{∞}c diverges, and if c=0 then the total probability is 0, not 1.

In case 1 the program chooses the coordinates x and y independently from the interval [‑1,1] at random, which corresponds to a uniform distribution on the square [‑1,1]×[‑1,1].

In case 2 the program chooses the scalar r from the interval [‑1,1] at random, which corresponds to a uniform distribution on that interval; the probability that |r|<1/2 is computed as (1/2‑(‑1/2))/(1‑(‑1))=1/2, the ratio of the length of the favorable sub‑interval to the total length.

In case 3 the program chooses the angle α from the interval [0,2π] at random, which corresponds to a uniform distribution on that interval; the probability that 2π/3<α<4π/3 is computed as (4π/3‑2π/3)/(2π‑0)=1/3, the ratio of the angular sub‑interval length to the total angle.

