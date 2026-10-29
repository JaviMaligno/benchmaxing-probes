# Brute-force count of integer pairs (x,y) in [-N,N]^2 with a x^2 + b xy + c y^2 = 0
import sympy as sp

def count(a, b, c, N):
    return sum(1 for x in range(-N, N + 1) for y in range(-N, N + 1)
               if a*x*x + b*x*y + c*y*y == 0)

x, y = sp.symbols('x y')
# Original: 12x^2 - xy - 6y^2 = 0, range [-100,100], expected 117
orig = count(12, -1, -6, 100)
print("original factor:", sp.factor(12*x**2 - x*y - 6*y**2), "count:", orig)
assert orig == 117
# Variant: 10x^2 + 7xy - 12y^2 = 0, range [-100,100]
var = count(10, 7, -12, 100)
print("variant factor:", sp.factor(10*x**2 + 7*x*y - 12*y**2), "count:", var)
