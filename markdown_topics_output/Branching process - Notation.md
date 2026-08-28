# Notation
Z_n – number of individuals in generation n.

p_j – probability that a single individual has exactly j offspring.

m=\sum j\,p_j – expected number of offspring per individual.

f(z)=\sum p_j z^j – probability generating function of the offspring distribution.

h(z) – generating function after two generations, given by h(z)=f(f(z)).

d – extinction probability (limit of d_n as n\to\infty).

d_n – probability that the process has died out by generation n.

N – number of acquaintances (used in binomial/Poisson approximation).

m=Np – mean of the binomial/Poisson offspring distribution.

Branch, BranchingSimulation – programs used to compute d_n and to simulate the process.

