# aime25-25 variant

**Problem.** Seventeen seats are lined up in a single row. Nine guests each choose a seat so that no guest is seated next to two other guests. Let $N$ be the number of subsets of the 17 seats that could be occupied. Find the remainder when $N$ is divided by $1000$.

**Answer.** 139  ($N = 3139$)

Verified by `solve.py` (brute-force enumeration plus the block/gap formula; same logic reproduces the original 2907 -> 907).
