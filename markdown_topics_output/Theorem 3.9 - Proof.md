# Proof
The proof proceeds by describing a‑unshuffles, the inverses of a‑shuffles. An a‑unshuffle distributes the cards one by one from the top of the deck onto the bottom of a labelled stacks (0,…,a‑1) with equal probability, then recombines the stacks by placing stack i on top of stack i+1. This process uniquely determines an a‑shuffle. Applying an ab‑unshuffle produces ab stacks labelled by ordered pairs (i,j) with 0\le i\le a‑1 and 0\le j\le b‑1. By sorting the deck first according to the second coordinate we obtain a b‑unshuffle, and then sorting according to the first coordinate yields an a‑unshuffle. The concatenation of the two unshuffles reproduces exactly the set of stacks produced by the original ab‑unshuffle, and the relative order of cards with the same label is preserved. Hence the two‑step unshuffle corresponds uniquely to a single ab‑unshuffle, which by inversion gives the required one‑to‑one correspondence between (a‑shuffle, b‑shuffle) pairs and ab‑shuffles. This establishes the theorem.

Start with the deck in increasing order (cards labelled 1 through n). Choose any n‑tuple M = (m_1, …, m_n) with each m_i in {0,…,a‑1}. Let n_i denote the number of occurrences of i in M for i = 0,…,a‑1.

Label the first n_0 cards of the deck with 0, the next n_1 cards with 1, and so on up to label a‑1.

The a‑shuffle corresponding to M is obtained by placing the cards that carry label i into exactly those positions of the deck whose index in M equals i; within each label class the cards retain their original increasing order.

This construction maps each M uniquely to a permutation of the deck, and every a‑shuffle can be obtained from some M, proving a bijection and hence that there are a^n distinct a‑shuffles.

