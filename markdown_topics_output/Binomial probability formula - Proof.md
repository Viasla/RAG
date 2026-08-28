# Proof
The proof constructs a full probability tree for the n trials, assigns the probability p to each success branch and q to each failure branch, and notes that the probability of any fixed path with j successes is p^j q^{n-j}. The total probability of observing j successes is obtained by summing over all \binom{n}{j} distinct paths that realize j successes, yielding b(n,p,j)=\binom{n}{j}p^j q^{n-j}.

