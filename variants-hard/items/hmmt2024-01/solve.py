# Variant of HMMT Feb 2024 #1: a,b,c nonzero reals; x^2+ax+b has roots b and c;
# x^2+cx+a has root k. Find b.  Original: k=5 -> 29.  Variant: k=7.
from sympy import symbols, solve, expand, Poly

def solve_for(k):
    a, b, c, x = symbols('a b c x')
    eqs = [b**2 + a*b + b,            # b is a root of x^2+ax+b
           c**2 + a*c + b,            # c is a root
           k**2 + c*k + a]            # k is a root of x^2+cx+a
    sols = solve(eqs, [a, b, c], dict=True)
    good = []
    for s in sols:
        if all(v.is_real and v != 0 for v in s.values()):
            # double-check: roots of x^2+ax+b are exactly {b, c} (as multiset)
            p = Poly(x**2 + s[a]*x + s[b], x)
            q = expand((x - s[b])*(x - s[c]))
            if expand(p.as_expr() - q) == 0:
                good.append(s)
    return good

orig = solve_for(5)
print("original:", orig)
assert len({s[symbols('b')] for s in orig}) == 1 and orig[0][symbols('b')] == 29
var = solve_for(7)
print("variant:", var)
bs = {s[symbols('b')] for s in var}
assert len(bs) == 1
print("variant answer b =", bs.pop())
