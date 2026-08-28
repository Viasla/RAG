# Examples
X_i, i=1,2,3,4, represent the values of four successive rolls of a die, and the sum X_1+X_2+X_3+X_4 is a random variable representing the total.

X denotes the random variable representing a single die roll, with possible values 1\text{–}6 each having probability 1/6 in the fair die case.

Y denotes the random variable representing a coin toss with outcomes H and T, each assigned probability 1/2 in the fair coin case.

In a drug effectiveness scenario, the random variable may take the value "effective" with probability 0.3 and "not effective" with probability 0.7.

The program RandomNumbers generates random real numbers in [0,1], and the mapping \lfloor6r\rfloor+1 produces a random integer between 1 and 6, which can be treated as a random variable with a specified distribution.

Bernoulli trials use a random variable to model the number of heads in repeated coin tosses, where each toss is represented by a binary random variable with probability p of heads.

Example 1.6: Rolling a fair six‑sided die, the random variable X takes values in {1,2,3,4,5,6}.  Each outcome has probability 1/6, so the event E of an even result is {2,4,6} with probability 1/2.  The distribution function is m(i)=1/6 for i=1,…,6.  Example 1.7: Tossing a fair coin twice and recording the outcomes as a string of heads and tails, the sample space is {HH,HT,TH,TT} with each outcome equally likely (m=1/4).  An alternative representation records only the number of heads, giving the sample space {0,1,2} with appropriate probabilities.  Example 1.8: Continuing Example 1.6, the probability of the event that the die shows a number in {2,4,6} is computed by summing the corresponding m(ω).  Example 1.9: An election among candidates A,B,C where A and B have equal chance and C has half that chance.  The sample space is {A,B,C} and the distribution satisfies m(A)=m(B)=2m(C) with m(A)+m(B)+m(C)=1.

Random integer (page 39).

Random number generator (page 2).

Random walk (page 471).

Random process (page 128).

Random permutation program (page 3).

Joint random variable (page 142).

