# Properties
Recursion: h_{n+1}(z)=h_n\bigl(h(z)\bigr), which follows from conditioning on the number of individuals in generation n and the independence of offspring.

Mean behavior: differentiating the recursion and evaluating at z=1 gives m_{n+1}=m_n\cdot m, so m_n=m^n. Consequently, if m>1 the expected population grows exponentially, while if m<1 it decays exponentially.

Extinction root: The equation z=h(z) always has the trivial solution z=1; a second solution d<1 exists precisely when m>1, and d is the probability of eventual extinction.

Special case – geometric offspring: When p_k forms a geometric series, h(z)=1-\frac{b}{1-c}+\frac{bz}{1-cz}, a Möbius transformation. Iterating this transformation yields closed‑form expressions for h_n(z) and therefore for the full distribution of Z_n.

Monotonicity: For any n, the sequence d_n=P(\text{extinction by generation }n) satisfies d_{n}=h(d_{n-1}) with d_1=p_0, and d_n\uparrow d as n\to\infty.

