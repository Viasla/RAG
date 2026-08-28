# Proof
Pascal’s proof used backward induction on the number of games in the problem of points, showing that the probability of a given outcome can be written as a sum of binomial terms, which directly yields the expansion formula.

A combinatorial proof counts the number of ways to select r positions among n for the factor b; each such selection corresponds to a term a^{n‑r}b^{r}, giving the coefficient binom{n}{r}.

Algebraic induction proves the statement by assuming (a+b)^k = Σ_{r=0}^{k} binom{k}{r} a^{k‑r}b^{r} and multiplying both sides by (a+b), then using the identity binom{k}{r}+binom{k}{r‑1}=binom{k+1}{r} to obtain the formula for k+1.

