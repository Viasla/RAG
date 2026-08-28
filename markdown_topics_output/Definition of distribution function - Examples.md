# Examples
Example 1.13 considers tossing a fair coin until the first head appears; the outcome space is Ω={1,2,3,…} and the distribution function is m(n)=1/2ⁿ for n=1,2,3,…; the series Σ_{n≥1}1/2ⁿ=1 confirms that m is a valid distribution function.

Using the same distribution function, the event E={2,4,6,…} (first head after an even number of tosses) has probability P(E)=Σ_{k≥1}1/2^{2k}=1/3, illustrating how events are evaluated by summing the appropriate m(ω) values.

For a finite sample space with three equally likely outcomes the uniform distribution is m(ω)=1/3 for each ω.

The geometric distribution on Ω={0,1,2,…} defined by m(j)=(1−r)^j r with 0<r<1 satisfies the definition.

Rolling a die until the first six appears yields an infinite sample space Ω={1,2,…} with m(n)=(5/6)^{n‑1}(1/6).

Example 2.13: For $X=U^2$ where $U\sim\text{Uniform}[0,1]$, the distribution function is $F_X(x)=0$ if $x\le0$, $F_X(x)=\sqrt{x}$ if $0\le x\le1$, and $F_X(x)=1$ if $x\ge1$.

Example 2.14: For $Z=X+Y$ where $X$ and $Y$ are independent uniform $[0,1]$, the distribution function is $F_Z(z)=0$ for $z<0$, $F_Z(z)=\tfrac12 z^2$ for $0\le z\le1$, $F_Z(z)=1-\tfrac12(2-z)^2$ for $1\le z\le2$, and $F_Z(z)=1$ for $z>2$.

