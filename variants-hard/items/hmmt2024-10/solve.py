# Splitty quartics x^4 + a x^2 + n: brute force reducibility mod every prime p < BOUND
# (factorisation over GF(p)), cross-checked against the classical criterion
# (n square, or a^2-4n square; n(a^2-4n) square gives Galois group C4,
# which has a 4-cycle, so NOT splitty).
from sympy import symbols, Poly, primerange, factor_list
from math import isqrt
x = symbols('x')
BOUND = 1000

def issq(m): return m >= 0 and isqrt(m)**2 == m

def criterion(a, n):
    d = a*a - 4*n
    return issq(n) or issq(d)

def brute(a, n):
    for p in primerange(2, BOUND):
        f = Poly(x**4 + a*x**2 + n, x, modulus=p)
        _, facs = f.factor_list()
        if len(facs) == 1 and facs[0][1] == 1 and facs[0][0].degree() == 4:
            return False  # irreducible mod p
    return True

def total(a, N=100):
    sb = sum(n for n in range(1, N+1) if brute(a, n))
    sc = sum(n for n in range(1, N+1) if criterion(a, n))
    return sb, sc

ob, oc = total(16)
print("original a=16: brute", ob, "criterion", oc, "expected 693", ob == oc == 693)
vb, vc = total(20)
print("variant a=20: brute", vb, "criterion", vc, "agree", vb == vc)
