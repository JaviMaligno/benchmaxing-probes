# hmmt2025-17 — variant

**Problem.** Compute the number of ways to arrange $3$ copies of each of the $24$ letters of the Greek alphabet in a row such that for any two distinct letters $y_1$ and $y_2$, the number of $y_2$'s strictly between the first and second occurrences of $y_1$ equals the number of $y_2$'s strictly between the second and third occurrences of $y_1$.

**Answer.** $2^{23}\cdot 24!$ (= 5204698426366666226930810880000)

Verified by `solve.py`: brute force for n = 1..5 letters matches n!·2^(n-1); same formula reproduces the original 2^25·26! for n = 26.
