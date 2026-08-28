# Proof
The proof proceeds by expanding the conditional expectations: 
1. Start with 
$$sum_{j}E(X|F_{j})P(F_{j})=sum_{j}sum_{k}x_{k}P(X=x_{k}|F_{j})P(F_{j}).$$
2. Use the definition of conditional probability to write $P(X=x_{k}|F_{j})P(F_{j})=P(X=x_{k}	ext{ and }F_{j}	ext{ occurs})$. 
3. Switch the order of summation: 
$$sum_{j}sum_{k}x_{k}P(X=x_{k}	ext{ and }F_{j}	ext{ occurs})=sum_{k}sum_{j}x_{k}P(X=x_{k}	ext{ and }F_{j}	ext{ occurs}).$$
4. For a fixed $k$, the events $F_{j}$ form a partition of $Omega$, so 
$$sum_{j}P(X=x_{k}	ext{ and }F_{j}	ext{ occurs})=P(X=x_{k}).$$
5. Therefore 
$$sum_{k}x_{k}P(X=x_{k})=E(X).$$

