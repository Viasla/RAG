# Proof
The moment generating functions of X and Y are g_X(t)=(p,e^t+q)^n and g_Y(t)=(p,e^t+q)^n, where q=1-p. Independence implies g_Z(t)=g_X(t)g_Y(t)=(p,e^t+q)^{2n}. This is the moment generating function of a Bin(2n,p) random variable, since the general form of the mgf of Bin(m,p) is (p,e^t+q)^m. Consequently, the probability mass function of Z is p_Z(j)=rac{1}{j!}h_Z^{(j)}(0)=inom{2n}{j}p^jq^{2n-j}, obtained by expanding (p,z+q)^{2n} as an ordinary generating function. The same conclusion follows by noting that the ordinary generating functions satisfy h_Z(z)=h_X(z)h_Y(z)=(p,z+q)^{2n}.

