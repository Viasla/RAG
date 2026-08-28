# Notation
Transient states are often collected in a set \(T\) and ordered first when the transition matrix is written in canonical form. In that form the submatrix \(Q\) contains the transition probabilities among transient states, while \(R\) contains probabilities from transient to absorbing states.

\mathbf{Q} denotes the sub‑matrix of transition probabilities among transient states.

\mathbf{N}= (I-\mathbf{Q})^{-1} is the fundamental matrix, giving the expected number of visits to each transient state before absorption.

\mathbf{t}=\mathbf{N}\mathbf{c} is the column vector of expected times to absorption, where \mathbf{c} is a column of ones.

\mathbf{R} is the sub‑matrix of transition probabilities from transient to absorbing states.

\mathbf{B}=\mathbf{N}\mathbf{R} gives the absorption probabilities for each starting transient state.

