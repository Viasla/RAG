# Formal Definition
A Markov chain is described by a finite set of states $S=\{s_1,s_2,\dots,s_r\}$ together with transition probabilities $p_{ij}=P\{\text{next state}=s_j\mid\text{current state}=s_i\}$ that do not depend on earlier states; the collection $P=(p_{ij})$ is called the transition matrix. For $n\ge1$, the $n$‑step transition probability $p^{(n)}_{ij}=P\{\text{state}=s_j\text{ after }n\text{ steps}\mid\text{state}=s_i\text{ now}\}$ satisfies $p^{(n)}_{ij}=\sum_{k=1}^r p_{ik}p^{(n-1)}_{kj}$, and in matrix form $P^n$ gives all $n$‑step probabilities.

An absorbing Markov chain is a discrete‑time stochastic process with a finite state space in which at least one state is absorbing (once entered it is never left) and all other states are transient.

For the pattern HTH the state space is {∅,H,HT,HTH} where HTH is absorbing; the one‑step transition probabilities are given by the matrix shown in the text, e.g. P(∅→H)=½, P(H→HT)=½, P(HT→HTH)=½, etc.

The expected time to absorption when starting from a transient state s is E_s(T)=∑_{n≥0}P_s(T>n), which for the chain above equals the amount BB defined by the gambling scheme.

The source text does not provide an explicit formal definition of a Markov chain.

