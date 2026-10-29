from fractions import Fraction as F
import sympy as sp

def solve(centers, target):
    # line y=k meets y=(x-c)^2 at x=c±sqrt(k). Point count changes only when
    # 2*sqrt(k) equals a difference of centers; test those critical s plus generic s between.
    diffs = sorted({abs(a-b) for a in centers for b in centers if a!=b})
    crit = [F(0)] + [F(d,2) for d in diffs]
    tests = set(crit)
    for i in range(len(crit)-1):
        tests.add((crit[i]+crit[i+1])/2)
    tests.add(crit[-1]+1); tests.add(crit[-1]*2+7)
    sols = []
    for s in sorted(tests):
        pts = set()
        for c in centers:
            pts.add(c+s); pts.add(c-s)
        if len(pts) == target:
            sols.append(s*s)
    # generic s in an open interval gives a continuum; require only isolated critical solutions
    assert all(any(k == c*c for c in crit) for k in sols), "non-isolated solutions"
    return sols

orig = solve([5*i for i in range(10)], 19)
print("original:", orig, "expected 2025/4:", orig == [F(2025,4)])
var = solve([3*i for i in range(12)], 23)
print("variant:", var, [sp.Rational(v.numerator, v.denominator) for v in var])
