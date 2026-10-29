# Min axis ratio of an ellipse through right trapezoid D=(0,0), C=(q,0), A=(0,h), B=(p,h).
import numpy as np, sympy as sp
from scipy.optimize import minimize_scalar

def exact(p,h,q):
    # conic x^2 + Bxy + Cy^2 + Dx + Ey + F = 0 through the 4 points
    Bc,Cc,Dc,Ec,F=sp.symbols('B C D E F'); x,y=sp.symbols('x y')
    con=x**2+Bc*x*y+Cc*y**2+Dc*x+Ec*y+F
    sol=sp.solve([con.subs({x:X,y:Y}) for X,Y in [(0,0),(q,0),(0,h),(p,h)]],[Bc,Dc,Ec,F],dict=True)[0]
    Bv=sol[Bc]; k=Bv**2/4
    C=sp.symbols('C',positive=True)
    f=(1+C)**2/(C-k)          # = r + 1/r + 2, r = eigenvalue ratio
    crit=[c for c in sp.solve(sp.diff(f,C),C) if c>k]
    val=sp.nsimplify(min(f.subs(C,c) for c in crit))
    s=sp.symbols('s',positive=True)  # s = axis ratio = sqrt(r)
    roots=[r for r in sp.solve(sp.Eq((s+1/s)**2,val),s) if r>=1]
    return sp.nsimplify(roots[0]), float(Bv)

def numeric(p,h,q):
    Bv=(q-p)/h  # from point constraints
    def ratio(C):
        M=np.array([[1,Bv/2],[Bv/2,C]]); ev=np.linalg.eigvalsh(M)
        if ev[0]<=0: return 1e9
        # also check the conic is a real ellipse: center value sign
        Dv,Ev=-q,-h*C; L=np.array([Dv,Ev])
        ctr=np.linalg.solve(2*M,-L); val=0.5*L@ctr
        if val>=0: return 1e9
        return np.sqrt(ev[1]/ev[0])
    res=minimize_scalar(ratio,bounds=(Bv**2/4+1e-9,1e4),method='bounded',options={'xatol':1e-12})
    return res.fun

for name,(p,h,q) in {"original":(18,33,130),"variant":(20,28,110)}.items():
    e,_=exact(p,h,q); n=numeric(p,h,q)
    print(name,(p,h,q),"exact:",e,"numeric:",n)
assert exact(18,33,130)[0]==sp.Rational(11,3)
