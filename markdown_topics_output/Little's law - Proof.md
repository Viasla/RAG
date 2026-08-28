# Proof
Little's law can be derived by an equilibrium argument: when a customer joins the queue he expects to find on average N people ahead of him, and after he leaves he expects to find λ T people behind him.  In equilibrium these two numbers must be equal, yielding N = λ T.  The text indicates that a formal proof is not given here but may be found in Ross; a reference to the literature is provided as footnote 24.

The queue length distribution in equilibrium is geometric with probabilities s_j=(1-ρ)ρ^j for j=0,1,2,… when ρ<1. The expected queue size is the mean of this distribution, N=ρ/(1-ρ). Applying Little's result N=λT gives T=N/λ=ρ/(λ(1-ρ)), which simplifies algebraically to 1/(μ-λ). Thus the expected waiting time in an M/M/1 queue is T=1/(μ-λ).

