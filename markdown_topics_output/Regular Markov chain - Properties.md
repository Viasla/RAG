# Properties
If a chain is regular, some power P^k has all positive entries, guaranteeing that every state is reachable from every other state in k steps.

For a regular chain, the limit \lim_{n\to\infty} P^n exists and has identical rows, providing a unique stationary distribution.

Regular chains are a proper subset of all Markov chains; not all chains are regular.

The convergence to the limiting matrix is independent of the initial probability vector; any initial distribution multiplied by P^n converges to the same stationary distribution as n→∞.

Every regular chain is ergodic (i.e., it is possible to reach any state from any other state), but the converse need not hold.

For a regular chain, the sequence of powers P^{n} converges to a matrix W whose rows are all identical to the strictly positive probability vector w.

The stationary distribution w is unique among probability vectors: any row vector v with vP = v must be a scalar multiple of w, and after normalisation it coincides with w.

The column vector c of ones is the unique (up to scalar) right eigenvector associated with eigenvalue 1: any column vector x with Px = x is a multiple of c.

All entries of w are strictly positive, reflecting the fact that every state is visited with positive long‑run frequency.

The convergence to W is exponential in n for regular chains, as illustrated by the rapid approach of P^{6} to W in the Land of Oz example.

