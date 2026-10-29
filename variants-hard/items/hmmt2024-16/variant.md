# hmmt2024-16 variant

**Problem.** A $4 \times 5$ board of unit squares is given. In each square, one of its two diagonals is chosen uniformly at random and drawn, independently for each square. Compute the probability that the resulting $40$ triangular regions can be colored black and white so that any two regions sharing an edge receive different colors.

**Answer.** $\dfrac{1}{4096}$

(Original: $4\times 4$ grid, answer $1/512$. Verified by brute force over all $2^{20}$ configurations in solve.py.)
