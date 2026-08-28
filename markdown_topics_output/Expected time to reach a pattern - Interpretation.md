# Interpretation
The expected waiting time for a pattern is exactly the expected total payout of a fair gambling game in which gamblers bet on each successive coin toss until the pattern appears; because the game is fair, the casino’s expected profit is zero, so the expected payout equals the number of gamblers (one per toss), which is E(T^B).

In the absorbing Markov chain model, each state corresponds to the longest suffix of the observed tosses that matches a prefix of the target pattern; moving to the absorbing state (the full pattern) corresponds to the pattern’s first occurrence, and the expected number of transitions before absorption is the desired waiting time.

The combinatorial tail‑sum method interprets P(T>n) as the proportion of length‑n sequences that have not yet contained the pattern; summing these tail probabilities yields the mean waiting time for the pattern.

