# aime25-24 variant

**Problem.** Let $g(x) = \sin\left(8\pi \cdot \sin(6x)\right)$. There are $n$ values of $x$ in the open interval $0 < x < 2\pi$ for which $g(x) = 0$. At exactly $t$ of these $n$ values, the graph of $y = g(x)$ is tangent to the $x$-axis. Find $n + t$.

**Answer.** 203  ($n = 191$, $t = 12$)

Verified by `solve.py` (exact root enumeration + independent dense-grid crossing count; the same code reproduces the original answer 149 for $\sin(7\pi\sin 5x)$).
