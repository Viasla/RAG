# Examples
For the pattern B=HTH, the gambling calculation gives BB=10, and therefore E(T^{HTH})=10; the absorbing Markov chain with states \emptyset, H, HT, HTH also yields an expected absorption time of 10 steps.

For the pattern B=HHH, the winnings BB equal 8+4+2=14, so the expected waiting time is E(T^{HHH})=14 tosses.

Starting with pattern A=HT and aiming for B=HTH, the calculation gives AB=4 and BB=10, hence E_{HT}(T^{HTH})=10-4=6 additional tosses needed on average.

Using the Guibas‑Odlyzko recurrence f(n)=f_p(n+1)+f_p(n+3) for HTH and summing over n gives \sum_{n\ge0}P(T>n)=10, which by the identity E(T)=\sum_{n\ge0}P(T>n) again confirms E(T^{HTH})=10.

