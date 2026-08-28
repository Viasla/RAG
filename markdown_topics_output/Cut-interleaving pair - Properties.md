# Properties
The total number of cut‑interleaving pairs for an a‑shuffle on n cards is a^n, since each of the n positions can be assigned any of the a stack labels independently.

For a given ordering D with r rising sequences, the number of cut‑interleaving pairs that produce D under an a‑shuffle is \binom{n+a-r}{n}.

The mapping from cut‑interleaving pairs to permutations is many‑to‑one; the multiplicity for ordering D is exactly the count given in the previous property, and the probability of D under an a‑shuffle is that multiplicity divided by a^n.

Cut‑interleaving pairs provide a concrete combinatorial encoding of shuffles: the pair corresponds to an n‑digit base‑a integer, establishing a one‑to‑one correspondence between S_a and the set of such integers.

Composing an a‑shuffle with a b‑shuffle yields a bijection between S_{a,b} and S_{ab}; consequently the probability distribution on permutations after the two‑step process equals that after a single ab‑shuffle.

