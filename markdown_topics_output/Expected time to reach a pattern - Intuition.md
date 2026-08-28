# Intuition
Because each bet in the gambling scheme is fair, the casino’s expected profit (the amount taken in) must equal its expected payout; the payout equals the total amount paid to gamblers who win when the pattern finally appears, so the expected payout equals the expected number of tosses needed to see the pattern.

Viewing the process as an absorbing Markov chain, the system starts in the empty‑prefix state and moves through longer prefixes until the full pattern is reached; the expected number of steps before absorption is exactly the expected waiting time for the pattern.

The combinatorial argument shows that the probability the pattern has not yet appeared after n tosses is a linear combination of the probabilities that it appears at specific later times, and summing these tail probabilities yields the expected waiting time.

