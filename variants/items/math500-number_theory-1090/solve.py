from fractions import Fraction

def terminates(n):
    while n % 2 == 0: n //= 2
    while n % 5 == 0: n //= 5
    return n == 1

def solve(limit):
    odds = [n for n in range(1, limit) if n % 2 == 1]
    good = sum(1 for n in odds if terminates(n))
    p = Fraction(good, len(odds))
    return p, p.numerator + p.denominator

p0, a0 = solve(2010)
print("original:", p0, a0)
assert a0 == 202
p1, a1 = solve(4000)
print("variant:", p1, a1)
