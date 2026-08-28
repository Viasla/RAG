# Statement
A function (f) defined on the state space (S) of an absorbing Markov chain is called *harmonic* if it satisfies (f(i)=sum_{jin S}p_{ij}f(j)) for every state (i).  In vector notation this is (mathbf f=mathbf Pmathbf f), where (mathbf P
) is the transition matrix of the chain.

A harmonic function represents a game in which a player's fortune is (f(i)) when the chain is in state (i).  The harmonic condition means that the expected fortune after one step is equal to the fortune before the step, i.e. the game is *fair*.

For a harmonic function (f) we have (mathbf f=mathbf P^nmathbf f) for all integers (nge1).

Let (mathbf P^infty=lim_{n	oinfty}mathbf P^n).  For an absorbing chain this limit exists and has the block form (egin{pmatrix}mathbf0&mathbf B\mathbf0&mathbf Iend{pmatrix}).  A harmonic function satisfies (mathbf f=mathbf P^inftymathbf f).

If the chain starts in a transient state (i), the expected fortune at absorption is (sum_k b_{ik}f(k)), where (b_{ik}) is the entry of (mathbf B) giving the probability of absorption in absorbing state (k) when starting from (i).  This expected final fortune equals the starting fortune (f(i)).

Thus, in a finite absorbing Markov chain, a fair game defined by a harmonic function remains fair to the end: the expected final fortune equals the initial fortune.

The game of Heads or Tails with an unlimited number of plays is an example where a fair game on an infinite state space does **not** remain fair to the end: starting with one penny and playing until one has two pennies, the gambler is sure to finish one penny ahead.

