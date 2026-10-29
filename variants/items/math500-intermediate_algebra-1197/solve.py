from fractions import Fraction as F

def lagrange_eval(pts, x):
    tot = F(0)
    for i, (xi, yi) in enumerate(pts):
        term = F(yi)
        for j, (xj, _) in enumerate(pts):
            if i != j:
                term *= F(x - xj, xi - xj)
        tot += term
    return tot

def solve(c, ns, target):
    # p of degree len(ns)-1 interpolating n/(n^2 - c) at ns; evaluate at target
    pts = [(n, F(n, n*n - c)) for n in ns]
    return lagrange_eval(pts, target)

def solve_method(c, ns, target):
    # Solution method: q(x) = (x^2-c)p(x) - x = (a x + b) prod(x-n); use x = +-sqrt(c) (c perfect square)
    r = int(round(c ** 0.5)); assert r*r == c
    prod = lambda x: __import__('math').prod(x - n for n in ns)
    # q(r) = -r, q(-r) = r
    # (a r + b) P(r) = -r ; (-a r + b) P(-r) = r
    s1 = F(-r, prod(r)); s2 = F(r, prod(-r))
    a = (s1 - s2) / (2*r); b = (s1 + s2) / 2
    q = (a*target + b) * prod(target)
    return (q + target) / (target*target - c)

orig = solve(1, range(2, 8), 8)
print("original:", orig, solve_method(1, range(2, 8), 8))
assert orig == F(3, 56)
var = solve(4, range(3, 9), 9)
print("variant:", var, solve_method(4, range(3, 9), 9))
assert var == solve_method(4, range(3, 9), 9)
