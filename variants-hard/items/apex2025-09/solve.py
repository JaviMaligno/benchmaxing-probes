"""apex2025-09 variant check.
Original: f = e^{it} + e^{2it} + (1/3) e^{3it}  -> perimeter 2*sqrt(3) + 8*pi/3
Variant : g = e^{it} + (3/2) e^{2it} + e^{3it} + (1/4) e^{4it}
Method (both): f'(t) = i w (1+w)^n with w = e^{it}, so |f'| = (2 cos(t/2))^n; the curve has a
cusp at t = pi and one self-intersection on the real axis at t = +-t0; the inner loop
t in [t0, 2pi - t0] is not on the boundary, so perimeter = int_{-t0}^{t0} |f'| dt.
Exact part: sympy (t0 from Im f = 0). Independent numeric part: segment-intersection search +
winding numbers decide which arcs bound the filled region, then integrate |f'| over them.
"""
import numpy as np, sympy as sp
from scipy.integrate import quad

def exact(coefs, n):
    t = sp.symbols('t', real=True); c = sp.symbols('c')
    w = sp.exp(sp.I*t)
    f = sum(sp.Rational(a)*w**m for m, a in coefs.items())
    # check derivative structure f' = i w (1+w)^n
    z = sp.symbols('z')  # polynomial identity in z = w
    assert sp.expand(sum(sp.Rational(a)*m*z**m for m, a in coefs.items()) - z*(1+z)**n) == 0
    # Im f = sum a_m sin(m t) = sin t * sum a_m U_{m-1}(cos t)  (Chebyshev U)
    poly = sp.factor(sum(sp.Rational(a)*sp.chebyshevu(m-1, c) for m, a in coefs.items()))
    tt = sp.Rational(7, 10)   # spot-check the identity
    assert abs(sp.N(sp.im(f.subs(t, tt)) - sp.sin(tt)*poly.subs(c, sp.cos(tt)))) < 1e-12
    roots = [r for r in sp.solve(poly, c) if r.is_real and -1 < r < 1]
    assert len(roots) == 1, (poly, roots)
    t0 = sp.acos(roots[0])
    speed = (2*sp.cos(t/2))**n            # >= 0 on [-pi, pi]
    Fanti = sp.integrate(speed, t)
    return poly, t0, sp.radsimp(sp.simplify(sp.expand_trig(Fanti.subs(t, t0) - Fanti.subs(t, -t0))))

def numeric(coefs, N=3000):
    f = lambda t: sum(float(a)*np.exp(1j*m*t) for m, a in coefs.items())
    df = lambda t: sum(1j*m*float(a)*np.exp(1j*m*t) for m, a in coefs.items())
    t = np.linspace(0, 2*np.pi, N, endpoint=False); A = f(t); B = np.roll(A, -1)
    cr = lambda u, v: (u.conj()*v).imag
    R = (B-A)[:, None]; S = (B-A)[None, :]; QP = A[None, :]-A[:, None]
    den = cr(R, S)
    with np.errstate(all='ignore'):
        u = cr(QP, S)/den; v = cr(QP, R)/den
    I, J = np.where((u > 0) & (u < 1) & (v > 0) & (v < 1) & (np.abs(den) > 1e-14))
    cuts = sorted({round(t[k], 3) for i, j in zip(I, J) if i < j and min(j-i, N-(j-i)) > 8 for k in (i, j)})
    zz = f(np.linspace(0, 2*np.pi, 8000, endpoint=False)); zc = np.append(zz, zz[0])
    wind = lambda p: round(np.angle((zc[1:]-p)/(zc[:-1]-p)).sum()/2/np.pi)
    cuts2 = cuts + [cuts[0] + 2*np.pi]; L = 0
    for a, b in zip(cuts2[:-1], cuts2[1:]):
        m = a + 0.3719*(b-a); d = df(m); nrm = 1j*d/abs(d); p = f(m)
        if (wind(p+1e-3*nrm) == 0) != (wind(p-1e-3*nrm) == 0):
            L += quad(lambda x: abs(df(x)), a, b, limit=200)[0]
    return [round(x/np.pi, 3) for x in cuts], L

R = sp.Rational
for name, coefs, n, expected in [
    ("original", {1: 1, 2: 1, 3: R(1, 3)}, 2, 2*sp.sqrt(3) + 8*sp.pi/3),
    ("variant",  {1: 1, 2: R(3, 2), 3: 1, 4: R(1, 4)}, 3, None),
]:
    poly, t0, P = exact(coefs, n)
    cuts, L = numeric(coefs)
    print(f"{name}: Im f / sin t = {poly}; t0 = {t0}; exact perimeter = {P} = {float(P):.6f}")
    print(f"   numeric: intersection params/pi = {cuts}; boundary length = {L:.6f}")
    assert abs(L - float(P)) < 1e-2
    if expected is not None:
        assert sp.simplify(P - expected) == 0
        print("   ORIGINAL CHECK PASSED (matches 2*sqrt(3) + 8*pi/3)")
