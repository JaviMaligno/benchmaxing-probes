from fractions import Fraction
from itertools import product
from sympy import prime

def p_even(n):
    ps = [prime(i) for i in range(1, n+1)]
    good = sum(1 for a, b in product(ps, ps) if (a + b) % 2 == 0)
    return Fraction(good, len(ps)**2)

orig = p_even(6)
print("original (first six primes):", orig)
assert orig == Fraction(13, 18)
var = p_even(7)
print("variant (first seven primes):", var)
