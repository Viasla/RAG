# Formal Definition
Definition 11.1: A state $s_i$ of a Markov chain is called absorbing if $p_{ii}=1$, i.e., it is impossible to leave that state. A Markov chain is absorbing if (i) it has at least one absorbing state, and (ii) from every state it is possible to reach an absorbing state (not necessarily in one step).

Definition 11.2: In an absorbing Markov chain, any state that is not absorbing is called transient.

An absorbing Markov chain is a Markov chain whose transition matrix can be written in canonical form \(\displaystyle P=\begin{pmatrix} I & 0\\ R & Q\end{pmatrix}\) where I is the identity matrix on the absorbing states, Q contains the transition probabilities among the transient states, and R contains the transition probabilities from transient to absorbing states. The fundamental matrix is defined as N=(I-Q)^{-1}. The absorption‑probability matrix is B=N R and the vector of expected times to absorption is t=N\mathbf{c} with \mathbf{c} a column vector of ones.

An absorbing Markov chain is a Markov chain that possesses at least one absorbing state (a state that, once entered, cannot be left) and from every transient state there is a non‑zero probability of eventually reaching an absorbing state. In the gambler’s ruin problem the chain has state space {0,1,…,T} with 0 and T absorbing states.

In the experiment of finding k consecutive identical outcomes the chain is defined with states 1,…,k where state i represents a current run of length i; state k is absorbing.

An absorbing Markov chain is a Markov chain that possesses at least one absorbing state— a state s such that the transition probability p_{ss}=1, i.e., once entered the process remains in s for all subsequent steps. In the gambler’s‑ruin example, states 0 and N are absorbing because "if the walker ever reaches 0 or N he stays there."

The transition matrix presented for the pattern‑matching chain has a row (HTH) that leads only to the absorbing state, embodying the formal structure of an absorbing chain.

The index references a 'canonical form of an absorbing Markov chain' on page 416, implying that such a chain can be represented in a standard matrix form.

