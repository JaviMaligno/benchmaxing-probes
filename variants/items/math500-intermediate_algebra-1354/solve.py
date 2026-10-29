# Sum_{k=1}^{n} 1/(1+w^k) for w^n=1, w!=1 (n odd). Pairing argument gives n/2.
# Independent check: numeric evaluation for EVERY root w != 1 (all must agree), then rationalize.
import cmath
from fractions import Fraction

def total(n):
    vals = []
    for j in range(1, n):
        # w = e^{2 pi i j/n}; w^k computed from the exact exponent (j*k mod n) to avoid drift
        s = sum(1 / (1 + cmath.exp(2j * cmath.pi * ((j * k) % n) / n)) for k in range(1, n + 1))
        vals.append(s)
    ref = vals[0]
    assert all(abs(v - ref) < 1e-6 for v in vals), "answer depends on choice of w"
    assert abs(ref.imag) < 1e-6
    return Fraction(ref.real).limit_denominator(1000)

def pairing(n):
    # (n-1)/2 pairs summing to 1, plus the k=n term 1/2
    return Fraction((n - 1) // 2) + Fraction(1, 2)

orig = total(1997)
print("original n=1997:", orig, "pairing:", pairing(1997))
assert orig == Fraction(1997, 2) == pairing(1997)

var = total(2027)
print("variant n=2027:", var, "pairing:", pairing(2027))
assert var == pairing(2027)
