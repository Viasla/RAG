# Examples
Example 6.15: In a fair coin‑toss game where Peter’s fortune changes by \(+1\) or \(-1\) with probability \(1/2\), the conditional expectation satisfies \(E(S_n\mid S_{n-1}=a,\dots)=a\); thus the game is a martingale.

If the coin is biased with heads probability \(p\) and tails probability \(q=1-p\), then \(E(S_n\mid\text{past})=a+p-q\). When \(p\neq q\) the process is no longer a martingale; it is unfavorable if \(p<q\) and favorable if \(p>q\).

Stock‑price illustration (Example 6.16): A simplified model where the price moves up or down by \$1\) each day with probability \(1/2\) yields a martingale for the price process. Mr. Ace’s trading system, which buys at a price \(V\) and sells at \(V+1\) repeatedly, has expected profit zero, illustrating that even elaborate systems cannot convert a martingale into a favorable game.

The martingale doubling system and the Labouchere system (mentioned in Exercises 1.1.9 and 1.1.10) are classic betting strategies that attempt to exploit a fair game but, by the martingale property, cannot produce a positive expected gain.

De Moivre's original gambler's ruin problem, where counters are re‑valued with powers of $q/p$, provides a concrete example of a martingale that leads to the ruin probability $P_a=\frac{(q/p)^a-1}{(q/p)^{a+b}-1}$ for $p\neq q$ and $P_a=\frac{a}{a+b}$ for $p=q=1/2$.

Exercise 9 proposes a simplified martingale where a player's current fortune is defined solely as the value of the next wagered counter, $(q/p)^a$, and shows that the expected fortune after one play still equals the pre‑play fortune, illustrating the martingale property in a more straightforward setting.

