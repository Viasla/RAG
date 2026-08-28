# Properties
Recurrence relation: for n≥3, w_n = (n‑1)·w_{n‑1} + (n‑1)·w_{n‑2}. This follows by conditioning on the image of element 1 in a derangement.

Alternative recurrence: w_n = n·w_{n‑1} + (‑1)^n, which yields the same sequence and is convenient for induction proofs.

Explicit formula (inclusion‑exclusion): w_n = n!·∑_{k=0}^{n} ((‑1)^k)/k! = ⌊n!/e + 1/2⌋, showing the close connection to the exponential function.

Asymptotic behavior: p_n = w_n/n! = 1/e + O(1/n!), so for large n the probability of a derangement tends to 1/e ≈ 0.368.

The sequence {w_n} grows roughly like n!; more precisely w_n ≈ n!/e.

The integer w_n is always the nearest integer to n!/e, providing a simple rounding rule for computing derangements.

