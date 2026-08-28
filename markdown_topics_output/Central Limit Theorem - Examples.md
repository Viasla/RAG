# Examples
A standard example illustrating the Central Limit Theorem is the approximation of a binomial distribution with many trials by a normal distribution.

The ratio 2/√(n c) serves as an example of de Moivre’s use of Stirling’s formula to approximate the central term of the binomial distribution.

The determination of the constant B from an infinite series is an early instance of analytic techniques applied to probability.

In simulating a binomial random variable for n ≥ 30, one can use the CLT to approximate it by a normal random variable with parameters μ = np and σ = √(npq), then round to the nearest integer.

Rolling a die n times yields distributions of the sum that become increasingly bell‑shaped as n grows, as shown by the density curves for n=10, 20, 30 in Figure 7.1.

In a simplified bridge hand model, the point count of 13 cards is the sum of 13 independent card values; the distribution of this sum approximates a bell shape, and the probability of an opening bid (point count ≥13) is computed as 0.2845.

An illustrated example is the standardized spike graph for n=270 and p=0.3; after correcting spike heights by a factor of 1/ε where ε=1/√(npq), the graph aligns closely with the standard normal density curve, as shown in Figure 9.3.  This demonstrates the theorem’s claim that the normal approximation improves as n increases.

1. Estimating the probability of exactly 55 heads in 100 tosses of a fair coin: np=50, \sqrt{npq}=5, so x_{55}=(55-50)/5=1. Then \displaystyle P(S_{100}=55)\approx\frac{\phi(1)}{5} = \frac{1}{5}\left(\frac{1}{\sqrt{2\pi}}e^{-1/2}\right)\approx0.0484, compared with the exact value 0.0485.

2. Estimating the probability that the number of heads in 100 tosses lies between 40 and 60: with mean 50 and standard deviation 5, the standardized bounds are (39.5-50)/5=-2.1 and (60.5-50)/5=2.1. The CLT gives \displaystyle P(40\le S_{100}\le60)\approx\text{NA}(-2.1,2.1)=2\,\text{NA}(0,2.1)\approx0.9642, versus the exact value 0.96480.

3. Dartmouth College example: The college wants 1050 freshmen and can accommodate at most 1060. Assuming each applicant accepts with probability p, the number of accepted students follows a binomial distribution. The CLT can be used to approximate the probability that the accepted count falls within the desired range by standardizing the binomial variable and using normal probabilities.

Exercise 1: Use the CLT to estimate probabilities for the number of heads in 100 coin tosses, including (P(S_{100}le45)), (P(45<S_{100}<55)), (P(S_{100}>63)), and (P(S_{100}<57)).  Exercise 2 applies the CLT to the distribution of heads in 200 tosses.  Exercise 4 compares Chebyshev’s inequality and the CLT for the number of heads in one million tosses, estimating probabilities for intervals (499,500)–(500,500), (499,000)–(501,000), and (498,500)–(501,500).  Exercise 5 evaluates a baseball batter’s 300 at‑bats using the CLT to decide whether a .267 average is within typical variance.  Exercise 6 uses the CLT to determine seat allocation for a train carrying 1000 passengers.  Exercise 7 examines the probability of too many acceptances at Dartmouth using the CLT.  Exercise 8 models membership arrivals at a club by treating each member’s attendance as independent Bernoulli trials and uses the CLT to solve for the total membership and the arrival probability (p).  Exercise 9 investigates limits involving binomial probabilities, including (P(A_n=0.8)), (P(0.7n<S_n<0.9n)), (P(S_n<0.8n+0.8sqrt{n})), and (P(0.79<A_n<0.81)).  Exercise 10 estimates the probability that a digit appears no more than 931 times in 10,000 random digits.  Exercise 11 uses a simulation to confirm CLT‑based confidence intervals.  Exercise 12 finds (x) such that the probability the number of heads in 400 flips lies within (200pm x) is approximately .80.  Exercise 13 applies the CLT to a defective noodle problem with 1900 items per crate.  Exercise 14 constructs 95 % confidence intervals for pie orders and determines required customer counts.  Exercise 16 uses the CLT to design a hypothesis test for an aspirin effectiveness claim, ensuring error probabilities below .01.  Exercise 17 employs the CLT to determine sample size for a poll with a .01 margin of error at 95 % confidence.  Exercise 18 discusses confidence intervals and clarifies that a 95 % confidence statement does not mean “certainly within 3 percentage points,” but that in repeated sampling about 95 % of intervals will contain the true proportion.

1.  A computational experiment using the program CLTGeneral generates a sequence of n random discrete distributions on the interval [−2, 4] and convolves them to find the distribution of S_n for n = 1, 4, and 10.  The resulting standardized distributions are plotted and compared with the standard normal density, showing a good fit when n = 10, which demonstrates the Central Limit Theorem in action. 2.  The distribution of heights of 9,593 adult women aged 21‑74 from the Health and Nutrition Examination Survey I (1971‑1974) is shown in Figure 9.10 and resembles a normal curve, illustrating an empirical example where a trait that is influenced by many independent factors (genetic and non‑genetic) follows the predictions of the CLT. 3.  In the multiple‑gene hypothesis for height, the height H of an individual is modeled as H = X_1 + X_2 + ··· + X_n + W, where each X_i represents the effect of a different gene pair and W captures non‑genetic factors.  When n is large, Theorem 9.5 guarantees that the sum X_1 + X_2 + ··· + X_n is approximately normally distributed, and if the genetic contributions dominate W, then H itself is approximately normal.

