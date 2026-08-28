# Proof
It is straightforward to show that the convolution is associative. Since (m1 * m2)(j) = Σk m1(k)m2(j−k), then ((m1 * m2) * m3)(j) = Σℓ (m1 * m2)(ℓ)m3(j−ℓ) = Σℓ Σk m1(k)m2(ℓ−k)m3(j−ℓ). Reindexing the double sum (e.g., let t=ℓ−k) gives the same expression as (m1 * (m2 * m3))(j), proving associativity. This follows from the commutativity and distributivity of summation over integers.

