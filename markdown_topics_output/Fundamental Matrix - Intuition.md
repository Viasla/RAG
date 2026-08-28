# Intuition
For an ergodic chain there are no absorbing states, so the naïve inverse $(I-P)^{-1}$ does not exist because $I-P$ is singular (the stationary vector $c$ satisfies $(I-P)c=0$). The authors therefore seek a matrix that plays the same role as $N$ by exploiting the fact that $P^n\to W$, the limiting matrix whose rows are the stationary distribution. Subtracting $W$ from each power of $P$ removes the non‑decaying component, yielding a convergent series analogous to the geometric series for $Q$ in the absorbing case.

The text suggests that the fundamental matrix encapsulates the long‑run behavior of a Markov chain, allowing one to derive quantities such as mean recurrence times without resorting to spectral methods.

