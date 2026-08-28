# Examples
The stepping‑stone model described earlier is an absorbing Markov chain: the theorem proved in Section 11.2 guarantees that with probability 1 the stones will eventually all be the same color, which corresponds to an absorbing configuration.

Example 11.13 (Drunkard’s Walk): A man walks on a four‑block stretch with corners 0,…,4. Corners 0 (home) and 4 (bar) are absorbing because the man stays there once reached. Corners 1, 2, 3 are transient. The transition matrix shown in the text makes this an absorbing chain.

Example 11.13 (drunkard’s walk with 5 blocks) is worked out explicitly: the matrices Q,R,N,t and B are computed, showing that the probability of reaching the bar before home when starting at position x equals x/5.

In the Land of Oz example (Example 11.1) the transition matrix is altered so that state R becomes absorbing, and the fundamental matrix N and the quantities Nc and NR are requested.

Exercises 1–8 ask the reader to identify absorbing Markov chains in various genetic and game‑theoretic models, to compute the fundamental matrix and related quantities, and to interpret the results.

Example 11.11 (referenced) where the probability of absorption in a state with a particular gene type equals the initial proportion of that gene type.

Student progression model with states F,1,2,3,4,G; F (flunk) and G (graduate) are absorbing, transition probabilities given by q (flunk), r (repeat), p (advance).

Mary‑John three‑card game: states are the number of cards Mary holds (0,1,2,3); transition matrix is set up as an absorbing chain, the fundamental matrix is computed, the expected number of moves and John’s winning probability are obtained.

Experiment with m equally probable outcomes: an absorbing chain with states 1,…,k (state k absorbing) yields the expected number of trials before k consecutive identical outcomes as (m^k‑1)/(m‑1).

Pollution diffusion model: areas 1,2,3 with transfer fractions q_{ij} and escape fraction q_i; adding an atmospheric absorbing state makes the system an absorbing Markov chain used to compute limiting pollution levels.

Leontief economic model: industries as states with inter‑industry coefficients q_{ij}; adding an absorbing state 0 (external demand) turns the model into an absorbing chain, allowing any external demand vector d to be satisfied.

Drunkard’s walk on n blocks (n=4,5) treated as an absorbing chain with absorbing states at the ends; expected time to absorption from position x is f(x)=x(n‑x).

Harmonic function example: any function f satisfying f(i)=∑_j p_{ij}f(j) is harmonic; for absorbing chains f=P^∞f, demonstrating that a fair game remains fair until absorption.

Coin‑toss pattern HTH waiting time: states encode the longest suffix matching the pattern; the absorbing state corresponds to pattern completion, and the expected time to absorption is obtained via the fundamental matrix.

Pattern‑matching chain for HTH: states are ∅, H, HT, HTH with transition matrix given; HTH is the absorbing state and the expected time to absorption from ∅ is 10.

Pattern‑matching chain for HHH: analogous construction yields expected absorption time 14.

Gambler’s‑ruin random walk on {0,…,N} with equal step probabilities p=q=½; states 0 and N are absorbing, and the harmonic function f(i)=i gives absorption probabilities i/N.

Stepping‑stone model (Example 11.12) is shown to be an absorbing Markov chain; the proportion of red squares evolves as a fair game and the eventual winning color’s probability equals its initial proportion.

Example 11.11 with G‑gene states: the function f(i) = proportion of G genes is harmonic, implying that the absorption probability into state (GG,GG) equals the initial G‑gene proportion.

Monte Carlo roulette (Example 6.6) forms a six‑state absorbing chain; program Absorbing Chain can compute win/lose/break‑even probabilities and expected winnings for a 1‑franc bet on red.

Penney‑ante game: absorbing states correspond to the first occurrence of pattern A or pattern B; the odds are given by Conway’s formula derived from the absorbing‑chain expectations BB‑AB and BB‑BA.

An implementation named 'AbsorbingChain (program)' appears on page 421, serving as a computational example of an absorbing Markov chain.

The term 'absorption probabilities' is listed on page 420, illustrating a typical quantitative output associated with absorbing Markov chains.

