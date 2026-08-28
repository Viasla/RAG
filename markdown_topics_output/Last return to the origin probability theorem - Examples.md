# Examples
For m=2 (walk length 4):

- k=0 (no return after time 0): probability = u_{4}=\binom{4}{2}/2^{4}=6/16=3/8.

- k=1 (last return at time 2): probability = \frac{\binom{2}{1}\binom{2}{1}}{2^{4}} = \frac{2\cdot2}{16}=4/16=1/4.

- k=2 (last return at time 4): probability = u_{4}=3/8 (the walk ends at the origin).

These three probabilities sum to 1, as required.

For m=3 (walk length 6) and k=2:

Probability = \frac{\binom{4}{2}\binom{2}{1}}{2^{6}} = \frac{6\cdot2}{64}=12/64=3/16.

