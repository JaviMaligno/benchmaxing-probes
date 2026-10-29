# Variant of math500-counting_and_probability-870

**Problem.** Six points, $P$, $Q$, $R$, $S$, $T$, and $U$, are chosen randomly and independently on the circumference of a circle. What is the probability that the segments $PQ$, $RS$, and $TU$ intersect each other pairwise (every two of the three segments cross)?

**Answer.** $\frac{1}{15}$

Verified by `solve.py` (exact enumeration of all 720 cyclic orderings, plus Monte Carlo ≈ 0.0665); the same code gives 1/3 on the original problem.
