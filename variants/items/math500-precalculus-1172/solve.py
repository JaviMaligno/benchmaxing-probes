from sympy import Matrix, symbols, solve, sqrt, nsimplify
import random, math

def dist(P1, d1, P2, d2):
    P1, d1, P2, d2 = map(Matrix, (P1, d1, P2, d2))
    assert d1.cross(d2) == Matrix([0, 0, 0]), "not parallel"
    t = symbols('t')
    v = P2 + t*d2 - P1
    ts = solve(v.dot(d2), t)[0]
    exact = sqrt(v.subs(t, ts).dot(v.subs(t, ts)))
    # independent check: cross-product formula
    w = P2 - P1
    alt = sqrt(w.cross(d1).dot(w.cross(d1)) / d1.dot(d1))
    assert (exact - alt).simplify() == 0
    # numeric brute-force minimisation over a fine grid near optimum
    f = lambda s: math.dist([float(x) for x in P1], [float(x) for x in (P2 + s*d2)])
    best = min(f(float(ts) + k*1e-4) for k in range(-2000, 2001))
    assert abs(best - float(exact)) < 1e-6
    return nsimplify(exact)

orig = dist([3, -10, 1], [2, -9, -2], [-5, -3, 6], [4, -18, -4])
print("original:", orig)
assert orig == 7
var = dist([1, 5, -2], [3, -10, 4], [8, -1, 9], [-6, 20, -8])
print("variant:", var)
