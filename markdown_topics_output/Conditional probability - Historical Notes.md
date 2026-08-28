# Historical Notes
The concept of conditional probability is introduced through concrete examples such as a die roll, a life‑table of female longevity, and a voting scenario, illustrating early practical uses before formalization.

The term “Bayes probability” is introduced later, linking conditional probability to Thomas Bayes’ work on inverse probabilities, and the Monty Hall problem is cited as a modern revival of conditional reasoning.

In the continuous setting conditional probability is defined using a conditional density function that is zero outside the conditioning event and normalized to integrate to one over that event. The text shows this definition with a general density f(x) and event E, leading to f(x|E)=f(x)/P(E) for x∈E and 0 otherwise, a formulation that mirrors the discrete case but with integrals. The memoryless property of the exponential distribution is introduced as an important example of a conditional probability property: given no emission in r seconds, the probability of waiting an additional s seconds is e^{-lambda s}, independent of r. This property is derived via the conditional probability formula P(F|E)=P(F∩E)/P(E). The text also connects conditional probability to practical scenarios such as search problems (p_i increase, q_i decrease) and the Monty Hall problem, highlighting its relevance in decision-making and inference.

