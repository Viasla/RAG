# Proof
Let Z1 be the number of offspring of the initial individual, with generating function f(z). For each of these Z1 individuals, let Zi (i=2,…,Z1+1) be the number of their offspring. The total number after two generations is S=∑_{i=2}^{Z1+1} Zi. Conditionally on Z1=k, the generating function of S is [f(z)]^k, because the Zi’s are i.i.d. with generating function f(z). Taking expectation over Z1 gives E[z^S] = ∑_{k} f(z)^k P(Z1=k) = f(f(z)).

