# Proof
Starting from the gambler interpretation, the expected time to reach pattern B can be decomposed as 

BB = E(T^{A or B}) + p_A·(BB – AB),

because with probability p_A the first pattern to appear is A, after which an additional expected time of BB – AB remains until B appears. Interchanging the roles of A and B yields 

AA = E(T^{A or B}) + p_B·(AA – BA).

Subtracting the two equations eliminates the unknown E(T^{A or B}) and using p_A + p_B = 1 gives a linear system in p_A and p_B. Solving the system yields 

p_A / p_B = (BB – BA) / (AA – AB),

which is precisely Conway’s formula.

