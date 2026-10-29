# Brute force: largest n < bound with given residues; plus CRT check.
from sympy.ntheory.modular import crt

def largest(bound, conds):
    for n in range(bound - 1, -1, -1):
        if all(n % m == r for m, r in conds):
            return n

def via_crt(bound, conds):
    ms = [m for m, _ in conds]; rs = [r for _, r in conds]
    x, M = crt(ms, rs)
    x = int(x); M = int(M)
    return x + ((bound - 1 - x) // M) * M

orig = (2010, [(7, 5), (11, 10), (13, 10)])
var = (3000, [(7, 2), (11, 8), (13, 8)])
o = largest(*orig); assert o == via_crt(*orig)
print("original:", o, "expected 1440", "OK" if o == 1440 else "MISMATCH")
v = largest(*var); assert v == via_crt(*var)
print("variant:", v)
