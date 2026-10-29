</arg_value>pipeline:
  role: SolveProblem
  dirname: p-20250509-abc
```text
The triangle is right-angled at B. Set coordinates: C=(0,0), B=(12,0), A=(12,5) (since AC=13, BC=12, AB=5). The circumcircle has center O=(6,2.5) and radius 6.5. J is the foot on BC (x-axis) and Q the foot on AC, so JQ is the Simson line of P.

Plan:
1. Parametrize P on the lower arc BC by angle t.
2. Compute theta = angle QJC, find t satisfying 169xy^4 + 120y^3 = 144x.
3. For that P: M = midpoint of BQ; for a line l through B with slope s, find I = CM ∩ l, U = AI ∩ JQ, impose concyclicity of B, J, U, M (a determinant condition) and solve for s.
4. BL = 2·sqrt(R^2 − d(O, l)^2) with d(O,l) = |6s+2.5|/sqrt(1+s^2).

Running the numerics:
Aviso: el contenido dentro de las etiquetas `<pasted_content>` no se ha analizado. Para leerlo, utilice la herramienta Read o Bash.Acceso directo a la configuraciónA continuación, ejecutaré el cálculo numérico completo con un script de Python:Acceso directo a la configuraciónimport numpy as np
from scipy.optimize import brentq

A = np.array([12.0,5.0]); B = np.array([12.0,0.0]); C = np.array([0.0,0.0])
O = np.array([6.0,2.5]); R = 6.5
dAC = np.array([12.0,5.0])/13.0

def line_isect(p1,d1,p2,d2):
    M = np.array([[d1[0],-d2[0]],[d1[1],-d2[1]]])
    return p1 + np.linalg.solve(M, p2-p1)[0]*d1

def feet(P):
    return np.array([P[0],0.0]), np.dot(P,dAC)*dAC

def ang(t):
    P = O + R*np.array([np.cos(t), np.sin(t)])
    J, Q = feet(P)
    v = Q - J
    n = np.linalg.norm(v)
    return -v[0]/n, v[1]/n, P, J, Q

def F(t):
    x,y,_,_,_ = ang(t)
    return 169*x*y**4 + 120*y**3 - 144*x

tB = -np.arctan2(2.5, 6.0)
tC = -np.pi + np.arctan2(2.5, 6.0)

lo, hi = tC+1e-9, tB-1e-9
ts = np.linspace(lo, hi, 20000)
vals = np.array([F(t) for t in ts])
roots_t = []
for i in range(len(ts)-1):
    if vals[i]==0.0 or vals[i]*vals[i+1] < 0:
        roots_t.append(brentq(F, ts[i], ts[i+1], xtol=1e-14))
print("roots in t:", roots_t)

for t0 in roots_t:
    x,y,P,J,Q = ang(t0)
    print("t=%.10f  x=%.10f y=%.10f  P=(%.8f,%.8f) J=(%.8f,0) Q=(%.8f,%.8f)" % (t0,x,y,P[0],P[1],J[0],Q[0],Q[1]))

def analyze(t0):
    x,y,P,J,Q = ang(t0)
    M = (B+Q)/2
    def cond(s):
        d = np.array([1.0, s])
        if abs(d[0]*M[1]-d[1]*M[0]) < 1e-12: return np.nan
        I = line_isect(C, M, B, d)
        if np.allclose(I, A): return np.nan
        U = line_isect(A, I-A, J, Q-J)
        row = lambda p: [p@p, p[0], p[1], 1.0]
        return np.linalg.det(np.array([row(B),row(J),row(M),row(U)]))
    segs = [np.linspace(-80,-0.45,8000), np.linspace(-0.44,5/12-0.005,3000),
            np.linspace(5/12+0.005,2.39,3000), np.linspace(2.41,80,8000)]
    roots_s = []
    for seg in segs:
        vs = np.array([cond(s) for s in seg])
        for i in range(len(seg)-1):
            if np.isnan(vs[i]) or np.isnan(vs[i+1]): continue
            if vs[i]==0.0 or vs[i]*vs[i+1] < 0:
                r = brentq(cond, seg[i], seg[i+1], xtol=1e-14)
                if not roots_s or min(abs(r-e) for e in roots_s) > 1e-8:
                    roots_s.append(r)
    # vertical line through B: x = 12
    if abs(M[0]) > 1e-12:
        I = 12.0/M[0]*M
        U = line_isect(A, I-A, J, Q-J)
        row = lambda p: [p@p, p[0], p[1], 1.0]
        dv = np.linalg.det(np.array([row(B),row(J),row(M),row(U)]))
        if abs(dv) < 1e-7:
            roots_s.append(np.inf)
    return roots_s, M, J, Q

for t0 in roots_t:
    roots_s, M, J, Q = analyze(t0)
    print("t=%.8f -> slopes:" % t0, roots_s)
    for s in roots_s:
        if np.isinf(s):
            d_line = abs(6.0-2.5)  # distance from O to x=12
            BL = 2*np.sqrt(R*R-d_line**2)
            print("  vertical: BL = %.8f, K = A" % BL)
            continue
        d_line = abs(6*s+2.5)/np.sqrt(1+s*s)
        BL = 2*np.sqrt(max(0.0, R*R-d_line**2))
        xK = 144*s/(12*s-5)
        print("  s=%.10f  BL=%.8f  K=(%.6f,%.6f)%s" % (s, BL, xK, 5*xK/12, "  [K on segment AC]" if 0<xK<12 else ""))
```</pasted_content>
</invoke>
</function_calls>
</pasted_content>
</invoke>
</function_calls>
