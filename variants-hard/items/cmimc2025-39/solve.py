from sympy import sqrt, Rational, nsimplify, simplify, Matrix, Point
import sympy as sp

def area_L(AB, BC, AC):
    a, b, c = sp.Integer(BC), sp.Integer(AC), sp.Integer(AB)
    # place A=(0,0), B=(c,0), C above
    A = sp.Matrix([0, 0]); B = sp.Matrix([c, 0])
    cx = (b**2 + c**2 - a**2) / (2*c)
    cy = sp.sqrt(b**2 - cx**2)
    C = sp.Matrix([cx, cy])
    G = (A + B + C) / 3
    def rot(v, s):  # rotate by +-90
        return sp.Matrix([-s*v[1], s*v[0]])
    def outward_square(P, Q):
        # square P Q R S built outside, returns (R, S) where R adj Q, S adj P
        d = Q - P
        n = rot(d, 1)
        mid = (P + Q) / 2
        if (n.dot(G - mid)) > 0:
            n = -n
        return Q + n, P + n
    X, Y = outward_square(A, B)   # ABXY
    P, Q = outward_square(B, C)   # BCPQ
    M, N = outward_square(A, C)   # ACMN
    # check vertex orders: square ABXY -> X adj B, Y adj A; BCPQ -> P adj C, Q adj B; ACMN -> M adj C, N adj A
    L1 = (M + P) / 2; L2 = (Q + X) / 2; L3 = (N + Y) / 2
    ar = sp.Rational(1, 2) * abs((L2 - L1)[0]*(L3 - L1)[1] - (L2 - L1)[1]*(L3 - L1)[0])
    return sp.nsimplify(sp.simplify(ar))

orig = area_L(78, 50, 112)
print("original:", orig)
assert orig == 8222
var = area_L(80, 26, 102)
print("variant:", var, float(var))
import random
# independent numeric check with floats, random orientation
import math
def num(AB,BC,AC):
    import cmath
    a,b,c=BC,AC,AB
    cx=(b*b+c*c-a*a)/(2*c); cy=math.sqrt(b*b-cx*cx)
    A,B,C=complex(0,0),complex(c,0),complex(cx,cy)
    # triangle counterclockwise A,B,C; outward for edge P->Q is rotation by -i
    def sq(P,Q): n=(Q-P)*(-1j); return Q+n,P+n
    X,Y=sq(A,B); P,Q=sq(B,C); M,N=sq(C,A)  # for AC: edge C->A ccw; M adj C? sq returns (A+n, C+n)
    N,M=M,N
    L1=(M+P)/2; L2=(Q+X)/2; L3=(N+Y)/2
    z=(L2-L1).conjugate()*(L3-L1); return abs(z.imag)/2
print("numeric check:", num(78,50,112), num(80,26,102))
