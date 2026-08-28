# Interpretation
Regularity means the chain ‘forgets’ its initial condition: as n grows, P^n approaches a matrix whose rows are identical, representing the limiting distribution (stationary distribution) that the chain will occupy regardless of its starting state.

Regularity guarantees that, for some fixed horizon n, the chain can transition between any pair of states in exactly n steps, which implies that the chain is irreducible and aperiodic.

Theorem 11.7 interprets the limiting matrix W as describing the long‑run behavior: regardless of the initial state, the probability of being in state s_{i} after a large number of steps converges to w_{i}, the i‑th component of the stationary distribution w.

The fixed row vector w satisfies wP = w, meaning that w is invariant under one step of the chain; similarly, the column vector c satisfies Pc = c, reflecting preservation of total probability.

