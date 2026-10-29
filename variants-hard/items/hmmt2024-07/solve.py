from math import gcd
from sympy import factorint

def m_value(N, start):
    # gcd of an integer polynomial of degree N over all n>=start equals gcd of
    # N+1 consecutive values (Newton forward differences); we use extra values as a check.
    def P(n):
        r = 1
        for k in range(1, N + 1):
            r *= (n - k**3)
        return r
    d = 0
    for n in range(start, start + N + 1):
        d = gcd(d, P(n))
    d2 = d
    for n in range(start + N + 1, start + 3 * N + 50):
        d2 = gcd(d2, P(n))
    assert d2 == d
    f = factorint(d)
    return sum(f.values()), f

orig, fo = m_value(40, 2024)
print("original (40 cubes, n>2023):", orig, fo)
assert orig == 48
var, fv = m_value(45, 2025)
print("variant (45 cubes, n>2024):", var, fv)
