# apex2025-11 variant

Hopper the Toad has a row of $n \geq 2$ stepping stones, numbered $1$ through $n$, with consecutive stones $1$ unit apart. She starts on stone $1$ and wants to land on each of stones $2$ through $n$ exactly once before returning to stone $1$. However, she can jump at most $5$ units at a time. Let $g(n)$ be the largest possible total distance of such a round trip, starting and ending at stone $1$. Determine the value of
\[
\lim_{n \to \infty} \frac{g(n)}{n}.
\]

**Answer:** $\dfrac{44}{9}$

Verification: `solve.py` (frontier/transfer DP over maximum Hamiltonian cycles with jumps <= k, cross-checked by brute force for small n) reproduces the original limit 14/5 for k=3 and gives 44/9 (period 9, increment 44) for k=5.
