from sympy import sqrt, Rational, nsimplify, simplify, N

def expr(base, a, b, c, d, e):
    # sqrt( (a/sqrt(b) + sqrt(c)/d + sqrt(e)) / sqrt(base) )
    return sqrt((a/sqrt(b) + sqrt(c)/d + sqrt(e)) / sqrt(base))

def solve(*args):
    v = simplify(expr(*args))
    num = N(expr(*args), 50)
    r = nsimplify(num, rational=True, tolerance=1e-40)
    assert abs(N(v - r, 50)) < 1e-40
    return r, num

orig, on = solve(5, 5, 80, 845, 9, 45)
print("original:", orig, on)
assert orig == Rational(13, 6)

var, vn = solve(7, 7, 63, 847, 12, 175)
print("variant:", var, vn)
