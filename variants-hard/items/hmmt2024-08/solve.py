# hmmt2024-08 variant: exponents a>b>c>d all odd, |w^a+w^b+w^c+w^d| = sqrt(3), w = e^{2 pi i/13}.
# Exact check: |S|^2 computed symbolically via sympy (minimal polynomial reduction), plus numeric filter.
import cmath, itertools, math
import sympy as sp

N = 13
z = cmath.exp(2j * math.pi / N)
w = sp.exp(2 * sp.pi * sp.I / N)

def exact_ok(c):
    S = sum(w**e for e in c)
    val = sp.N(sp.expand(S * sp.conjugate(S)), 60)
    val_ok = abs(val - 3) < sp.Float('1e-50')
    # also check via difference structure: |S|^2 = 4 + sum over ordered pairs of w^(x-y)
    diffs = sorted(((x - y) % N) for x in c for y in c if x != y)
    return val_ok and diffs == list(range(1, N)) * 1

def best(allowed, limit=60):
    res = None
    for c in itertools.combinations([e for e in range(1, limit) if allowed(e)], 4):
        if abs(abs(sum(z**e for e in c)) - math.sqrt(3)) < 1e-9:
            d, cc, b, a = c
            v = 1000 * a + 100 * b + 10 * cc + d
            if res is None or v < res[0]:
                res = (v, c)
    assert exact_ok(res[1])
    # any a >= limit would give value >= 1000*limit, larger than found
    assert res[0] < 1000 * limit
    return res

orig = best(lambda e: True)
print("original:", orig)
assert orig[0] == 7521
var = best(lambda e: e % 2 == 1)
print("variant:", var)
