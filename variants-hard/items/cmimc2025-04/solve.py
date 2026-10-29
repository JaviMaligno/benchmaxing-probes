# a=log_x y, b=log_y z, c=log_z x, abc=1.
# Eq1: a+b+c=S ; Eq3: log_z y + log_x z = ca + ab = T ; Eq2: log_{1/a} z = k -> z=(1/a)^k
import sympy as sp, math
def solve(S, k, T):
    a,b,c = sp.symbols('a b c')
    sols = sp.solve([a+b+c-S, a*b+a*c-T, a*b*c-1],[a,b,c],dict=True)
    zs=set()
    for s in sols:
        av,bv,cv=[complex(s[v]) for v in (a,b,c)]
        if any(abs(t.imag)>1e-12 for t in (av,bv,cv)): continue
        av,bv,cv=av.real,bv.real,cv.real
        if min(av,bv,cv)<=0: continue  # need real logs with positive bases (x,y,z>1 branch)
        z=(1/av)**k
        # independent numeric check: build x,y,z and evaluate the original equations
        x=z**cv; y=x**av
        L=lambda base,v: math.log(v)/math.log(base)
        assert abs(L(x,y)+L(y,z)+L(z,x)-S)<1e-6
        assert abs(L(L(y,x),z)-k)<1e-6
        assert abs(L(z,y)+L(x,z)-T)<1e-6
        zs.add(round(z,6))
    return zs
orig=solve(8,-3,16); print("original:",orig); assert orig=={64.0}
var=solve(10,-3,25); print("variant:",var)
