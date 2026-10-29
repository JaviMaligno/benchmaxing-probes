import sympy as sp
from mpmath import mp, mpf, sqrt as msqrt, acos
mp.dps = 40

def solve(AB, BC, AD):
    R = sp.Rational(AB, 2)
    A = sp.Matrix([-R, 0]); B = sp.Matrix([R, 0]); O = sp.Matrix([0, 0])
    # D on upper semicircle with AD given: angle ADB = 90, so BD = sqrt(AB^2-AD^2)
    # D = A + AD*(cos a, sin a), cos a = AD/AB
    ca = sp.Rational(AD, AB); sa = sp.sqrt(1 - ca**2)
    D = A + AD * sp.Matrix([ca, sa])
    cb = sp.Rational(BC, AB); sb = sp.sqrt(1 - cb**2)
    C = B + BC * sp.Matrix([-cb, sb])
    # E = intersection of lines BC and AD
    t, s = sp.symbols('t s')
    sol = sp.solve(list(A + t*(D-A) - (B + s*(C-B))), [t, s], dict=True)[0]
    E = sp.simplify(A + sol[t]*(D-A))
    # triangle E C D; E-excircle center = (-e*E + c*C + d*D)/(-e+c+d) with side lengths opposite
    e = sp.sqrt(((C-D).T*(C-D))[0]); c = sp.sqrt(((E-D).T*(E-D))[0]); d = sp.sqrt(((E-C).T*(E-C))[0])
    L = (-e*E + c*C + d*D) / (-e + c + d)
    OL = sp.sqrt(((L-O).T*(L-O))[0])
    return sp.nsimplify(sp.radsimp(sp.simplify(OL))), sp.N(OL, 30), (A, B, C, D, E, L)

def numeric_check(AB, BC, AD):
    # independent float check: excenter = point equidistant from line CD and lines EC, ED, on far side of CD from E
    import math
    R = AB/2
    A = (-R, 0); B = (R, 0)
    D = (A[0] + AD*AD/AB, AD*math.sqrt(1-(AD/AB)**2))
    C = (B[0] - BC*BC/AB, BC*math.sqrt(1-(BC/AB)**2))
    def inter(P1,P2,P3,P4):
        x1,y1=P1;x2,y2=P2;x3,y3=P3;x4,y4=P4
        den=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        px=((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/den
        py=((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/den
        return (px,py)
    E = inter(A,D,B,C)
    dist=lambda P,Q: math.hypot(P[0]-Q[0],P[1]-Q[1])
    # excenter opposite E lies on internal bisector of angle E at distance r_E/sin(E/2)
    a=dist(C,D); b=dist(E,D); c=dist(E,C)  # a opposite E
    s=(a+b+c)/2; area=math.sqrt(s*(s-a)*(s-b)*(s-c)); rE=area/(s-a)
    u1=((C[0]-E[0])/c,(C[1]-E[1])/c); u2=((D[0]-E[0])/b,(D[1]-E[1])/b)
    bis=(u1[0]+u2[0],u1[1]+u2[1]); n=math.hypot(*bis); bis=(bis[0]/n,bis[1]/n)
    cosE=u1[0]*u2[0]+u1[1]*u2[1]; half=math.acos(cosE)/2
    L=(E[0]+bis[0]*rE/math.sin(half),E[1]+bis[1]*rE/math.sin(half))
    return math.hypot(*L)

# Original check
ex, num, _ = solve(20, 13, 7)
target = (97 - 3*sp.sqrt(1001))/2
print("original exact:", ex, "numeric:", num, "float-check:", numeric_check(20,13,7))
print("original matches:", sp.simplify(ex - target) == 0)

import sys
if len(sys.argv) > 1:
    AB, BC, AD = map(int, sys.argv[1:4])
else:
    AB, BC, AD = 20, 12, 8
ex, num, _ = solve(AB, BC, AD)
print("variant", (AB,BC,AD), "exact:", ex, "numeric:", num, "float-check:", numeric_check(AB,BC,AD))
