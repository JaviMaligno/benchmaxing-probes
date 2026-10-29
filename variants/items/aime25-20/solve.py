# Numeric construction of the configuration; arcs computed from coordinates.
import math
import numpy as np

def circ(P, Q, R):
    ax, ay = P; bx, by = Q; cx, cy = R
    d = 2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    ux = ((ax*ax+ay*ay)*(by-cy)+(bx*bx+by*by)*(cy-ay)+(cx*cx+cy*cy)*(ay-by))/d
    uy = ((ax*ax+ay*ay)*(cx-bx)+(bx*bx+by*by)*(ax-cx)+(cx*cx+cy*cy)*(bx-ax))/d
    O = np.array([ux, uy]); return O, np.linalg.norm(P-O)

def second_hit(O, r, P, Q, known):
    # intersections of line PQ with circle; return the one != known, check it lies on segment PQ
    d = Q-P; f = P-O
    a = d@d; b = 2*f@d; c = f@f-r*r
    disc = math.sqrt(b*b-4*a*c)
    ts = [(-b-disc)/(2*a), (-b+disc)/(2*a)]
    pts = [(t, P+t*d) for t in ts]
    t, X = max(pts, key=lambda tp: np.linalg.norm(tp[1]-known))
    assert -1e-9 <= t <= 1+1e-9, "intersection not on segment"
    return X

def solve(Adeg, Bdeg, Cdeg, w=(1, 2, 3)):
    A_, B_, C_ = map(math.radians, (Adeg, Bdeg, Cdeg))
    B = np.array([0.0, 0.0]); C = np.array([1.0, 0.0])
    c = math.sin(C_)/math.sin(A_)  # AB
    A = np.array([c*math.cos(B_), c*math.sin(B_)])
    D, E, F = (B+C)/2, (A+C)/2, (A+B)/2
    O, r = circ(D, E, F)
    G = second_hit(O, r, B, D, D)
    H = second_hit(O, r, A, E, E)
    J = second_hit(O, r, A, F, F)
    ang = lambda P: math.degrees(math.atan2(*(P-O)[::-1])) % 360
    pts = {'G': G, 'D': D, 'E': E, 'H': H, 'J': J, 'F': F}
    order = sorted(pts, key=lambda k: ang(pts[k]))
    # check cyclic order is G,D,E,H,J,F (either orientation)
    seq = ''.join(order); target = 'GDEHJF'
    ok = any(seq == (target*2)[i:i+6] for i in range(6)) or any(seq == (target[::-1]*2)[i:i+6] for i in range(6))
    assert ok, seq
    def arc(p, q):  # minor arc between adjacent points
        d = abs(ang(pts[p]) - ang(pts[q])) % 360
        return min(d, 360-d)
    DE, HJ, FG = arc('D', 'E'), arc('H', 'J'), arc('F', 'G')
    return DE, HJ, FG, w[0]*DE + w[1]*HJ + w[2]*FG

o = solve(84, 60, 36)
print("original arcs DE,HJ,FG:", [round(x, 6) for x in o[:3]], "answer:", round(o[3], 6))
assert round(o[3]) == 336
v = solve(80, 58, 42)
print("variant arcs DE,HJ,FG:", [round(x, 6) for x in v[:3]], "answer:", round(v[3], 6))
