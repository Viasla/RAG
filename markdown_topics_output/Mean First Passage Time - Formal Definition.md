# Formal Definition
**Definition 11.7.**  If an ergodic Markov chain is started in state $s_i$, the expected number of steps to reach state $s_j$ for the first time is called the *mean first passage time* from $s_i$ to $s_j$.  It is denoted by $m_{ij}$.  By convention $m_{ii}=0$.

For a discrete‑time Markov chain with transition matrix P, let m_{ij} denote the mean first passage time from state i to state j.  For i\neq j, m_{ij} is the expected number of transitions required for the chain to reach j for the first time when it starts in i.  For i=j the quantity reduces to the mean recurrence time, which can be expressed as 1/w_i where w_i is the stationary probability of state i.  Using the fundamental matrix Z, the mean first passage times satisfy the formula m_{ij}=\frac{z_{jj}-z_{ij}}{w_j}, which in the text appears as m_{ki}=\frac{z_{ii}-z_{ki}}{w_i}.

