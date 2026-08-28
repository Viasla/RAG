# Intuition
The alternating scheme mimics the way prime factors cancel between the numerator and denominator of the binomial coefficient. By dividing as soon as a divisor that appears in the denominator is present in the current product, one guarantees that no fractional intermediate values arise. Because each division removes a factor that would otherwise inflate the product, the size of the running total is kept at or below the ultimate value of \(\binom{n}{k}\).

