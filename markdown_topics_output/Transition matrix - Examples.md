# Examples
In Example 11.1 the weather in the Land of Oz is modeled with three states $R$ (rain), $N$ (nice), and $S$ (snow). The one‑step transition matrix is $\mathbf P=\begin{pmatrix}1/2&1/4&1/4\\ 1/2&0&1/2\\ 1/4&1/4&1/2\end{pmatrix}$, where the first row gives the probabilities of the next day's weather given that today is rainy, the second row gives the probabilities given a nice day, and the third row gives the probabilities given a snowy day.

Example 11.2 computes successive powers $\mathbf P^1,\dots,\mathbf P^6$ for the same weather chain, showing that after six steps the distribution $(0.4,0.2,0.4)$ is essentially independent of the initial state, illustrating the regular Markov chain property.

