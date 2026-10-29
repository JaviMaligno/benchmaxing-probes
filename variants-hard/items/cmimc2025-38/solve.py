"""cmimc2025-38 variant check.
Locus of m such that roots of (x^2 + B x + C)(x^2 - 2 m x + K) are concyclic.
Analytic: segment [-sqrt K, sqrt K] (length 2 sqrt K) plus a full circle of radius
r^2/(2|c|), where p = u+vi root of first quadratic, c = (K+|p|^2)/(2u), r^2 = c^2-K.
Numeric (independent): parametrise by a root a of the 2nd quadratic (b = K/a),
contour D(a)=0 where D is the 2x2 determinant 'a and b lie on a common circle
through p, conj(p)' (circle family |z|^2-|p|^2-2c(Re z-u)=0, incl. line Re z=u),
map contours to m=(a+K/a)/2 and measure length (each m covered twice).
"""
import numpy as np, sympy as sp
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

def analytic(B, C, K):
    u = sp.Rational(-B, 2); p2 = sp.Integer(C)  # |p|^2 = C for complex roots
    c = (K + p2) / (2 * u); r2 = c**2 - K
    assert r2 > 0
    return sp.nsimplify(2 * sp.sqrt(K) + 2 * sp.pi * r2 / (2 * abs(c)))

def numeric(B, C, K, L=60.0, N=3001):
    u = -B / 2.0; p2 = float(C)
    xs = np.linspace(-L, L, N); X, Y = np.meshgrid(xs, xs + 1e-7)
    A = X + 1j * Y; Bb = K / A
    D = (np.abs(A)**2 - p2) * (Bb.real - u) - (np.abs(Bb)**2 - p2) * (A.real - u)
    D = D / (1 + np.abs(D))  # tame blow-up near 0
    cs = plt.contour(X, Y, D, levels=[0.0])
    total = 0.0
    for path in cs.allsegs[0]:
        a = path[:, 0] + 1j * path[:, 1]
        if len(a) < 2: continue
        m = (a + K / a) / 2
        dm = np.abs(np.diff(m))
        # drop jumps (spurious level crossing at pole a=0 or across sign-tame artefacts)
        dm = dm[dm < 5.0]
        # also discard parts where D sign change is a pole artefact: check |raw D| small
        total += dm.sum()
    plt.close("all")
    return total / 2

orig = analytic(2, 5, 25)
print("original analytic:", orig, "=", float(orig))
print("original expected 10+40pi/3 =", float(10 + 40 * sp.pi / 3), "match:", sp.simplify(orig - (10 + 40 * sp.pi / 3)) == 0)
print("original numeric :", numeric(2, 5, 25))
var = analytic(4, 5, 25)
print("variant analytic :", var, "=", float(var))
print("variant numeric  :", numeric(4, 5, 25))
