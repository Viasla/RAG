# Notation
$s_i$ denotes a state of the chain.

$p_{ii}$ denotes the one‑step transition probability from state $i$ back to itself.

An absorbing state satisfies $p_{ii}=1$; transient states have $p_{ii}<1$ and can move to other states.

R – the matrix of transition probabilities from transient states to absorbing states;\nQ – the sub‑matrix of transitions among transient states;\nN=(I-Q)^{-1} – the fundamental matrix, giving expected numbers of visits to transient states;\nB=N\,R – the matrix of absorption probabilities;\nt – the column vector of expected times to absorption, obtained as t=N\mathbf{1};\nc – the column vector of ones used in the definition of t.

