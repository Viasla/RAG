# Examples
Example 10.10 computes the second‑generation generating function for a process with at most two offspring and probabilities p_0=1/2, p_1=1/4, p_2=1/4. Using the recursion h_2(z)=h(h(z)) one obtains h_2(z)=11/16+ (1/8)z+ (9/64)z^2+ (1/32)z^3+ (1/64)z^4, matching the distribution derived directly from the family tree.

Example 10.11 assumes a geometric offspring distribution p_k=bc^{k-1} (k\ge1) with 0<b\le1-c and 0<c<1. The one‑step generating function simplifies to h(z)=1-\frac{b}{1-c}+\frac{bz}{1-cz}, and the recursion h_{n+1}(z)=h_n(h(z)) can be evaluated in closed form because h(z) is a Möbius transformation.

