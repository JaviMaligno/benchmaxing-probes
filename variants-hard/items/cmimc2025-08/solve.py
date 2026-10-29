from sympy import symbols, factor_list, I, Poly, expand, re, im, sqrt, N, real_roots, sqrt as ssqrt, Integer
import cmath
x = symbols('x')

def solve(P):
    P = expand(P)
    assert len(real_roots(Poly(P, x))) == 0, "P has a real root"
    # numeric first-quadrant roots
    q1 = [complex(r) for r in Poly(P, x).nroots(n=30) if re(r) > 0 and im(r) > 0]
    assert len(q1) == 1, q1
    r = q1[0]
    _, facs = factor_list(P, extension=I)
    for f, _m in facs:
        pf = Poly(f, x)
        if pf.degree() != 2:
            continue
        if abs(complex(pf.eval(r))) > 1e-8:
            continue
        c2, c1, c0 = pf.all_coeffs()
        assert c2 == 1
        # x^2 + c1 x + c0 = 0 -> x = (-c1 +- sqrt(c1^2 - 4 c0))/2
        s = expand(-c1); D = expand(c1**2 - 4*c0)
        a, b = int(re(s)), int(im(s)); c, d = int(re(D)), int(im(D))
        # D must not be a perfect Gaussian square (else form degenerates)
        rt = complex(D) ** 0.5
        assert abs(rt.real - round(rt.real)) > 1e-6 or abs(rt.imag - round(rt.imag)) > 1e-6
        cand = (complex(a, b) + cmath.sqrt(complex(c, d))) / 2  # principal sqrt
        assert abs(cand - r) < 1e-9, (cand, r)
        return a, b, c, d, a + b + c + d
    raise ValueError("no quadratic factor found")

orig = x**4 + 20*x**3 + 29*x**2 - 666*x + 2025
o = solve(orig)
print("original (a,b,c,d,sum):", o)
assert o[-1] == 322

var = x**4 + 24*x**3 + 65*x**2 - 900*x + 2500
v = solve(var)
print("variant  (a,b,c,d,sum):", v)
print("ANSWER", v[-1])
