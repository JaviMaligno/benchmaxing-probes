# hmmt2025-18 variant

Bea writes $1011$ numbers $x_{1}, \ldots, x_{1011}$ around a circle. Initially, each number is chosen uniformly and independently at random from the interval $[0,1]$. Every minute, she *simultaneously* replaces each $x_{i}$ with $\max(x_{i-1}, x_{i}, x_{i+1})$ for all $i = 1, 2, \ldots, 1011$ (indices taken cyclically, so $x_{0}=x_{1011}$ and $x_{1012}=x_{1}$). Compute the expected number of distinct values on the circle after $60$ minutes.

**Answer:** $\frac{1011}{61}$
