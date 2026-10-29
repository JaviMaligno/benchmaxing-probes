from sympy import symbols, Eq, solve, Rational
from fractions import Fraction

x = symbols('x')

def symbolic(A, B, k):
    # (A + k x)/B = (A + x)/(B - x), x != 0
    sols = solve(Eq((A + k*x)*(B - x), B*(A + x)), x)
    return [s for s in sols if s != 0 and B - s != 0]

def brute(A, B, k):
    # independent check over positive rationals with small denominator
    found = set()
    for den in range(1, 13):
        for num in range(1, 200 * den):
            v = Fraction(num, den)
            if v >= B:
                break
            if Fraction(A) + k * v == (Fraction(A) + v) / (B - v) * B:
                found.add(v)
    return sorted(found)

orig = symbolic(16, 12, 4)
print("original symbolic:", orig, "brute:", brute(16, 12, 4))
assert orig == [5] and brute(16, 12, 4) == [Fraction(5)]

var = symbolic(18, 15, 3)
print("variant symbolic:", var, "brute:", brute(18, 15, 3))
assert var == [4] and brute(18, 15, 3) == [Fraction(4)]
print("VARIANT ANSWER:", var[0])
