from sympy import primefactors

def sigma_brute(n):
    return sum(d for d in range(1, n + 1) if n % d == 0)

def answer(n):
    A = sigma_brute(n)
    return A, sum(primefactors(A))

# Original: n = 500 -> expected 25
A0, s0 = answer(500)
print("original: sigma(500) =", A0, "sum of distinct primes =", s0)
assert s0 == 25

# Variant: n = 200
A1, s1 = answer(200)
print("variant: sigma(200) =", A1, "sum of distinct primes =", s1)
