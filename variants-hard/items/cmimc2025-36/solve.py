# Central n-gon of the chord family A_i A_{i+k}: brute-force half-plane intersection
# (numeric) plus exact closed form via sympy (apothem = R cos(pi k/n)).
import itertools, math
import sympy as sp

def central_area(n, k):
    P = [(math.cos(2*math.pi*i/n), math.sin(2*math.pi*i/n)) for i in range(n)]
    lines = []  # a x + b y <= c, half-plane containing the center
    for i in range(n):
        (x1, y1), (x2, y2) = P[i], P[(i+k) % n]
        a, b = y2-y1, x1-x2
        c = a*x1 + b*y1
        if c < 0: a, b, c = -a, -b, -c
        lines.append((a, b, c))
    pts = []
    for (a1,b1,c1),(a2,b2,c2) in itertools.combinations(lines, 2):
        d = a1*b2 - a2*b1
        if abs(d) < 1e-12: continue
        x = (c1*b2 - c2*b1)/d; y = (a1*c2 - a2*c1)/d
        if all(a*x+b*y <= c+1e-9 for a,b,c in lines):
            pts.append((x, y))
    uniq = []
    for p in pts:
        if all(math.hypot(p[0]-q[0], p[1]-q[1]) > 1e-7 for q in uniq): uniq.append(p)
    pts = sorted(uniq, key=lambda p: math.atan2(p[1], p[0]))
    assert len(pts) == n, len(pts)
    return 0.5*abs(sum(pts[i][0]*pts[(i+1)%len(pts)][1]-pts[(i+1)%len(pts)][0]*pts[i][1] for i in range(len(pts))))

def ratio(n, k1, k2):
    num = central_area(n, k1)/central_area(n, k2)
    ex = (sp.cos(sp.pi*k1/n)/sp.cos(sp.pi*k2/n))**2
    return num, ex

# Original: n=24, k1=9 (3 stars), k2=11 (one star)
num, ex = ratio(24, 9, 11)
orig = 3 + sp.sqrt(2) + sp.sqrt(3) + sp.sqrt(6)
print("original numeric:", num, " exact:", ex, " expected:", float(orig))
assert abs(num - float(orig)) < 1e-9 and abs(sp.N(ex - orig, 50)) < 1e-40

# Variant: n=24, k1=10 (2 stars), k2=11 (one star)
print("gcd checks:", math.gcd(24,10), math.gcd(24,11))
num, ex = ratio(24, 10, 11)
print("variant numeric:", num, " exact(50 d):", sp.N(ex, 30))
cand = sp.nsimplify(sp.N(ex, 60), [sp.sqrt(2), sp.sqrt(3)])
print("closed form:", cand, " diff:", sp.N(ex - cand, 50))
assert abs(sp.N(ex - cand, 60)) < 1e-45 and abs(num - float(cand)) < 1e-9
print("VARIANT ANSWER:", cand)
