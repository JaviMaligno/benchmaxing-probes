"""hmmt2024-28 variant check.
Numerically constructs pentagon ABTCD (TB, TC, angle BTC, angle ATD, area S),
solving AB=CD, area=S and the tangency condition at T, then independently
verifies internal tangency of circles (TAB),(TCD) via circumcentres and convexity.
Compares [TAD] with closed form 2(S + TB*TC/2)(2-sqrt3) (beta=120, delta=90)."""
from mpmath import mp, cos, sin, pi, sqrt, findroot, acos
import itertools
mp.dps = 40
r = pi/180

def config(TB, TC, beta, delta, a, d, al):
    T = (0, 0); B = (TB, 0)
    A = (a*cos(al*r), a*sin(al*r)); D = (d*cos((al+delta)*r), d*sin((al+delta)*r))
    C = (TC*cos(beta*r), TC*sin(beta*r))
    return T, A, B, C, D

def dist(P, Q): return sqrt((P[0]-Q[0])**2 + (P[1]-Q[1])**2)
def ang(P, Q, R):
    v = (P[0]-Q[0], P[1]-Q[1]); w = (R[0]-Q[0], R[1]-Q[1])
    return acos((v[0]*w[0]+v[1]*w[1])/(dist(P, Q)*dist(R, Q)))/r
def area(P):
    n = len(P); return abs(sum(P[i][0]*P[(i+1) % n][1]-P[(i+1) % n][0]*P[i][1] for i in range(n)))/2
def circumcentre(P, Q, R):
    ax, ay = P; bx, by = Q; cx, cy = R
    D = 2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux = ((ax**2+ay**2)*(by-cy)+(bx**2+by**2)*(cy-ay)+(cx**2+cy**2)*(ay-by))/D
    uy = ((ax**2+ay**2)*(cx-bx)+(bx**2+by**2)*(ax-cx)+(cx**2+cy**2)*(bx-ax))/D
    return (ux, uy)
def convex(P):
    n = len(P); s = []
    for i in range(n):
        p, q, w = P[i], P[(i+1) % n], P[(i+2) % n]
        s.append((q[0]-p[0])*(w[1]-q[1])-(q[1]-p[1])*(w[0]-q[0]))
    return all(x > 0 for x in s) or all(x < 0 for x in s)

def solve(TB, TC, beta, delta, S):
    sols = []
    def F(a, d, al):
        T, A, B, C, D = config(TB, TC, beta, delta, a, d, al)
        # tangent-chord: tangency at T  <=>  angle TAB + angle TDC = 180 - beta
        return [dist(A, B)-dist(C, D), ang(T, A, B)+ang(T, D, C)-(180-beta), area([A, B, T, C, D])-S]
    for g in itertools.product([2, 4, 6, 8, 10], [2, 4, 6, 8, 10], [3, 10, 20, beta-delta-3]):
        try: a, d, al = findroot(F, g)
        except Exception: continue
        if not (a > 0 and d > 0 and 0 < al < beta-delta): continue
        T, A, B, C, D = config(TB, TC, beta, delta, a, d, al)
        if not convex([A, B, T, C, D]): continue
        O1, O2 = circumcentre(T, A, B), circumcentre(T, C, D)
        R1, R2 = dist(O1, T), dist(O2, T)
        if abs(dist(O1, O2)-abs(R1-R2)) > mp.mpf(10)**-20: continue  # internal tangency
        val = area([T, A, D])
        if not any(abs(val-v) < 1e-15 for v in sols): sols.append(val)
    return sols

orig = solve(4, 5, 120, 90, 22)
print("original [TAD]:", [mp.nstr(v, 20) for v in orig], " expected 64(2-sqrt3) =", mp.nstr(64*(2-sqrt(3)), 20))
assert len(orig) == 1 and abs(orig[0]-64*(2-sqrt(3))) < 1e-20
var = solve(3, 6, 120, 90, 27)
closed = 2*(27+3*6/mp.mpf(2))*(2-sqrt(3))
print("variant [TAD]:", [mp.nstr(v, 20) for v in var], " closed form 72(2-sqrt3) =", mp.nstr(closed, 20))
assert len(var) == 1 and abs(var[0]-closed) < 1e-20
print("OK")
