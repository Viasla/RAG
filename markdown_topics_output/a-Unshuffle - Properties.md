# Properties
There are exactly a^n distinct a‑shuffles of an n‑card deck, and consequently there are a^n distinct a‑unshuffles.

The probability that, in an a‑shuffle, the first card (card number 1) ends up in the i‑th position is 
$$
\frac{(a-1)^{i-1}a^{n-i}+(a-2)^{i-1}(a-1)^{n-i}+\cdots+1^{i-1}2^{n-i}}{a^n}.
$$

For a 2‑unshuffle (riffle shuffle) on a 52‑card deck, the probability that the first card lies in the first half after three riffle shuffles can be estimated computationally; after seven riffle shuffles this probability becomes very close to 1/2, reflecting rapid mixing.

The a‑unshuffle coding preserves the relative order of cards within each pile, which means that the a‑unshuffle is a stable sorting operation with respect to the original labeling.

Repeated application of a‑unshuffles until all labels become distinct requires at least \lceil\log_2(n)\rceil unshuffles for the case a = 2, as shown in Exercise 5.

