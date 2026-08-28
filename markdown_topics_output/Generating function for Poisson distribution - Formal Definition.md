# Formal Definition
The generating function for the Poisson distribution with mean $m$ is
$$h(z)=\sum_{j=0}^{\infty}\frac{e^{-m}m^j z^j}{j!}.$$

By factoring out $e^{-m}$ and recognizing the remaining series as the exponential series, the function simplifies to
$$h(z)=e^{-m}\sum_{j=0}^{\infty}\frac{(mz)^j}{j!}=e^{-m}e^{mz}=e^{m(z-1)}.$$

