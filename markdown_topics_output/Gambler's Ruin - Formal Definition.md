# Formal Definition
Let X_k be independent Bernoulli random variables with P(X_k=1)=p and P(X_k=-1)=q=1-p. Define S_n = \sum_{k=1}^n X_k with S_0=0. The gambler’s ruin problem asks for the distribution of the hitting time T = \min\{n\ge1:S_n=1\}\, subject to the condition that S_k\le0 for 1\le k<T. The probability mass function of T is r_n = P(T=n).

Consider a Markov chain with state space {0,1,…,N}. From any transient state i∈{1,…,N−1} the chain moves to i+1 with probability p and to i−1 with probability q=1−p. States 0 and N are absorbing, i.e., once the chain enters either of these states it stays there forever. The quantity b_{iN} denotes the probability that, starting from state i, the chain is eventually absorbed in state N rather than state 0.

