# Direct numeric construction (no shortcut formula): F=(0,0) foot of altitude,
# A=(0,h), B=(-b,0), C=(c,0), P=(0,p) with 0<p<h. Scan p, find where X,Y,A collinear.
import math

def circle(P1, P2, P3):
    (x1,y1),(x2,y2),(x3,y3) = P1,P2,P3
    d = 2*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
    ux = ((x1*x1+y1*y1)*(y2-y3)+(x2*x2+y2*y2)*(y3-y1)+(x3*x3+y3*y3)*(y1-y2))/d
    uy = ((x1*x1+y1*y1)*(x3-x2)+(x2*x2+y2*y2)*(x1-x3)+(x3*x3+y3*y3)*(x2-x1))/d
    return (ux, uy), math.hypot(x1-ux, y1-uy)

def second_x(O, r, known):
    # circle meets y=0 at x = ox +- sqrt(r^2-oy^2); return the root other than `known`
    s = math.sqrt(r*r - O[1]**2)
    r1, r2 = O[0]+s, O[0]-s
    return r1 if abs(r1-known) > abs(r2-known) else r2

def reflect(Pt, Q, O):
    dx, dy = O[0]-Q[0], O[1]-Q[1]
    vx, vy = Pt[0]-Q[0], Pt[1]-Q[1]
    t = (dx*vx+dy*vy)/(dx*dx+dy*dy)
    return (Q[0]+2*t*dx-vx, Q[1]+2*t*dy-vy)

def setup(AB, AC, BC):
    b = (AB**2-AC**2+BC**2)/(2*BC); c = BC-b
    return b, c, math.sqrt(AB**2-b**2)

def residual(AB, AC, BC, p):
    b, c, h = setup(AB, AC, BC)
    A, B, C, P = (0,h), (-b,0), (c,0), (0,p)
    O1, r1 = circle(A,P,B); O2, r2 = circle(A,P,C)
    Bp = (second_x(O1,r1,-b), 0); Cp = (second_x(O2,r2,c), 0)
    # check B'X = B'A and X on w1 hold by construction (reflection over line B'O1)
    X = reflect(A,Bp,O1); Y = reflect(A,Cp,O2)
    assert abs(math.hypot(X[0]-O1[0],X[1]-O1[1])-r1) < 1e-7
    assert abs(math.hypot(X[0]-Bp[0],X[1]-Bp[1])-math.hypot(A[0]-Bp[0],A[1]-Bp[1])) < 1e-7
    ux, uy = X[0]-A[0], X[1]-A[1]; wx, wy = Y[0]-A[0], Y[1]-A[1]
    return (ux*wy-uy*wx)/(math.hypot(ux,uy)*math.hypot(wx,wy))

def solve_PA(AB, AC, BC):
    b, c, h = setup(AB, AC, BC)
    N = 200000; sols = []
    ps = [h*(i+0.5)/N for i in range(N)]
    vals = [residual(AB,AC,BC,p) for p in ps]
    for i in range(N-1):
        if vals[i] == 0 or vals[i]*vals[i+1] < 0:
            lo, hi = ps[i], ps[i+1]
            for _ in range(200):
                mid = (lo+hi)/2
                if residual(AB,AC,BC,lo)*residual(AB,AC,BC,mid) <= 0: hi = mid
                else: lo = mid
            p = (lo+hi)/2
            if abs(residual(AB,AC,BC,p)) < 1e-9:
                sols.append(h-p)
    return sols, h

def circumradius(a, b, c):
    s = (a+b+c)/2
    return a*b*c/(4*math.sqrt(s*(s-a)*(s-b)*(s-c)))

for tri, label, expect in [((5,8,7),'ORIGINAL',7*math.sqrt(3)/3), ((13,15,14),'VARIANT',65/8)]:
    pa, h = solve_PA(*tri)
    print(label, 'AB,AC,BC =', tri, '| PA solutions:', pa, '| h =', h,
          '| circumradius =', circumradius(*tri), '| expected', expect,
          '| match:', len(pa)==1 and abs(pa[0]-expect) < 1e-9)
