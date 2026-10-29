from sympy import symbols, Rational, solve, expand, Poly, simplify
x = symbols('x')
def f0(points, at=0):
    # Generic rational f = (p2 x^2+p1 x+p0)/(q2 x^2+q1 x+q0); solve linear system f(n)=n^3, q0 normalized.
    p2,p1,p0,q2,q1 = symbols('p2 p1 p0 q2 q1')
    q0 = 1
    P = p2*x**2+p1*x+p0; Q = q2*x**2+q1*x+q0
    eqs = [P.subs(x,n) - n**3*Q.subs(x,n) for n in points]
    sol = solve(eqs, [p2,p1,p0,q2,q1], dict=True)
    assert len(sol)==1
    Ps, Qs = P.subs(sol[0]), Q.subs(sol[0])
    for n in points: assert simplify(Ps.subs(x,n)/Qs.subs(x,n) - n**3)==0
    return simplify(Ps.subs(x,at)/Qs.subs(x,at))
def f0_method(points, at=0):
    # Independent: P - x^3 Q = c*prod(x-a); top 3 coeffs determine Q (c=-q2), lower 3 give P.
    R = expand(-Poly([1],x).as_expr()*1)
    pr = expand(-1*__import__('sympy').prod([x-a for a in points]))  # c=-1 so q2=1
    co = Poly(pr, x).all_coeffs()  # deg5..0
    Q = -(co[0]*x**2+co[1]*x+co[2])
    P = co[3]*x**2+co[4]*x+co[5]
    return Rational(P.subs(x,at))/Q.subs(x,at)
orig = f0([1,2,3,4,5]); print("original:", orig, f0_method([1,2,3,4,5]))
assert orig == Rational(24,17)
var = f0([1,2,3,4,6]); print("variant:", var, f0_method([1,2,3,4,6]))
assert var == f0_method([1,2,3,4,6])
