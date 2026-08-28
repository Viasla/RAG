# Statement
If Z is a continuous random variable with cumulative distribution function F_Z and probability density f_Z, and φ is a strictly monotone, differentiable function with inverse φ⁻¹, then the random variable X = φ(Z) has cumulative distribution function F_X(x)=F_Z(φ⁻¹(x)) and probability density function f_X(x)=f_Z(φ⁻¹(x))⋅|d/dx φ⁻¹(x)|.  In particular, for the linear transformation φ(z)=σz+µ, the inverse is φ⁻¹(x)=(x‑µ)/σ and the density simplifies to f_X(x)=f_Z((x‑µ)/σ)·(1/σ).

Theorem 5.1 provides the density of a random variable obtained by applying a monotone transformation to a continuous random variable, giving the general formula 

[
    f_{g(X)}(y)=sum_{x:g(x)=y}rac{f_X(x)}{|g'(x)|}
] 

For the specific case of squaring a symmetric continuous variable, it simplifies to 

[
    f_{X^2}(r)=egin{cases}	frac{1}{2sqrt r},igl(f_X(sqrt r)+f_X(-sqrt r)igr), & r>0,\[4pt]0, & rle0.
end{cases}


