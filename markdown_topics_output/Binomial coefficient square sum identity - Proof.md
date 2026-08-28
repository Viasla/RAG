# Proof
Let an urn contain (n) red balls and (n) blue balls.  Any way of selecting (n) balls from the urn can be described by the number (j) of red balls chosen, where (j) can range from (0) to (n).  For a fixed (j) there are \(\binom{n}{j}\) ways to select (j) red balls and \(\binom{n}{n-j}=\binom{n}{j}\) ways to select the remaining (n-j) blue balls.  Hence, for each (j) the number of selections with exactly (j) red balls is \(\binom{n}{j}^{2}\).  Summing over all possible (j) gives 
\(\displaystyle \sum_{j=0}^{n}\binom{n}{j}^{2}\).  On the other hand, the total number of ways to choose any (n) balls from the (2n) balls in the urn is 
\(\binom{2n}{n}\).  Because both expressions count the same set of selections, they are equal, proving the identity.

Rewrite the sum as ∑_{k=0}^n {n choose k}{n choose n-k}. This is the coefficient of x^n in the product (1+x)^n(1+x)^n = (1+x)^{2n}. Therefore the coefficient equals {2n choose n}.

Thus ∑_{k=0}^n {n choose k}^2 = {2n choose n}.

