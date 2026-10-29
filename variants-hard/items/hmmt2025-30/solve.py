"""hmmt2025-30 variant: plane section of a rectangular prism is a hexagon with given sides;
distance from prism center to plane.
Three checks: (1) exact closed form from opposite-side differences (sympy),
(2) forward construction of a prism+plane realising the sides, (3) independent numeric
inverse solve (random restarts over box dims, normal, offset) showing the distance is unique."""
import itertools, numpy as np, sympy as sp
from scipy.optimize import least_squares

def exact_d2(sides):
    s = [sp.Integer(x) for x in sides]
    dl = [abs(s[i+3]-s[i])/2 for i in range(3)]          # d*w for each pair of parallel faces
    u = [dl[(i+1)%3]**2 + dl[(i+2)%3]**2 - dl[i]**2 for i in range(3)]
    return sp.nsimplify(1/(2*sum(1/v for v in u)))

def section(A,B,C,n,d):
    n = np.array(n,float); n /= np.linalg.norm(n)
    V = [np.array(v) for v in itertools.product([-A,A],[-B,B],[-C,C])]
    pts = []
    for i in range(8):
        for j in range(i+1,8):
            if np.sum(V[i]!=V[j])==1:
                fi, fj = V[i]@n-d, V[j]@n-d
                if fi*fj < 0: pts.append(V[i]+fi/(fi-fj)*(V[j]-V[i]))
    if len(pts) < 3: return None
    P = np.array(pts); c = P.mean(0)
    u = np.cross(n,[1,0,0] if abs(n[0])<.9 else [0,1,0]); u /= np.linalg.norm(u); v = np.cross(n,u)
    P = P[np.argsort(np.arctan2((P-c)@v,(P-c)@u))]
    return [np.linalg.norm(P[(k+1)%len(P)]-P[k]) for k in range(len(P))]

def forward(sides, d2):
    s = sides; d = float(sp.sqrt(d2))
    dl = [abs(s[i+3]-s[i])/2 for i in range(3)]
    al = [(s[i]+s[i+3])/2/(dl[i]/d) for i in range(3)]     # alpha_i = (s+ + s-)/(2w)
    u = [dl[(i+1)%3]**2 + dl[(i+2)%3]**2 - dl[i]**2 for i in range(3)]
    n = np.sqrt([2*d*d/v for v in u])
    P = [(al[1]+al[2])/2, (al[0]+al[2])/2, (al[0]+al[1])/2]
    L = section(*[P[i]/n[i] for i in range(3)], n, d)
    return L

def cyc_match(L, sides):
    s = np.array(sides,float)
    return len(L)==6 and any(np.allclose(np.roll(L,k),t,atol=1e-8) for k in range(6) for t in (s, s[::-1]))

def numeric(sides, trials=250, seed=1):
    rng = np.random.default_rng(seed); s = np.array(sides,float); sc = s.max()
    targets = [np.roll(s,k) for k in range(6)] + [np.roll(s[::-1],k) for k in range(6)]
    def res(x,t):
        A,B,C,th,ph,d = x
        L = section(abs(A),abs(B),abs(C),[np.sin(th)*np.cos(ph),np.sin(th)*np.sin(ph),np.cos(th)],d)
        return np.ones(6)*1e3 if (L is None or len(L)!=6) else np.array(L)-t
    out = []
    for _ in range(trials):
        x0 = np.r_[rng.uniform(.2,1.5,3)*sc, rng.uniform(0,np.pi), rng.uniform(0,2*np.pi), rng.uniform(-.3,.3)*sc]
        r = least_squares(res, x0, args=(targets[rng.integers(12)],))
        if np.max(np.abs(r.fun)) < 1e-7: out.append(abs(r.x[5]))
    return sorted(set(np.round(out,6)))

for name, sides, expected in [("ORIGINAL",[45,66,63,55,54,77],sp.Rational(95,24)),
                              ("VARIANT",[44,60,54,52,50,66],None)]:
    d2 = exact_d2(sides); L = forward(sides, d2); nd = numeric(sides)
    print(name, sides, "d^2 =", d2, " d =", sp.sqrt(d2), "=", float(sp.sqrt(d2)))
    print("  forward construction reproduces sides:", cyc_match(L, sides), np.round(L,6))
    print("  numeric inverse distinct distances:", nd)
    if expected is not None: print("  matches original answer sqrt(95/24):", d2 == expected)
