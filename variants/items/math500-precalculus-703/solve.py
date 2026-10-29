import numpy as np, sympy as sp, math

def theta_sum(deg):
    # alternating polynomial z^deg - z^(deg-1) + ... + 1 (deg even)
    coeffs = [(-1)**i for i in range(deg+1)]
    roots = np.roots(coeffs)
    thetas = [(math.atan2(r.imag, r.real)) % (2*math.pi) for r in roots]
    assert all(abs(abs(r)-1) < 1e-9 for r in roots)
    num = sum(thetas)
    # exact: roots are z^(deg+1) = -1, z != -1
    n = deg + 1
    exact = sum(sp.Rational(2*k+1, n)*sp.pi for k in range(n) if sp.Rational(2*k+1, n) != 1)
    assert abs(float(exact) - num) < 1e-8, (exact, num)
    return sp.nsimplify(exact / sp.pi) * sp.pi

orig = theta_sum(8)
print("original:", orig)
assert sp.simplify(orig - 8*sp.pi) == 0
var = theta_sum(10)
print("variant:", var)
