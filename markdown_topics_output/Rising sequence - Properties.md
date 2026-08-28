# Properties
The number of cut‑interleaving pairs that yield a given ordering D with r rising sequences under an a‑shuffle is  Σ_{a,r}= {n+a-r choose n}.

The probability assigned to D by an a‑shuffle equals Σ_{a,r}/a^{n}.

The Eulerian numbers satisfy  a^{n}=\sum_{r=1}^{a}{n+a-r \choose n}A(n,r)  (Theorem 3.12).

From the previous identity one obtains the recursion  A(n,a)=an-\sum_{r=1}^{a-1}{n+a-r \choose n}A(n,r) .

A(n,1)=1 because the only permutation with a single rising sequence is the identity ordering.

The number of rising sequences in \(\sigma\) equals the number of falls in \(\sigma^{-1}\).

For an \(a\)-shuffle of an \(n\)-card deck, the probability that the resulting ordering has exactly \(r\) rising sequences (with \(1\le r\le a\)) is
$$\frac{\binom{n+a-r}{n}}{a^{n}}\,A(n,r).$$

The number of rising sequences in any permutation lies between 1 (the identity) and \(n\) (the reverse order).

The maximum possible number of rising sequences after an \(a\)-shuffle is \(a\); an \(a\)-shuffle cannot produce more than \(a\) rising sequences.

