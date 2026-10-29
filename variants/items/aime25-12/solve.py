# Region in plane x+y+z=S with x-yz<y-zx<z-xy  <=>  (x-y)(1+z)<0 and (y-z)(1+x)<0.
# Parametrise by (x,y), z=S-x-y; area in plane = sqrt(3) * area in (x,y).
from fractions import Fraction as F
import math, sympy as sp

def clip(poly, a, b, c):  # keep a*x+b*y+c >= 0
    out = []
    n = len(poly)
    for i in range(n):
        P, Q = poly[i], poly[(i+1) % n]
        fp = a*P[0]+b*P[1]+c; fq = a*Q[0]+b*Q[1]+c
        if fp >= 0: out.append(P)
        if (fp >= 0) != (fq >= 0):
            t = fp/(fp-fq); out.append((P[0]+t*(Q[0]-P[0]), P[1]+t*(Q[1]-P[1])))
    return out

def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly))))/2

def finite_area_xy(S):
    B = F(10**6)
    box = [(-B,-B),(B,-B),(B,B),(-B,B)]
    # linear forms (a,b,c) = a x + b y + c
    xy = (1,-1,0); onez = (-1,-1,1+S); yz = (1,2,-S); onex = (1,0,1)
    neg = lambda f: tuple(-v for v in f)
    regs = []
    for s1 in (1,-1):        # sign of (x-y); (1+z) must be opposite
        for s2 in (1,-1):    # sign of (y-z); (1+x) must be opposite
            fs = [xy if s1>0 else neg(xy), neg(onez) if s1>0 else onez,
                  yz if s2>0 else neg(yz), neg(onex) if s2>0 else onex]
            p = box
            for f in fs:
                p = clip(p, *map(F, f))
                if not p: break
            if p and area(p) > 0:
                bounded = all(abs(v[0]) < B and abs(v[1]) < B for v in p)
                regs.append((bounded, area(p)))
    fin = [a for bd, a in regs if bd]
    assert len(regs) == 3 and len(fin) == 1, regs
    return fin[0]

def grid_check(S, A_xy, N=1500):
    # independent numeric check: count lattice cells in bounding box of finite region
    lo, hi = -2, S + 3
    h = (hi - lo) / N; cnt = 0
    for i in range(N):
        x = lo + (i+.5)*h
        for j in range(N):
            y = lo + (j+.5)*h; z = S - x - y
            if x - y*z < y - z*x < z - x*y and x > -1 and y > -1 and z > -1:
                cnt += 1
    return cnt*h*h

def answer(S):
    A = finite_area_xy(S)
    expr = sp.nsimplify(sp.Rational(A.numerator, A.denominator)) * sp.sqrt(3)
    a, b = sp.Mul(expr).as_coeff_Mul()
    a = sp.Rational(a); b = b**2
    assert a.is_integer and sp.factorint(int(b)) and all(e == 1 for e in sp.factorint(int(b)).values())
    g = grid_check(S, A)
    print(f"S={S}: area = {expr}, grid xy-area {g:.2f} vs exact {float(A):.2f}, a+b = {int(a)+int(b)}")
    return int(a) + int(b)

assert answer(75) == 510, "original check failed"
print("ORIGINAL OK")
print("VARIANT ANSWER:", answer(87))
