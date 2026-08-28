# Examples
In the maze example (Example 11.22), after making state 5 absorbing and forming the canonical transition matrix, the fundamental matrix N is computed as a specific 8×8 matrix.  Multiplying N by the vector c of absorbing probabilities yields the expected times to absorption for each starting state: (6,5,6,5,5,6,6).  These values illustrate the symmetry of the maze: states 1,3,7,9 all have expected time 6 to reach food, while states 2,4,6,8 have expected time 5.  The mean recurrence times for the nine states of the maze are given by the reciprocals of the stationary distribution vector w=(1/12,1/8,1/12,1/8,1/6,1/8,1/12,1/8,1/12), yielding r=(12,8,12,8,6,8,12,8,12).  Another example is the Land of Oz weather chain with stationary vector (2/5,1/5,2/5); the mean recurrence times are (5/2,5,5/2).

Exercise 1: Given the transition matrix $P=egin{pmatrix}1/2&1/2\1/4&3/4end{pmatrix}$, the fundamental matrix $Z$ is computed and the resulting mean first passage matrix $M$ is obtained using the relation $m_{ij}=(z_{jj}-z_{ij})/w_j$.

Exercise 9(b): For a random walk on a circle of circumference $n=5$ with step probabilities $p=0.5$ (clockwise) and $q=0.5$ (counterclockwise), the mean first passage matrix is computed and verified to satisfy $m_{ij}=d(n-d)$ where $d$ is the clockwise distance from state $i$ to $j$.

Exercise 7(d): In a maze with rooms as states, the expected number of steps before reaching Room 5 for the first time from Room 1 is obtained by using the mean first passage matrix; this value is the $(1,5)$ entry of $M$.

