import sympy as sp
x = sp.symbols('x')

def coeff_sum_of_shift(f, shift):
    g = sp.expand(f.subs(x, x + shift))
    return sum(sp.Poly(g, x).all_coeffs())

orig = coeff_sum_of_shift(3*x**4 + 5*x**2 - 9*x - 2, -1)
print("original:", orig)
assert orig == -2

var = coeff_sum_of_shift(4*x**4 + 3*x**2 - 7*x + 6, -1)
print("variant:", var)
