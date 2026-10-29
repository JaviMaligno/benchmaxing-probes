# System: |C - z| = r,  |z - a - k| = |z - b*i - k|  ; find k with exactly one solution z.
import sympy as sp
from fractions import Fraction

def solve(cx, cy, r, a, b):
    k, x, y = sp.symbols('k x y', real=True)
    # perpendicular bisector of (a+k, 0) and (k, b)
    line = sp.expand((x-a-k)**2 + y**2 - (x-k)**2 - (y-b)**2)  # = 0
    circ = (x-cx)**2 + (y-cy)**2 - r**2
    # eliminate y via line (linear in x,y), get quadratic in x, require zero discriminant
    ysol = sp.solve(line, y)[0]
    q = sp.Poly(sp.expand(circ.subs(y, ysol)), x)
    A, B, C = q.all_coeffs()
    disc = sp.simplify(B**2 - 4*A*C)
    ks = sp.solve(sp.Eq(disc, 0), k)
    # independent numeric check: count intersections for each k
    for kv in ks:
        sols = sp.solve([circ.subs(k, kv), line.subs(k, kv)], [x, y], dict=True)
        assert len(sols) == 1, (kv, sols)
    s = sp.nsimplify(sum(ks))
    fr = Fraction(int(sp.numer(s)), int(sp.denom(s)))
    return ks, fr, fr.numerator + fr.denominator

ks, s, ans = solve(25, 20, 5, 4, 3)
print("original k:", ks, "sum:", s, "m+n:", ans)
assert ans == 77
ks, s, ans = solve(20, 15, 13, 12, 5)
print("variant k:", ks, "sum:", s, "m+n:", ans)
