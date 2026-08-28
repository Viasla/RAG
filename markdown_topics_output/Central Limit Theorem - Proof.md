# Proof
While many formal proofs of the Central Limit Theorem are available, the book presents a graphical illustration that serves as a more convincing demonstration of the theorem.

Using Stirling’s formula n!∼√(2πn)(n/e)^n, de Moivre derived that the ratio of the middle term of the binomial distribution to the sum of all terms is approximately 2/√(n c), where c is the circumference of the unit circle (c=2π).  This demonstrates that the central term behaves like the density of the normal distribution at its peak.

The constant B from an infinite series was identified by de Moivre as √c; substituting this into the binomial approximation yields the correct normalizing factor for the limiting normal distribution.

The proof uses Stirling's approximation for factorials: n!∼√(2πn)n^ne^{‑n}.  For x=0 one obtains ∞_{n→∞} sqrt{npq},b(n,p,⟨np⟩)=1/√(2π).  The general case follows by similar manipulation of the binomial coefficient and the exponential terms.  Thus the limit equals the standard normal density.

The proof demonstrates that the scaled binomial mass function converges pointwise to the Gaussian density, and since the total mass is preserved, the convergence holds in distribution, yielding the Central Limit Theorem for Bernoulli trials.

The proof follows from adding together the approximations to the binomial probabilities given in Theorem 9.1. Each individual binomial probability b(n,p,k) is approximated by \frac{\phi(x_k)}{\sqrt{npq}}, where x_k=(k-np)/\sqrt{npq}. Summing these approximations over all k between a*\sqrt{npq}+np and b*\sqrt{npq}+np yields a Riemann sum that converges to the integral of the standard normal density \phi(x) on [a,b] as n\to\infty. Thus the limit of the cumulative binomial probability equals the normal area. The theorem is also a special case of the more general Central Limit Theorem.

De Moivre’s original proof used the factorial approximation (n!approx sqrt{2pi n},n^n e^{-n}) (Stirling’s formula) to derive an approximate expression for the binomial coefficient (inom{n}{k}).  By manipulating this expression and applying the standardization of the binomial variable, he arrived at an approximation that matches the density of a normal distribution.  While the text does not provide a full modern proof, it notes that the CLT also follows from more general arguments applicable to any independent trial process with finite variance.

The text does not provide a detailed proof of Theorem 9.5.  It states that the uniform boundedness condition |X_n| ≤ A for all n, and the divergence of s_n to infinity, are necessary for the conclusion to hold, referencing Exercise 15 for justification of the latter condition.

The central limit theorem establishes that standardizing the distribution of S_n and height‑correcting it produces a distribution that is very well approximated by the standard normal density when n is large.  The rigorous proofs rely on characteristic functions or moment generating functions, but the key conclusion is convergence in distribution to N(0,1).

The excerpt does not contain a full proof of the CLT.  It states that the result will be shown in this section for continuous independent trials and indicates that the proof may follow from characteristic functions or other standard arguments.

The text does not include a formal proof of the Central Limit Theorem.  The exercises are designed to provide empirical support via simulation rather than a theoretical derivation.  Consequently, no proof details are extracted.

No proof of the Central Limit Theorem is presented in the supplied text.

