# Variant of math500-intermediate_algebra-1166

**Problem.** Let $x,$ $y,$ and $z$ be positive real numbers. Find the minimum value of
\[\frac{(x + y + z)[(2x + 2y)^2 + (x + y + z)^2]}{xyz}.\]

**Answer.** $64$ (attained at $x = y = 1$, $z = 2$).

Method (same as original): AM-GM gives $(2x+2y)^2 \ge 16xy$ and $(x+y+z)^2 = ((x+\tfrac z2)+(y+\tfrac z2))^2 \ge 4(x+\tfrac z2)(y+\tfrac z2)$, then weighted AM-GM on the resulting sum and on $x+y+z$.

Verified by `solve.py` (exact critical-point analysis + multi-start numeric minimisation; same code reproduces the original answer 100).
