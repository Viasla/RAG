# Intuition
The result is a consequence of the fact that each trial has m equally likely outcomes, so the probability of a particular outcome is 1/m.  A run of k successes can be viewed as a state in a Markov chain where the state number indicates how many consecutive successes have just occurred.  As the chain progresses, the only way to increase the state is to observe the desired outcome, while any other outcome resets the state to 1.  The expected time to absorption (reach state k) therefore grows geometrically with k and m.

