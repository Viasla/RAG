# Formal Definition
Definition 11.1: A state $s_i$ of a Markov chain is called absorbing if it is impossible to leave it, i.e., $p_{ii}=1$.

Definition 11.1 (continued): A Markov chain is absorbing if it has at least one absorbing state and every state can reach an absorbing state (not necessarily in one step).

Definition 11.2: In an absorbing Markov chain, any state that is not absorbing is called transient.

A state i of a Markov chain is called absorbing if the transition probability P_{ii}=1 and P_{ij}=0 for all j\neq i; equivalently, once the chain enters i it stays there with probability one. In matrix form the transition matrix can be written in canonical form \[P=\begin{pmatrix}Q & R\\0 & I\end{pmatrix}\] where the rows of R give the probabilities of moving from transient states to absorbing states, and the identity block I corresponds to the absorbing states themselves.

state absorbing, 416 of a Markov chain

