# hmmt2024-19 variant

Find the number of ordered triples $(p, q, r)$ of permutations of the set $\{1,2,3,4,5,6\}$ such that, for every $x \in \{1,2,3,4,5,6\}$,
$$p(q(r(x))) = r(q(p(x))) = q(x),\qquad q(r(p(x))) = p(r(q(x))) = r(x),\qquad r(p(q(x))) = q(p(r(x))) = p(x).$$

**Answer:** 1036

(Original: same conditions on $\{1,2,3,4,5\}$, answer 146; solve.py reproduces 146 and gives 1036 for the variant.)
