# Examples
In a queueing system where customers arrive in each small time unit with probability p, the time until the next arrival T has a geometric distribution; the probability that no customer arrives in the next k units is q^k, illustrating the memoryless property. Another example is service time: if the service time follows a geometric distribution with parameter p, the probability that service takes an additional s time units given that s has already been served is q^s, independent of the elapsed time.

The exponential density is frequently used to model the time until the next event in a Poisson process, such as the time between emissions from a radioactive source. The memoryless property for this density was demonstrated by computing \(P(T>r+s|T>r)\) and showing it equals \(e^{-\lambda s}\), which equals \(P(T>s)\).

The geometric distribution, which models the number of Bernoulli trials until the first success, shares the memoryless property: \(P(X>r+s \mid X>r) = P(X>s)\). While not explicitly derived in the given excerpt, this property is noted as shared by both the exponential and geometric distributions in the text.

