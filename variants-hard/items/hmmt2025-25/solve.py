# Numeric brute-force geometry + exact closed form, for original and variant.
import math, sympy as sp

def numeric(s, a):
    R = s/math.sqrt(3)
    A = (0.0, R); B = (-s/2, -R/2); C = (s/2, -R/2)
    def inside(P):
        def cr(o,p,q): return (p[0]-o[0])*(q[1]-o[1])-(p[1]-o[1])*(q[0]-o[0])
        d=[cr(A,B,P),cr(B,C,P),cr(C,A,P)]
        return all(x>1e-12 for x in d) or all(x<-1e-12 for x in d)
    def ang(P):
        u=(B[0]-P[0],B[1]-P[1]); v=(C[0]-P[0],C[1]-P[1])
        return math.degrees(math.acos((u[0]*v[0]+u[1]*v[1])/math.hypot(*u)/math.hypot(*v)))
    sols=set()
    # X on circumcircle with AX=a: central angle t with chord 2R sin(t/2)=a
    t = 2*math.asin(a/(2*R))
    for sg in (1,-1):
        th = math.pi/2 + sg*t
        X = (R*math.cos(th), R*math.sin(th))
        # P lies on line through X perpendicular to AX (angle AXP=90); scan along it
        d = (A[0]-X[0], A[1]-X[1]); n = (-d[1], d[0]); L = math.hypot(*n); n=(n[0]/L,n[1]/L)
        f = lambda k: ang((X[0]+k*n[0], X[1]+k*n[1])) - 120
        N=200000; lo=-3*s; hi=3*s; prev=None
        for i in range(N+1):
            k=lo+(hi-lo)*i/N; P=(X[0]+k*n[0],X[1]+k*n[1])
            try: v=f(k)
            except Exception: prev=None; continue
            if prev is not None and (prev[1]<0)!=(v<0):
                a1,b1=prev[0],k
                for _ in range(80):
                    m=(a1+b1)/2
                    if (f(a1)<0)!=(f(m)<0): b1=m
                    else: a1=m
                Pm=(X[0]+a1*n[0],X[1]+a1*n[1])
                if inside(Pm): sols.add(round(abs(a1),9))
            prev=(k,v)
    return sols

def exact(s, a):
    R = sp.Integer(s)/sp.sqrt(3)
    return sp.nsimplify(sp.sqrt(4*R**2 - a**2) - R)

for name,(s,a) in {"original":(6,5),"variant":(9,7)}.items():
    e = exact(s,a)
    print(name, "numeric XP:", numeric(s,a), "exact:", e, "=", float(e))
orig = exact(6,5)
print("original matches sqrt(23)-2sqrt(3):", sp.simplify(orig-(sp.sqrt(23)-2*sp.sqrt(3)))==0)
