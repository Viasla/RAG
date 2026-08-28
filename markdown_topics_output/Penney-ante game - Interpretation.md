# Interpretation
Conway’s odds formula 
\[\frac{p_A}{p_B}=\frac{BB-BA}{AA-AB}\] 
expresses the win‑loss odds for the first player purely in terms of the deterministic payoffs associated with the two patterns. The derivation uses the linearity of expectation: the total expected time to reach B can be decomposed as the expected time to reach either A or B plus the probability that A occurs first times the expected additional time from A to B, i.e. \(BB=E(T^{A\;or\;B})+p_A(BB-AB)\). Swapping A and B gives a second equation. Solving the two equations together with \(p_A+p_B=1\) yields the stated odds. This shows that the game’s bias can be computed without enumerating all possible toss sequences, relying only on the combinatorial structure of the patterns.

