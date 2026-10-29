# Brute-force sum of proper divisors, plus independent sympy check.
from sympy import divisor_sigma

def s_brute(n):
    return sum(d for d in range(1, n) if n % d == 0)

def s_sympy(n):
    return int(divisor_sigma(n)) - n

def answer(n):
    a = s_brute(s_brute(n))
    b = s_sympy(s_sympy(n))
    assert a == b
    return a

orig = answer(284)
print("original (N=284):", orig)
assert orig == 284

print("variant (N=244): s(244) =", s_brute(244), "; answer =", answer(244))
