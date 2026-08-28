# Formal Definition
Let D be a deck of n distinct cards. An a‑unshuffle is a mapping from a permutation of the deck back to the identity ordering that corresponds to the inverse of an a‑shuffle. In the coding used in Theorem 3.9, the set S of all n‑tuples M = (m_1, …, m_n) with each m_j ∈ {0,…,a‑1} represents all possible labelings of the cards; the a‑unshuffle associated with M takes a shuffled deck and places each card whose label is i back into the i‑th block of the original ordered deck, preserving the relative order within each block.

Equivalently, if an a‑shuffle is defined by the labeling procedure described (label the first n_0 cards with 0, the next n_1 cards with 1, …), then the a‑unshuffle is the unique permutation σ such that σ∘(a‑shuffle) = identity, and σ can be recovered by reading the tuple M that produced the a‑shuffle.

