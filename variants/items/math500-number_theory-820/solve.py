from math import gcd
from sympy import divisors

def count(g, L):
    # a = g*x, b = g*y with x*y = L/g^2... general: enumerate divisors a of L that are multiples of g
    n = 0
    for a in divisors(L):
        if a % g: continue
        b = g * L // a  # since a*b = gcd*lcm
        if a < b and gcd(a, b) == g and a * b // gcd(a, b) == L:
            n += 1
    return n

orig = count(210, 210**3)
print("original (gcd=210, lcm=210^3):", orig)
assert orig == 8
var = count(2310, 2310**3)
print("variant (gcd=2310, lcm=2310^3):", var)
