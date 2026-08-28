# Properties
For a regular chain the common row of the limiting matrix W is the unique fixed row vector that is also a probability vector (components non‑negative, sum to one, and strictly positive).

Any fixed row vector for P is a scalar multiple of w; any fixed column vector for P is a scalar multiple of the constant vector c.

A fixed row vector is a left eigenvector of P associated with eigenvalue 1; a fixed column vector is a right eigenvector associated with eigenvalue 1.

The fixed row vector w satisfies wP = w and, when normalised, has components that sum to 1; for regular chains these components are all positive.

The fixed column vector x satisfies Px = x and, in the regular case, is the all‑ones vector, indicating that the column sums of P equal 1.

The fixed vector is invariant under the transition: multiplying it by P leaves it unchanged (wP = w).

For an ergodic (irreducible and aperiodic) finite Markov chain the fixed vector exists, is unique, and all its entries are strictly positive.

If P* is the reverse (time‑reversed) transition matrix, then P and P* share the same fixed vector w, as noted in Exercise 13.

The mean recurrence time to state i equals 1/w_i, linking the fixed vector to expected return times.

The fixed vector serves as the limiting distribution: for any initial distribution μ, μP^k → w as k → ∞ for ergodic chains.

