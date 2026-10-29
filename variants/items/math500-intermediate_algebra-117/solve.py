from sympy import symbols, rem, expand, solve, Poly
x,a,b,c,d,e=symbols('x a b c d e')

def solve_item(r1,r2,s1,s2,k,P0,target):
    P = x**3 + a*x**2 + b*x + P0
    R = c*x + d
    eqs = []
    eqs += Poly(expand(rem(P,(x-r1)*(x-r2),x) - R), x).all_coeffs()
    eqs += Poly(expand(rem(P,(x-s1)*(x-s2),x) - k*R), x).all_coeffs()
    sols = solve(eqs,[a,b,c,d],dict=True)
    assert len(sols)==1, sols
    s = sols[0]
    Ps = P.subs(s)
    # independent check of the remainder conditions
    Rs = R.subs(s)
    assert expand(rem(Ps,(x-r1)*(x-r2),x)-Rs)==0
    assert expand(rem(Ps,(x-s1)*(x-s2),x)-k*Rs)==0
    return Ps.subs(x,target), expand(Ps)

orig, Po = solve_item(1,4,2,3,2,5,5)
print("original P(x) =", Po, " P(5) =", orig)
assert orig == 15
var, Pv = solve_item(1,5,2,4,2,7,6)
print("variant P(x) =", Pv, " P(6) =", var)
