# Proof
One proof proceeds by decomposing any walk of length $2m$ according to the time $2k$ of its last return to the origin (with $0le kle m$).  The number of walks whose last return occurs at $2k$ is $inom{2k}{k}inom{2m-2k}{m-k}=2^{2m}u_{2k}u_{2m-2k}$.  Summing over $k$ gives 
$$sum_{k=0}^minom{2k}{k}inom{2m-2k}{m-k}=2^{2m}u_{2m},,$$ 
so the term $k=0$ (no return at any positive time) contributes $2^{2m}u_{2m}$ walks, i.e. probability $u_{2m}$.  An alternative proof uses the reflection (ballot) principle: the event ${S_1ge0,dots,S_{2m}ge0}$ is in bijection with walks that never hit the origin after time 0, and the ballot theorem gives exactly $inom{2m}{m}/2^{2m}$.  A third argument notes that the number of such walks equals the Catalan number $C_m=rac1{m+1}inom{2m}{m}$ multiplied by $2$, and dividing by $2^{2m}$ again yields $u_{2m}$.

