# Notation
(p) – probability of winning one dollar on a single play.
(q=1-p) – probability of losing one dollar.
(T) – target fortune; upper absorbing boundary.
(x) – initial fortune; state variable.
(w_i) – probability that the gambler eventually reaches (T) before 0 when starting from state (i).  The absorbing Markov chain transition matrix (P) has entries (P_{i,i+1}=p), (P_{i,i-1}=q) for (1le ile T-1); (P_{0,0}=P_{T,T}=1).  The recurrence relation is (w_i=Pw_{i+1}+qw_{i-1}).

$p$: probability of winning a single game (move +1). $q$: probability of losing a single game (move –1), with $p+q=1$. $M$: upper absorbing boundary (target capital). $s$: initial stake, often denoted $z$ in the derivations. $q_k$: probability that the gambler’s capital hits 0 before reaching $M$ when starting from $k$. $p_k$: probability that the capital reaches $M$ before 0 (i.e., survival probability).

