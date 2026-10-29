# Variant of math500-intermediate_algebra-964

For every nonnegative integer $n$, let $\text{rem}_5(n)$ denote the remainder when $n$ is divided by 5. Define a function $g: \{0,1,2,3,\dots\} \times \{0,1,2,3,4\} \to \{0,1,2,3,4\}$ recursively by

\[g(i,j) = \begin{cases}\text{rem}_5 (j+1) & \text{ if } i = 0 \text{ and } 0 \le j \le 4 \text{,}\\ g(i-1,2) & \text{ if } i \ge 1 \text{ and } j = 0 \text{, and} \\ g(i-1, g(i,j-1)) & \text{ if } i \ge 1 \text{ and } 1 \le j \le 4. \end{cases}\]

What is $g(2024,3)$?

**Answer:** 2

(Table: rows i=0..4 are 12340, 34012, 03142, 13421, 41324; every row from i=5 on is 32323, so g(2024,3)=2.)
