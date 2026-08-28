# Examples
For \(n=6\) and \(k=3\), compute \(\binom{6}{3}\) as follows: start with 1, multiply by 6 (→6), divide by 1 (→6), multiply by 5 (→30), divide by 2 (→15), multiply by 4 (→60), divide by 3 (→20). The intermediate results are 6, 30, 15, 60, 20; each is an integer and none exceeds the final value 20.

For \(n=5\) and \(k=2\), the alternating computation is: 1×5=5, ÷1=5, ×4=20, ÷2=10. The intermediate integers are 5, 20, 10; the maximum intermediate value (20) is exactly twice the final value, showing that the bound “none exceed the final value” must be interpreted after each *division* step, i.e., after every complete multiplication‑division pair the result does not exceed the final binomial coefficient.

