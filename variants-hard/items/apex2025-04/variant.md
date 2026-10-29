# apex2025-04 variant

Call an $n \times n$ array of positive integers *divisor-complete* if:
- for each $i$, the entries of the $i$-th row are exactly all the divisors of some positive integer $a_i$;
- for each $j$, the entries of the $j$-th column are exactly all the divisors of some positive integer $b_j$;
- $a_i \neq a_k$ whenever $i \neq k$.

For a prime $q$, let $T(q)$ be the least positive integer $n$ that is a multiple of $q$ and for which a divisor-complete $n \times n$ array exists. Compute the sum of $T(q)$ over all primes $q$ with $5 \le q \le 17$.

**Answer:** 355693695038760  ( $= 5! + 7! + 11! + 13! + 17!$ )
