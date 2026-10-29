from sympy import symbols, factor_list, Poly, ZZ
x = symbols('x')

def answer(expr):
    c, facs = factor_list(expr, x, domain=ZZ)
    assert c == 1
    total = 0
    for f, m in facs:
        p = Poly(f, x)
        assert p.LC() == 1 and p.degree() > 0
        total += m * p.eval(1)
    return total, facs

orig, of = answer(x**8 + 3*x**4 - 4)
print("original factors:", of, "sum:", orig)
assert orig == 10
var, vf = answer(x**8 + 63*x**4 - 64)
print("variant factors:", vf, "sum:", var)
