# Notation
The transition probability from state $i$ to state $j$ is denoted $p_{ij}$. An absorbing state satisfies $p_{ii}=1$ and $p_{ij}=0$ for $j
eq i$. In the canonical form of an absorbing chain, the transition matrix is partitioned as \[P=\begin{bmatrix}I_r & 0\\ R & Q\end{bmatrix}\] where $I_r$ is the $r\times r$ identity matrix for the $r$ absorbing states, $Q$ is the $t\times t$ matrix of transition probabilities among the $t$ transient states, and $R$ is the $t\times r$ matrix of probabilities of moving from transient to absorbing states.

P – full transition matrix in canonical form.

I – identity matrix on absorbing states.

Q – submatrix of transitions among transient states.

R – submatrix of transitions from transient to absorbing states.

N – fundamental matrix, N=(I-Q)^{-1}.

B – absorption‑probability matrix, B=NR.

t – column vector of expected times to absorption, t=Nc.

c – column vector of ones.

\mathbf{B} – sometimes used for the same absorption matrix.

\mathbf{N} – sometimes used for the same fundamental matrix.

Transition matrix P is partitioned as P=[[Q,R],[0,I]], where Q contains transition probabilities among transient states, R from transient to absorbing, and I is the identity on absorbing states. The limiting matrix P^∞=[[0,B],[0,I]] with B=(I−Q)^{-1}R.

Fundamental matrix N=(I−Q)^{-1} gives the expected number of visits to each transient state before absorption.

T^B – the total number of gamblers (or time steps) taken until pattern B occurs; it equals the expected time to absorption when the chain starts from the empty state.

AB – the total amount won by gamblers who arrived while pattern A was present before pattern B occurs.

BB – the total amount paid to gamblers when pattern B finally occurs; also equals the expected absorption time for the chain that models pattern B.

f(i) – the proportion of G genes (or a harmonic function) evaluated at state i; used to compute absorption probabilities.

b_{iN} – the probability of being absorbed in state N when the random walk starts at i.; expressed as i/N for p=q or via a geometric formula for p≠q.

B – the expected time to reach a particular pattern; in the examples B=10 for HTH and B=14 for HHH.

β_{ij} – the probability of absorption in absorbing state j when starting from transient state i; assembled into matrix B = N R in the standard absorbing‑chain decomposition.

The phrase 'absorbing Markov chain' is used as the standard terminology for this class of stochastic processes.

