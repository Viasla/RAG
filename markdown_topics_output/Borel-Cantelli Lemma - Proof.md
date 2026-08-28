# Proof
Step 1: For any (rinmathbb{N}) the probability that none of the events ({A_i : i>r}) occur is bounded by (mathbb{P}(igcap_{i>r}A_i^c)le e^{-sum_{i=r}^{infty}a_i}), obtained using the inequality (xle e^{-x}) and the independence of the events.
Step 2: If (sum_{i=1}^{infty}a_i) diverges, then for each (r) the tail sum (sum_{i=r}^{infty}a_i) also diverges to (+infty) as (r	oinfty). Consequently (lim_{r	oinfty}e^{-sum_{i=r}^{infty}a_i}=0). Thus (mathbb{P}(	ext{no }A_i 	ext{ with }i>r	ext{ occur})	o 0.
Step 3: The event that infinitely many (A_i) occur is the complement of the event that only finitely many occur. The probability that only finitely many occur is (lim_{r	oinfty}mathbb{P}(	ext{no }A_i 	ext{ with }i>r	ext{ occur})=0.
Step 4: Therefore (mathbb{P}(	ext{infinitely many }A_i	ext{ occur})=1.


The proof also relies on the fact that the events are independent; without independence the inequality in Step 1 would not hold.

