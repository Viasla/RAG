# Formal Definition
An ordering (permutation) D of length n is said to have r rising sequences if, when D is read from the first to the last element, it can be partitioned into r maximal consecutive subsequences each of which is strictly increasing, and no longer increasing run can be formed by joining two adjacent subsequences.

For a permutation \(\sigma\) of \(\{1,2,\dots,n\}\), a *rising sequence* is a maximal consecutive subsequence \(\sigma(i),\sigma(i+1),\dots,\sigma(j)\) such that \(\sigma(k)<\sigma(k+1)\) for all \(i\le k<j\). The total number of rising sequences in \(\sigma\) equals the number of *falls* in the inverse permutation \(\sigma^{-1}\), where a fall is a position \(k\) with \(\sigma^{-1}(k)>\sigma^{-1}(k+1)\).

