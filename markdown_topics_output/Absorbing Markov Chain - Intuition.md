# Intuition
An absorbing state is a state that, once entered, cannot be left (its self‑transition probability equals 1). An absorbing Markov chain therefore consists of at least one such “sticky’’ state together with other states that eventually “drift’’ into one of the absorbing states. The process is said to be “absorbed’’ when it first reaches an absorbing state, after which it remains there forever.

In an absorbing Markov chain the process eventually enters a state that, once reached, cannot be left. The matrices Q and R describe, respectively, transitions among transient states and transitions from transient to absorbing states, while the fundamental matrix N gives the expected number of visits to each transient state before absorption. Multiplying N by the column vector of ones yields the expected time to absorption (t), and N R yields the absorption probabilities (B).

The process can be visualized as a random walk that eventually gets trapped in an absorbing state, analogous to a game that ends when a player either wins all money or loses everything.

In the gene‑type absorption example the number of genes of a particular type behaves like a fair game; the probability of eventual absorption in a state with that gene type equals the initial proportion of that type.

The gambling interpretation treats each arrival of a gambler as a unit of cash taken by the casino (1 dollar) and the only payouts occur when the target pattern B is completed; because each bet is perfectly fair, the casino’s expected intake must equal its expected payout, leading directly to the expected time to absorption being equal to the total payout BB.

In the random‑walk model on {0,…,N} with absorbing endpoints, the intuition is that once the walk hits 0 or N it stays there forever, so the long‑run behavior is determined entirely by the probability of absorption at each endpoint, which can be computed via harmonic functions.

