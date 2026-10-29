import sympy as sp
x, y = sp.symbols('x y')

def product_y(a, b, c):
    # y = x^2 - a, y^2 = b*x + c ; distinct solutions (x,y)
    sols = sp.solve([sp.Eq(y, x**2 - a), sp.Eq(y**2, b*x + c)], [x, y], dict=True)
    pts = {(sp.nsimplify(sp.simplify(s[x])), sp.simplify(s[y])) for s in sols}
    # independent numeric check of distinctness / count
    num = sp.Poly((x**2 - a)**2 - (b*x + c), x).nroots()
    assert len(set(round(complex(r).real, 9) + 1j*round(complex(r).imag, 9) for r in num)) == len(pts)
    p = sp.simplify(sp.prod([s[1] for s in pts]))
    pn = 1
    for r in num:
        pn *= (r**2 - a)
    assert abs(complex(pn) - complex(p)) < 1e-6
    return sp.nsimplify(p), len(pts)

orig, n0 = product_y(8, -5, 44)
print("original:", orig, "num solutions:", n0)
assert orig == 1736
var, n1 = product_y(7, -9, 45)
print("variant:", var, "num solutions:", n1)
