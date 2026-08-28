# Examples
Example 6.29 applies Little's law to a queue where arrivals occur at rate λ and service times are exponentially distributed with rate μ.  When the traffic intensity ρ = λ/μ is less than 1, the expected queue length N and the expected waiting time T are finite, and Little's law provides the relationship N = λ T.  The example also notes that in simulation (Figure 6.8) the relationship holds, with the queue length distribution estimated by simulation and the waiting times tracked.

Simulation example: arrival rate λ=1 and service rate μ=1.1, giving ρ=1/1.1=10/11. The expected queue size N=ρ/(1-ρ)=10, and the expected waiting time T=1/(μ-λ)=10. The observed simulation averages were 8.19 for queue size and 7.37 for waiting time, close to the theoretical values. The waiting time histogram was exponential with parameter μ-λ, confirming the theoretical distribution.

