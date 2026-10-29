import sympy as sp

def solve(AB, AC, AT):
    AB, AC, AT = map(sp.Integer, (AB, AC, AT))
    # power of A wrt both diameter circles equals AT^2 (T on radical axis)
    ABp, ACp = AT**2/AB, AT**2/AC
    AM, AN = (AB+ABp)/2, (AC+ACp)/2          # centers of the diameter circles
    MN = (AB-ABp)/2 + (AC-ACp)/2              # external tangency
    cosA = (AM**2+AN**2-MN**2)/(2*AM*AN)
    sinA = sp.sqrt(1-cosA**2)
    AO = sp.nsimplify(MN/sinA)                # A,M,O,N concyclic with diameter AO
    # independent coordinate check
    A = sp.Matrix([0,0]); u = sp.Matrix([1,0]); v = sp.Matrix([cosA, sinA])
    B, Bp, C, Cp = AB*u, ABp*u, AC*v, ACp*v
    x, y = sp.symbols('x y'); O = sp.Matrix([x,y])
    sol = sp.solve([(O-B).dot(O-B)-(O-Bp).dot(O-Bp), (O-C).dot(O-C)-(O-Cp).dot(O-Cp)], [x,y], dict=True)[0]
    Ov = O.subs(sol)
    assert sp.simplify((Ov-B).norm()-(Ov-Cp).norm()) == 0   # B,B',C,C' concyclic
    M, N = (B+Bp)/2, (C+Cp)/2; r1, r2 = (AB-ABp)/2, (AC-ACp)/2
    assert sp.simplify((M-N).norm()-(r1+r2)) == 0           # externally tangent
    T = M + (N-M)*r1/(r1+r2)
    assert sp.simplify(T.norm()-AT) == 0                    # AT reproduced
    assert sp.simplify(Ov.norm()-AO) == 0
    assert 0 < ABp < AB and 0 < ACp < AC
    return sp.simplify(AO)

orig = solve(18, 36, 12)
print("original:", orig); assert orig == sp.Rational(65, 3)
var = solve(25, 45, 15)
print("variant:", var)
