from math import factorial
from fractions import Fraction
from sympy import isprime

def direct(p, N):
    n = factorial(N)
    r = (pow(p, n, n) - 1) % n
    return Fraction(r, n)

def crt_method(p, N):
    # p appears exactly once in N!; p^n = 1 mod m (m = N!/p), = 0 mod p
    n = factorial(N); m = n // p
    k = (-pow(m % p, -1, p)) % p
    return Fraction(m * k, n)

# original
assert isprime(2017)
o = direct(2017, 2025); assert o == crt_method(2017, 2025)
print("original:", o, "matches 1311/2017:", o == Fraction(1311, 2017))
# variant
assert isprime(2011) and 2011 <= 2025 < 2*2011
v = direct(2011, 2025); assert v == crt_method(2011, 2025)
print("variant:", v)
