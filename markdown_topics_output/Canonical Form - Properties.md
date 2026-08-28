# Properties
The canonical form separates transient and absorbing behavior, allowing the use of matrix algebra (e.g., computing (I‑Q)^{-1}) to find absorption probabilities and expected times to absorption.

The canonical form isolates the absorbing behaviour of the chain, allowing the absorption probabilities to be computed as the product \(\mathbf{B}=\mathbf{N}\mathbf{R}\).  The fundamental matrix \(\mathbf{N}\) exists because \(\mathbf{I}-\mathbf{Q}\) is invertible for an absorbing chain, and its entries give the expected number of visits to each transient state before absorption.  Multiplying \(\mathbf{N}\) by the column vector of ones yields the expected time to absorption from each transient state (the vector \(\mathbf{t}\)).  The first row of \(\mathbf{B}\) directly provides the probabilities of being absorbed in each absorbing state when the chain starts in the corresponding transient state.

