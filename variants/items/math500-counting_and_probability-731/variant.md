# Variant of math500-counting_and_probability-731

**Problem.** Equilateral triangle $PQR$ has center $O$. A point is chosen uniformly at random from the interior of triangle $PQR$. What is the probability that it is closer to $O$ than to any of the three vertices $P$, $Q$, $R$?

**Answer.** $\frac{2}{3}$

(Verified by solve.py: exact half-plane clipping gives 2/3, Monte Carlo 0.6634; the same code reproduces 1/2 for the original rectangle at k = 5/2, 1, 3, 7/4.)
