# Statement
The Fundamental Limit Theorem appears as section 11.4 in Grinstead and Snell’s 'Introduction to Probability', positioned within the Markov Chains chapter.

The Fundamental Limit Theorem for Regular Markov Chains states that if $\mathbf{P}$ is a regular transition matrix then $$\lim_{n\to\infty}\mathbf{P}^{n}=\mathbf{W},$$ where $\mathbf{W}$ is a matrix whose each row is the unique fixed probability row vector $\mathbf{w}$ for $\mathbf{P}$, and all entries of $\mathbf{W}$ are strictly positive.

It also follows that each column of $\mathbf{P}^{n}$ converges to the same constant vector, i.e. $\mathbf{P}^{n}\mathbf{y}$ tends to a constant vector for any column vector $\mathbf{y}$.

Let $P$ be the transition matrix of a regular Markov chain with state space ${s_1,dots ,s_r}$ and let $w$ be the unique probability vector satisfying $wP=w$.  Then the limit $displaystyle lim_{n	oinfty}P^n$ exists and equals a matrix $W$ whose every row is the vector $w$.  Consequently, for any initial probability vector $u$, $uP^n	o w$ as $n	oinfty$.  Equivalently, for every column vector $y$ the limit $lim_{n	oinfty}P^ny$ is the constant vector $umathbf{1}$ where $u$ is the common value of all components of the limit vector.

The Fundamental Limit Theorem for Regular Markov Chains is cited in the index as appearing on page 448 of the source text and is associated with a fundamental matrix discussed on page 419.

