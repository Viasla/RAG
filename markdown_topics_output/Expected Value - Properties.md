# Properties
The expected value of a discrete random variable is obtained by multiplying each possible outcome by its probability and summing the results.

If the series $\sum_{x} x\,m(x)$ does not converge absolutely, the random variable is said to have no expected value, as illustrated by the St. Petersburg paradox.

Linearity of expectation is hinted at: the expected value of a sum of simpler random variables can be computed by summing their individual expectations, allowing a quicker calculation of $E(X)$ in the three‑coin toss example.

For a geometric distribution with success probability $p$, the expected waiting time until the first success is $E(T)=1/p$, demonstrating a closed‑form property derived from the series $\sum_{k\ge1} k q^{k-1}p$.

The expected value is linear, allowing combination of separate payoff components; this underlies the derivation of $x$ and $y$ in Huygens’ dice game.

When two random variables are independent, the expectation of their product equals the product of their expectations, as stated by $E(XY)=E(X)E(Y)$; the text asks whether $X$ and $Y$ (sum and difference of dice rolls) satisfy this condition.

Expected value provides a decision criterion that can incorporate infinite payoffs, as in Pascal’s assumption that $v$ is infinite, leading to a dominant strategy regardless of $p$.

Linearity: $E(aX+bY)=aE(X)+bE(Y)$ for any constants $a,b$ and random variables $X,Y$.

If $X$ and $Y$ are independent, $E(XY)=E(X)E(Y)$.

For an indicator variable $X_i$, $X_i^2=X_i$, so $E(X_i^2)=E(X_i)=1/n$ in the hat problem.

The variance is defined as $V(X)=E[(X-E(X))^2]$; for the sum $S_n$ of independent indicators, $V(S_n)=E(S_n^2)-[E(S_n)]^2=1$ as shown in the exercises.

