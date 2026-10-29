# aime25-15 variant

**Problem.** Let $M$ be the number of ordered triples of positive integers $(x, y, z)$ with $x, y, z \le 3^7$ such that $x^3 + y^3 + z^3$ is divisible by $3^8$. Find the remainder when $M$ is divided by $1000$.

**Answer.** 379  (M = 10097379)

Original: bound 3^6, modulus 3^7, answer 735 (N = 885735). Verified by solve.py (cube-residue convolution, cross-checked against brute force on small cases).
