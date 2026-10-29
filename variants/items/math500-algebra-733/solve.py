# The shared "messy" terms (exponential, binomial, phi) are identical in f and g,
# so they cancel in f - g; intersections are the real roots of the polynomial difference.
import sympy as sp
from fractions import Fraction
x = sp.symbols('x')

def largest_intersection(fpoly, gpoly):
    d = sp.expand(gpoly - fpoly)
    roots = [r for r in sp.real_roots(sp.Poly(d, x))]
    # independent check: brute-force integer/half-integer scan for sign changes / zeros
    zs = [Fraction(k, 2) for k in range(-200, 201) if d.subs(x, sp.Rational(k, 2)) == 0]
    return max(roots), d, sp.factor(d), max(zs) if zs else None

orig_f = 72*x**4 + 3*x**3 - 6*x**2 + 2*x + 1
orig_g = 72*x**4 + 4*x**3 - 11*x**2 - 6*x + 13
var_f  = 51*x**4 + 3*x**3 - 4*x**2 + 5*x + 2
var_g  = 51*x**4 + 4*x**3 - 7*x**2 - 8*x + 17

o = largest_intersection(orig_f, orig_g)
print("original: g-f =", o[2], "largest root =", o[0], "scan =", o[3])
assert o[0] == 6
v = largest_intersection(var_f, var_g)
print("variant:  g-f =", v[2], "largest root =", v[0], "scan =", v[3])
print("VARIANT ANSWER:", v[0])
