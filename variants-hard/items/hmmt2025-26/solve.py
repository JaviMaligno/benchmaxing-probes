from sympy import *

def circ(P,Q,R):
    x,y=symbols('x y')
    s=solve([ (x-P[0])**2+(y-P[1])**2-(x-Q[0])**2-(y-Q[1])**2,
              (x-P[0])**2+(y-P[1])**2-(x-R[0])**2-(y-R[1])**2],[x,y],dict=True)[0]
    return (s[x],s[y])

def area(AB,BC,CD,DA):
    # D=(0,0), C=(CD,0), A=(p,h), B=(p+AB,h)
    p,h=symbols('p h',real=True)
    sol=[s for s in solve([p**2+h**2-DA**2,(CD-p-AB)**2+h**2-BC**2],[p,h],dict=True) if s[h].is_positive][0]
    p,h=sol[p],sol[h]
    A=(p,h);B=(p+AB,h);C=(Rational(CD),0);D=(0,0)
    O=[circ(A,B,C),circ(B,C,D),circ(C,D,A),circ(D,A,B)]
    s=sum(O[i][0]*O[(i+1)%4][1]-O[(i+1)%4][0]*O[i][1] for i in range(4))
    return nsimplify(simplify(abs(s)/2))

orig=area(11,8,19,4)
print("original:",orig, "matches 9*sqrt(15):", simplify(orig-9*sqrt(15))==0)
var=area(10,7,18,5)
print("variant:",var, N(var))
# numeric cross-check with floats
import math
def num(AB,BC,CD,DA):
    d=CD-AB; p=(DA**2-BC**2+d**2)/(2*d); h=math.sqrt(DA**2-p**2)
    pts=[(p,h),(p+AB,h),(CD,0),(0,0)]
    def cc(a,b,c):
        ax,ay=a;bx,by=b;cx,cy=c
        dd=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
        ux=((ax*ax+ay*ay)*(by-cy)+(bx*bx+by*by)*(cy-ay)+(cx*cx+cy*cy)*(ay-by))/dd
        uy=((ax*ax+ay*ay)*(cx-bx)+(bx*bx+by*by)*(ax-cx)+(cx*cx+cy*cy)*(bx-ax))/dd
        return ux,uy
    A,B,C,D=pts
    O=[cc(A,B,C),cc(B,C,D),cc(C,D,A),cc(D,A,B)]
    return abs(sum(O[i][0]*O[(i+1)%4][1]-O[(i+1)%4][0]*O[i][1] for i in range(4)))/2
print("numeric orig:",num(11,8,19,4),9*math.sqrt(15))
print("numeric variant:",num(10,7,18,5))
