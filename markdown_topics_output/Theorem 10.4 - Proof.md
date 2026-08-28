# Proof
The mgf of X is defined by the series g_X(t)=∑_{k=0}^∞ μ_k t^k/k! and equivalently by the integral g_X(t)=∫_{-∞}^{∞} e^{tx} f_X(x) dx.

Replacing t by iτ with τ∈ℝ gives the series g_X(iτ)=∑_{k=0}^∞ μ_k (iτ)^k/k! which converges for all τ, allowing us to define the characteristic function k_X(τ)=g_X(iτ)=∫_{-∞}^{∞} e^{iτx} f_X(x) dx.

The function k_X(τ) is the Fourier transform of f_X(x).

The Fourier transform has an inverse given by f_X(x)= (1/2π)∫_{-∞}^{∞} e^{-iτx} k_X(τ) dτ, suitably interpreted.

Because the characteristic function uniquely determines the density, the mgf, which determines the characteristic function, uniquely determines the density under the hypotheses of Theorem 10.4.

Since X is bounded, its mgf converges for all t, ensuring the above representation is valid and the inversion formula applies.

