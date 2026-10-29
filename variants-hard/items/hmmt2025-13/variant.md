# hmmt2025-13 variant

**Problem.** Maya has $20$ marbles labeled $1,2,3,\ldots,20$, as well as $5$ indistinguishable jars. Two marbles are *adjacent* if their labels differ by $1$. Compute the number of ways for her to put $4$ marbles in each jar such that each marble is in the same jar as at least one of its adjacent marbles. (The order in which the marbles are placed does not matter.)

**Answer.** $945$

Verified by `solve.py` (DFS enumeration of set partitions + independent run-structure enumeration; both give 105 on the original 16 balls / 4 boxes data and 945 on the variant).
