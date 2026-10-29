from fractions import Fraction as Fr
import math

def shoelace(P):
    s = 0
    for i in range(len(P)):
        x1,y1 = P[i]; x2,y2 = P[(i+1)%len(P)]
        s += x1*y2 - x2*y1
    return abs(s)/2

def solve(AD, DE, EB, AF, FG, GC, quad_area, cx=Fr(3,7)):
    # A at origin, AB on x-axis; C = AC*(cos, sin) with arbitrary shape; scale height to match area.
    AB = AD+DE+EB; AC = AF+FG+GC
    # place C at (AC*cx, h) param: choose h then rescale y so [DEGF] = quad_area
    def pts(h):
        A=(Fr(0),Fr(0)); B=(Fr(AB),Fr(0))
        C=(Fr(AC)*cx, h)
        on = lambda P,t: (P[0]*t, P[1]*t)
        D=(Fr(AD),Fr(0)); E=(Fr(AD+DE),Fr(0))
        F=on(C,Fr(AF,AC)); G=on(C,Fr(AF+FG,AC))
        M=(2*F[0]-D[0], 2*F[1]-D[1]); N=(2*E[0]-G[0], 2*E[1]-G[1])
        return A,B,C,D,E,F,G,M,N
    # area is linear in h (affine shear in x preserves areas; y scaling linear)
    p = pts(Fr(1))
    q1 = shoelace([p[3],p[4],p[6],p[5]])
    h = Fr(quad_area)/q1
    A,B,C,D,E,F,G,M,N = pts(h)
    hept = shoelace([A,F,N,B,C,E,M])
    tri = shoelace([A,B,C])
    return hept, tri

for cx in (Fr(3,7), Fr(0), Fr(2), Fr(-1,3)):
    o = solve(4,16,8,13,52,26,288,cx)
    v = solve(3,9,6,5,15,10,300,cx)
    print("cx",cx,"original heptagon",o[0],"tri",o[1],"| variant heptagon",v[0],"tri",v[1])
o = solve(4,16,8,13,52,26,288)
assert o[0] == 588, o
print("ORIGINAL answer reproduced:", o[0])
v = solve(3,9,6,5,15,10,300)
print("VARIANT answer:", v[0])
