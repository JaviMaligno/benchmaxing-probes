# Chords AB, CD, EF through X pairwise perpendicular; X at origin, chords along axes.
# A at -a_i on axis i, partner at +k/a_i with k = R^2 - OX^2 (power of a point).
# O = ((k/a_i - a_i)/2)_i up to sign; |O|^2 = OX^2 gives a quadratic in k.
import sympy as sp, itertools, random

def solve(a, d2):
    k = sp.symbols('k')
    eq = sum((k/ai - ai)**2 for ai in a)/4 - d2
    roots = sp.solve(sp.Eq(eq, 0), k)
    valid = [r for r in roots if r.is_real and r > 0]
    # numeric geometric check: build points, verify all six on sphere radius R
    for r in valid:
        kv = float(r)
        O = [(kv/float(ai) - float(ai))/2 for ai in a]
        R2 = float(r + d2)
        pts = []
        for i, ai in enumerate(a):
            for t in (-float(ai), kv/float(ai)):
                p = [0.0]*3; p[i] = t; pts.append(p)
        for p in pts:
            assert abs(sum((p[j]-O[j])**2 for j in range(3)) - R2) < 1e-9
        assert abs(sum(c*c for c in O) - float(d2)) < 1e-9
    return sp.nsimplify(sp.simplify(sum(r + d2 for r in valid)))

orig = solve([1, sp.sqrt(2), 2], sp.Rational(1, 2))
print("original:", orig, "matches 31/7:", orig == sp.Rational(31, 7))
var = solve([1, 2, 3], 2)
print("variant:", var, float(var))
