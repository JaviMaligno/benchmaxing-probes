import itertools, random
import sympy as sp

def solve(s, r):
    s, r = sp.nsimplify(s), sp.nsimplify(r)
    # spheres in the 8 corners, centers at distance r from three faces
    cs = [tuple(r if b == 0 else s - r for b in bits) for bits in itertools.product([0, 1], repeat=3)]
    # check each is externally tangent to exactly three others
    for c in cs:
        t = sum(1 for d in cs if d != c and sp.simplify(sp.sqrt(sum((a-b)**2 for a, b in zip(c, d))) - 2*r) == 0)
        assert t == 3, t
    # by symmetry the tangent sphere is centered at cube center
    m = s/2
    R = sp.simplify(sp.sqrt(3*(m - r)**2) - r)
    assert R > 0 and R <= m  # contained in cube
    # numeric check: maximize min_i(|P-c_i|) - r over interior points P (random search)
    csf = [tuple(float(x) for x in c) for c in cs]
    best = -1
    rnd = random.Random(0)
    for _ in range(200000):
        P = [rnd.uniform(0, float(s)) for _ in range(3)]
        v = min(sum((a-b)**2 for a, b in zip(P, c))**0.5 for c in csf) - float(r)
        best = max(best, v)
    assert best <= float(R) + 1e-9 and best > float(R) - 0.05, (best, float(R))
    return sp.radsimp(R)

orig = solve(4, 1)
print("original:", orig, float(orig))
assert sp.simplify(orig - (sp.sqrt(3) - 1)) == 0
var = solve(6, sp.Rational(3, 2))
print("variant:", var, float(var))
