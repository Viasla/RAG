# Proof
The text does not give a detailed proof of Theorem 11.8; it merely cites the result and notes that the left nullspace of P‑I being one‑dimensional implies the uniqueness of the fixed row vector. The proof for ergodic chains is indicated to follow from the fact that an ergodic transition matrix can be written as a convex combination (½I+½P) that is regular and has the same fixed vectors.

Assume x satisfies Px = x and let M = max_i x_i with x_k = M for some index k. If p_{kj}>0 then from the equality (Px)_k = Σ_j p_{kj} x_j = M we deduce that every x_j with p_{kj}>0 must also equal M. By ergodicity, for any state i there exists a path of positive‑probability transitions from k to i, and iterating the previous argument shows x_i = M for all i. Hence x is constant.