The binomial distribution with large n becomes approximately normal, as shown by Galton’s quincunx experiments.

A quincunx (Galton board) physically demonstrates that the distribution of ball positions after many rows approximates a normal distribution.

The convolution of two normal distributions, as in a two‑stage quincunx, results in another normal distribution, illustrating the additive property of normality.

In models of human height, the sum H=X_1+⋯+X_n+W of genetic and non‑genetic components is approximated by a normal distribution for large n, per the CLT.

Example 9.7: choosing (n) random numbers uniformly from ([0,1]) and summing them; as (n) increases, the density of (S_n) becomes increasingly normal and after standardization (S_n^*) has mean 0 and variance 1.
Example 9.8: choosing (n) numbers from an exponential distribution with parameter (lambda); the standardized sum again tends to a normal shape.
Exercise 1: estimating the probability that the sum of 24 dice rolls exceeds 84 or equals 84 using the CLT.
Exercise 2: estimating the probability that a random walker is more than 10 steps from the origin after 100 steps using the CLT.
Exercise 3: estimating the probability that a rope of 100 strands supports 1000 or 970 pounds, where each strand’s strength is independent with mean 10 and standard deviation 1.
Exercise 4: simulation of 1000 random digits to test the CLT by checking how often the sample mean lies within three standard deviations of the expected value 4.5.
Exercise 5: estimating probabilities for the number of dice throws needed to reach a cumulative sum of 700 using the CLT.
Exercise 6: estimating loss probabilities for a bank handling rolls of pennies, including the chance of losing more than 25 cents in 100 rolls.
Exercise 7: estimating the probability that the average of 18 height measurements falls between 199 and 201 feet.
Exercise 8: estimating (P(S_{30}=0)) for a student’s grade errors cancelling out.
Exercise 9: using the CLT to prove the Law of Large Numbers.
Exercise 10: applying the CLT and the Law of Large Numbers to understand Peter’s fortune after 10,000 penny‑matching trials.
Exercise 12: estimating the probability of net gain in 100 bets on roulette using two payoff matrices, then comparing the CLT estimates to exact probabilities 0.437 and 0.509.

1. Exercise 4 asks to approximate the densities of the sum S_{25}, its standardized sum S_{25}^*, and its average A_{25} of 25 uniformly distributed numbers on [0,20] by normal densities.  2. Exercise 5 implements a simulation with 1000 trials to plot the histogram of S_{25} and compares it with the normal approximation, then repeats for S_{25}^* and A_{25}.  3. Exercise 7 simulates 25 random numbers from [0,1] drawn from five different densities (constant, linear, quadratic, V‑shaped, and a variant of V‑shape) and compares the bar graph of the sum S_{25} with the normal density φ(x) having the same mean μ(S_{25}) and variance σ(S_{25}).  4. Exercise 9 explores the required n for normality by sampling n=3,6,12,20 from each of the densities in Exercise 7 and plotting histograms of S_n.  5. Exercise 11 treats the daily price changes X_n of a stock as independent N(0,1/4) variables and uses the CLT to approximate probabilities that the 365th day’s price Y_{365}=100+∑X_i exceeds 100, 110, or 120.  6. Exercise 13(a) uses the CLT to compute the mean and variance of the average velocity of 10^{20} particles each with N(0,1) velocity, and then asks for P(average ≥10^{−9}).  7. Exercise 14(a) applies the CLT to the average of n distance measurements with variance 16, yielding an approximate 95% confidence interval for the true distance d as A_n ± 8/√n.

1. In simulating a branching process with many offspring per generation, the Central Limit Theorem is used to replace the sum of 1000 independent experiments with a single normal experiment, as noted in the description of the BranchingSimulation program.

2. Example 10.13 compares the limiting behavior of the probability mass function of a branching process with the Central Limit Theorem for sums S_n, highlighting the similar form of the limiting expressions.

3. The text references Theorem 9.3 for the Central Limit Theorem in the context of integer‑valued independent random variables.

A Drunkard's Walk example is listed at pages 416, 419–421, 423, 427, 443; this random-walk scenario is typically used to demonstrate the Central Limit Theorem.

The index points to page 213 for the "standard normal random variable," page 264 for a "standardized random variable," and page 326 for a "standardized sum."  These entries suggest that the text discusses the normalization process used in the CLT, where sums of independent random variables are standardized to converge in distribution to a standard normal.  Page 333 is also cited for "sample mean," which is the primary object of study in many CLT applications.  These items collectively provide context for typical examples and applications of the CLT.  Additionally, page 333 is referenced for "statistics applications of the Central Limit Theorem to," implying that practical examples of the theorem are presented there.

