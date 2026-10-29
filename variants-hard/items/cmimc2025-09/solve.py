# Largest prime factor of n^5 - 1, by independent trial division and sympy cross-check.
from sympy import factorint, isprime

def lpf_trial(N):
    largest, p = 1, 2
    while p * p <= N:
        while N % p == 0:
            largest, N = p, N // p
        p += 1
    return max(largest, N) if N > 1 else largest

def aurifeuillean(y):
    # Phi_5(5y^2) = A^2 - 5y*B^2 = (A - sqrt(5y)B)(A + ...) with 5y = square when y = 5k^2; here use
    # the identity x^4+x^3+x^2+x+1 = (x^2+3x+1)^2 - 5x(x+1)^2 with x = 5y^2 -> 5x = (5y)^2
    x = 5 * y * y
    A, B = x * x + 3 * x + 1, 5 * y * (x + 1)
    assert A * A - B * B == x**4 + x**3 + x**2 + x + 1
    return A - B, A + B

for n, y in [(45, 3), (80, 4)]:
    N = n**5 - 1
    a = lpf_trial(N)
    b = max(factorint(N))
    assert a == b and isprime(a)
    print(n, "->", a, "Aurifeuillean factors:", aurifeuillean(y), factorint(N))

assert lpf_trial(45**5 - 1) == 2851  # original answer
print("ORIGINAL OK: 2851; VARIANT:", lpf_trial(80**5 - 1))
