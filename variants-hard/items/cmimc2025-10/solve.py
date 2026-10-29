from fractions import Fraction
import sympy as sp

def run(a0, rec, num, den, k, c, N=6):
    # exact partial sums
    a = a0; s = Fraction(0)
    for n in range(N):
        s += Fraction(k**n * num(a), den(a))
        a = rec(a)
    # remainder of telescoping: k^N/(a_N + c); confirm s + k^N/(a_N+c) is the closed form
    closed = s + Fraction(k**N, a + c)
    return s, closed

x = sp.symbols('x')
def check_identity(rec, num, den, k, c):
    lhs = sp.Rational(1)/(x+c) - k/(rec(x)+c)
    return sp.simplify(lhs - num(x)/den(x)) == 0

# ORIGINAL
orec = lambda a: a**3+5*a**2+10*a+6
onum = lambda a: a+1
oden = lambda a: a**2+3*a+4
assert check_identity(orec, onum, oden, 2, 2)
s, closed = run(2024, orec, onum, oden, 2, 2)
print("original closed form:", closed, " partial-sum gap:", float(Fraction(1,2026)-s))
assert closed == Fraction(1, 2026)

# VARIANT
vrec = lambda a: a**3+7*a**2+18*a+15
vnum = lambda a: a+1
vden = lambda a: a**2+4*a+6
assert check_identity(vrec, vnum, vden, 3, 3)
s, closed = run(2025, vrec, vnum, vden, 3, 3)
print("variant closed form:", closed, " partial-sum gap:", float(Fraction(1,2028)-s))
assert closed == Fraction(1, 2028)
# independent numeric check: partial sum within 1e-100 of answer
assert 0 < Fraction(1,2028) - s < Fraction(1,10**100)
print("VARIANT ANSWER:", Fraction(1,2028))
