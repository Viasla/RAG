# Examples
In Example 11.13 (the Drunkard’s Walk), states 1,2,3 are transient and states 0,4 are absorbing; after ordering the transient states first, the transition matrix takes the canonical block form described above.

From the canonical form the author writes \(\mathbf{R}=\begin{array}{cc}&0&4\\1&1/2&0\\2&0&0\\3&0&1/2\end{array}\).  Using the previously computed fundamental matrix \(\mathbf{N}=\begin{pmatrix}3/2&1&1/2\\1&2&1\\1/2&1&3/2\end{pmatrix}\) the absorption matrix is obtained as \(\mathbf{B}=\mathbf{N}\mathbf{R}=\begin{pmatrix}0&4\\2&1/2\\3&1/4&3/4\end{pmatrix}\).  The first row of \(\mathbf{B}\) shows that, starting from state 1, the probability of absorption in state 0 is \(3/4\) and in state 4 is \(1/4\).

The program *Absorbing Chain* is applied to the drunkard’s walk with five blocks.  The canonical matrices computed are: \(\mathbf{Q}=\begin{bmatrix}1&2&3&4\\2&0.0&0.50&0.00&0.00\\3&0.0&0.50&0.00&0.50\\4&0.0&0.00&0.50&0.00\end{bmatrix}\), \(\mathbf{R}=\begin{bmatrix}1&0.50&0.00\\2&0.00&0.00\\3&0.00&0.00\\4&0.00&0.50\end{bmatrix}\), \(\mathbf{N}=\frac13\begin{pmatrix}1.60&1.20&0.80&0.40\\1.20&2.40&1.60&0.80\\0.80&1.60&2.40&1.20\\0.40&0.80&1.20&1.60\end{pmatrix}\), \(\mathbf{t}=\frac13\begin{pmatrix}4.00\\6.00\\6.00\\4\end{pmatrix}\), and \(\mathbf{B}=\frac13\begin{pmatrix}0.80&0.20\\0.60&0.40\\0.40&0.60\\0.20&0.80\end{pmatrix}\).

