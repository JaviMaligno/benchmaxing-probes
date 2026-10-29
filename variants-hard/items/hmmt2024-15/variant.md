# hmmt2024-15 variant

The kingdom of Dodecania has $12$ towns. Its council decides to build several two-way roads, each joining a pair of distinct towns. When construction is complete, it turns out that every town is joined by a single road to exactly $3$ other towns, and for any pair of distinct towns, the number of other towns joined by a single road to both of them is either exactly $0$ or exactly $2$. Compute the number of ways Dodecania could have built its roads.

**Answer:** 421575

(Components must be $K_4$ or the cube graph $Q_3$; $12 = 4+4+4$ gives $\frac{12!}{3!\,(4!)^3} = 5775$, $12 = 4+8$ gives $\binom{12}{4}\cdot\frac{8!}{48} = 495\cdot 840 = 415800$.)
