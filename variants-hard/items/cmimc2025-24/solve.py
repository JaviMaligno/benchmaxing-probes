# Hexagon ABCDEF side 1, G on CD with CG = t*CD, H on DE with FH || AG (trapezoid AGHF).
# Altitude from H to AG = distance from H to line AG.
from sympy import *
def solve(t):
    P=[Matrix([cos(pi*k/3),sin(pi*k/3)]) for k in range(6)]
    A,B,C,D,E,F=P
    G=C+t*(D-C)
    s=symbols('s')
    H=D+s*(E-D)
    v=G-A
    sol=solve_eq=solve_(H-F,v,s)
    Hs=H.subs(s,sol)
    assert 0<=sol<=1, sol
    w=Hs-A
    dist=Abs(v[0]*w[1]-v[1]*w[0])/sqrt(v.dot(v))
    # sanity: GH not parallel to AF (genuine trapezoid, one pair of parallels)
    return nsimplify(simplify(dist)), sol
def solve_(u,v,s):
    return solve(Eq(u[0]*v[1]-u[1]*v[0],0),s)[0]
from sympy import solve as _s
def solve_(u,v,s): return _s(Eq(u[0]*v[1]-u[1]*v[0],0),s)[0]
orig,so=solve(Rational(1,2))
print("original:",radsimp(orig),"s=",so, "matches 2sqrt39/13:", simplify(orig-2*sqrt(39)/13)==0)
var,sv=solve(Rational(1,3))
print("variant (CG=1/3):",radsimp(var),"s=",sv, float(var))
