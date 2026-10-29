"""hmmt2025-27 variant check.
Exact: with theta = angle ABP = angle ACP, law of sines in BPC gives
sin(B-theta) = r sin(C-theta), r = PC/BP. Then [BPC]/[ABC] computed exactly.
Independent check: numeric root-finding for P directly from the two conditions."""
import sympy as sp
import mpmath as mp

def exact(AB, AC, BC, r):
    a, b, c = map(sp.Integer, (BC, AC, AB))
    cosB = (a**2 + c**2 - b**2) / (2*a*c); cosC = (a**2 + b**2 - c**2) / (2*a*b)
    sinB = sp.sqrt(1 - cosB**2); sinC = sp.sqrt(1 - cosC**2)
    th = sp.atan((sinB - r*sinC) / (cosB - r*cosC))
    if th < 0: th += sp.pi
    Bang, Cang = sp.acos(cosB), sp.acos(cosC)
    assert 0 < float(th) < min(float(Bang), float(Cang))  # P strictly inside
    x = a*sp.sin(Cang - th) / sp.sin(Bang + Cang - 2*th)   # BP
    area_BPC = sp.Rational(1, 2)*x*(r*x)*sp.sin(sp.pi - (Bang + Cang - 2*th))
    area_ABC = sp.Rational(1, 2)*a*c*sinB
    return sp.nsimplify(sp.simplify(area_BPC/area_ABC), rational=True), sp.N(area_BPC/area_ABC, 30)

def numeric(AB, AC, BC, k):  # k = BP/PC
    mp.mp.dps = 40
    Ax = mp.mpf(AB**2 - AC**2 + BC**2)/(2*BC); Ay = mp.sqrt(AB**2 - Ax**2)
    A = (Ax, Ay); B = (0, 0); C = (mp.mpf(BC), 0)
    def ang(V, X, Y):
        u = (X[0]-V[0], X[1]-V[1]); w = (Y[0]-V[0], Y[1]-V[1])
        return mp.acos((u[0]*w[0]+u[1]*w[1])/mp.sqrt(u[0]**2+u[1]**2)/mp.sqrt(w[0]**2+w[1]**2))
    f = lambda px, py: [ang(B, A, (px, py)) - ang(C, A, (px, py)),
                        mp.sqrt(px**2+py**2) - k*mp.sqrt((px-BC)**2+py**2)]
    P = mp.findroot(f, (BC/3, Ay/3))
    return P[1]/Ay  # same base BC

for label, (AB, AC, BC, k), expect in [("original", (6, 8, 7, sp.Rational(1, 2)), sp.Rational(7, 18)),
                                       ("variant", (5, 7, 6, sp.Rational(1, 2)), None)]:
    ex, exn = exact(AB, AC, BC, 1/k)
    nu = numeric(AB, AC, BC, mp.mpf(k.p)/k.q)
    print(label, "exact:", ex, "| exact numeric:", exn, "| independent numeric:", mp.nstr(nu, 25))
    assert abs(float(ex) - float(nu)) < 1e-20 and abs(exn - ex) < 1e-25
    if expect is not None:
        assert ex == expect, ex
        print("original reproduced:", ex == expect)
