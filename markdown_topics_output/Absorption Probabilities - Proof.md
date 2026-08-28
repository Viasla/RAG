# Proof
The proof proceeds by expanding the definition of $B_{ij}$ as a double sum over all numbers of steps $n$ and intermediate transient states $k$:

$B_{ij} = sum_{n=0}^inftysum_{k=1}^t q_{ik}^{(n)},r_{kj}$. 

Rearranging the sums gives $B_{ij} = sum_{k=1}^t igl(sum_{n=0}^infty q_{ik}^{(n)}igr) r_{kj}$. The inner sum is precisely $n_{ik}$, the $(i,k)$ entry of the fundamental matrix $N = I+Q+Q^2+cdots = (I-Q)^{-1}$.  Hence $B_{ij} = sum_{k} n_{ik} r_{kj}$, which is the $(i,j)$ entry of the product $N R$. This completes the proof.

