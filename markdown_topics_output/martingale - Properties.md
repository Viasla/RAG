# Properties
For a martingale \(S_n\), the unconditional expectation is constant: \(E(S_n)=E(S_1)\) for all \(n\).

If a game is fair (martingale) and a gambler stops at a bounded stopping time, the expected fortune at stopping remains the initial fortune (an instance of the optional stopping theorem).

A biased coin game where \(p\neq q\) fails the martingale property; the conditional expectation deviates by \(p-q\), making the game either unfavorable (\(p<q\)) or favorable (\(p>q\)).

Elaborate betting systems cannot change the martingale property; they may alter the distribution of outcomes (e.g., increasing the probability of a small gain) but leave the expected value unchanged.

In the stock‑price example, despite Mr. Ace’s system giving a higher than ½ chance of a positive profit after a fixed number of days, the expected profit is exactly zero, illustrating that martingale fairness persists under a wide class of trading rules.

For the martingale constructed by de Moivre, the expected fortune remains constant over time, regardless of the biased odds $p\neq q$.

The martingale property implies that the expected final fortune equals the initial fortune, which is a central theorem in martingale theory and underpins the derivation of ruin probabilities.

When the game ends (one player has all counters), the fairness condition still holds, allowing one to set up equations such as $P_a\left(\sum_{j=a+1}^{a+b}(q/p)^j\right)=P_b\left(\sum_{j=1}^{a}(q/p)^j\right)$ and solve for $P_a$.

