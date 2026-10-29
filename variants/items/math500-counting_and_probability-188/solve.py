from fractions import Fraction
import random

def exact_prob(a, L):
    """P(triangle with sides a, x, y exists), x,y ~ U(0,L).
    For fixed x, valid y in (|x-a|, x+a) intersected with (0,L); integrate piecewise-linear length exactly."""
    a, L = Fraction(a), Fraction(L)
    def length(x):
        lo = max(abs(x - a), Fraction(0)); hi = min(x + a, L)
        return max(hi - lo, Fraction(0))
    # breakpoints where piecewise-linear integrand changes; Simpson exact on linear pieces
    pts = sorted({Fraction(0), L} | {p for p in (a, L - a, (L - a) / 1) if 0 < p < L})
    total = Fraction(0)
    for u, v in zip(pts, pts[1:]):
        m = (u + v) / 2
        total += (v - u) * (length(u) + 4 * length(m) + length(v)) / 6
    return total / (L * L)

def mc(a, L, n=400000, seed=1):
    r = random.Random(seed); c = 0
    for _ in range(n):
        x, y = r.uniform(0, L), r.uniform(0, L)
        if x + y > a and a + x > y and a + y > x: c += 1
    return c / n

orig = exact_prob(1, 3)
print("original:", orig, "MC", mc(1, 3))
assert orig == Fraction(1, 2)
var = exact_prob(2, 4)
print("variant:", var, float(var), "MC", mc(2, 4))
