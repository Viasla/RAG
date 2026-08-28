# Formal Definition
If an ergodic Markov chain is started in state s_i, the expected number of steps to return to s_i for the first time is called the mean recurrence time for s_i and is denoted by r_i.

For a finite Markov chain with transition matrix P and stationary distribution w, the mean recurrence time to state i, denoted m_{ii}, is the expected number of steps required to return to i after leaving it (i.e. the first passage time from i to i).  In terms of the fundamental matrix Z, m_{ii} = z_{ii}/w_i, where z_{ii} is the ii‑th entry of Z and w_i is the i‑th entry of the stationary vector.  For an ergodic chain starting in equilibrium, the expected time until the next occurrence of state i is μ̄_i = sum_k w_k m_{ki} + w_i r_i, and this also simplifies to μ̄_i = z_{ii}/w_i.

The index lists 'mean recurrence time' with a reference to page 454 in the context of Markov chains, indicating its occurrence in the discussion of mean recurrence properties.

