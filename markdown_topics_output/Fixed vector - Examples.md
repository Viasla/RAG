# Examples
In the Land of Oz example the limiting vector w = (0.4, 0.2, 0.4) is obtained by solving wP = w together with w1+w2+w3=1, illustrating a concrete fixed row vector for a regular chain.

Example 11.20 shows how to compute the same fixed row vector by setting w1 = 1, solving the reduced linear system from wP = w, and then normalising the resulting vector (1, 1/2, 1) to obtain the probability vector (0.4, 0.2, 0.4).

For the vowel‑consonant chain studied by Markov, the transition matrix \[\begin{pmatrix}.128&.872\\ .663&.337\end{pmatrix}\] has fixed vector (0.432,0.568), predicting that about 43.2 % of the letters in the novel are vowels and 56.8 % are consonants, which matches the actual counts.

Exercise 7(c) asks the reader to find the fixed vector of the maze‑room Markov chain; the solution, though not given in the text, would be the unique probability vector w satisfying wP = w for that particular transition matrix.

