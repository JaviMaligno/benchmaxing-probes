# Independent numeric solve: O=(0,0) radius R; P=(a,b) on circle |P|=r, radius r.
# WLOG chord on line y=c. Chord endpoints x=+-s, s=sqrt(R^2-c^2);
# omega meets line at x=a+-t, t=sqrt(r^2-(c-b)^2). Need A,C,D,B = -s, a-t, a+t, s
# with AC:CD:DB = 1:2:3.  Unknowns a,b,c (b determined by a^2+b^2=r^2).
import itertools, math
import sympy as sp

def solve(R, r):
    a, b, c = sp.symbols('a b c', real=True)
    s = sp.sqrt(R**2 - c**2); t = sp.sqrt(r**2 - (c - b)**2)
    eqs = [a**2 + b**2 - r**2,
           (a - t + s) - 2*s/6,      # AC = L/6
           (a + t + s) - 2*s/2]      # AD = L/2
    found = set()
    for a0, b0, c0 in itertools.product([-0.9*r, -0.3*r, 0.3*r, 0.9*r], [-0.9*r, -0.3*r, 0.3*r, 0.9*r], [-0.9*R, -0.5*R, -0.2*R, 0.2*R, 0.5*R, 0.9*R]):
        try:
            sol = sp.nsolve(eqs, (a, b, c), (a0, b0, c0), tol=1e-25, prec=40)
        except Exception:
            continue
        if any(abs(sp.im(v)) > 1e-20 for v in sol):
            continue
        av, bv, cv = [float(sp.re(v)) for v in sol]
        if abs(cv) < 1e-9:   # diameter, excluded
            continue
        if R**2 - cv**2 <= 0 or r**2 - (cv - bv)**2 <= 0:
            continue
        found.add(round(2*math.sqrt(R**2 - cv**2), 9))
    return found

def closed_form(R, r):
    x2 = sp.Rational(R**2 - 4*r**2, 5)
    return 6*sp.sqrt(x2)

print("original (123,61): numeric", solve(123, 61), "closed form", closed_form(123, 61))
assert solve(123, 61) == {42.0} and closed_form(123, 61) == 42
print("variant  (203,101): numeric", solve(203, 101), "closed form", closed_form(203, 101))
