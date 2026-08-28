# Examples
Dice game: rolling a fair die, winning the face value on odd rolls and losing it on even rolls, yields an expected gain $\mu = \frac{1}{6}(1-2+3-4+5-6) = -\frac{3}{6}= -0.5$, matching simulation averages of $-0.57$ (100 rolls) and $-0.4949$ (10,000 rolls).

Three‑coin toss: letting $X$ be the number of heads, the possible values $0,1,2,3$ have probabilities $1/8,3/8,3/8,1/8$ respectively, giving $E(X)=0\cdot\frac18+1\cdot\frac38+2\cdot\frac38+3\cdot\frac18=\frac32$.

Geometric waiting time: tossing a fair coin until the first head, with $X$ the number of tosses, $m(i)=\frac1{2^i}$, leads to $E(X)=\sum_{i=1}^{\infty} i\frac1{2^i}=2$.

St. Petersburg paradox: if a player is paid $2^n$ dollars when the first head appears on the $n$‑th toss, then $P(Y=2^n)=\frac1{2^n}$ and $E(Y)=\sum_{n=1}^{\infty}2^n\frac1{2^n}$ diverges, so $Y$ has no expectation.

Expected waiting time for first success in a Bernoulli process: with success probability $p$, $E(T)=\frac1p$; for a fair coin this gives an expected 2 tosses until the first head, and for a fair die an expected 6 rolls until the first six.

Height example: choosing a woman from the Swarthmore basketball team at random, the random variable $X$ (height in inches) has an average $\frac{69+69+66+68+71+65+67+66+66+67+70+72}{12}=67.9$, which is the expected value $E(X)$.

Huygens’ Proposition XIV: two players alternate rolling dice; the game ends if Huygens rolls a 7 or his opponent rolls a 6. Solving the equations for $x$ and $y$ yields $x=31/61$, the expected probability of Huygens winning.

Pascal’s wager: compare $p(-u)+(1-p)v$ with $p\cdot0+(1-p)(-x)$ to decide whether belief or non‑belief maximizes expected payoff, assuming an infinite $v$ makes belief optimal regardless of $p$.

Graunt’s mortality table assumes a constant $5/8$ survival probability per decade, allowing calculation of expected surviving populations at successive ages.

Pricing a life annuity: the expected value of a terminal annuity over the random lifetime gives a rational price, a direct application of expected value to finance.

Thorp’s blackjack strategy: using expected value calculations to show that a certain betting system yields a positive expected win per hand.

In the hat‑return problem, $X_i$ is the indicator of person $i$ receiving his own hat; $E(X_i)=1/n$, so the expected total number of correct returns $E(S_n)=\sum_{i=1}^n E(X_i)=1$.

For $n$ independent Bernoulli trials with success probability $p$, the number of successes $S_n$ has $E(S_n)=np$, and the standardized variable $S_n^*=(S_n-np)/\sqrt{npq}$ has expected value $0$.

For a sample of $n$ observations $x_1,\dots,x_n$ from a population with mean $\mu$, the sample mean $\bar x=\frac1n\sum_{i=1}^n x_i$ satisfies $E(\bar x)=\mu$.

