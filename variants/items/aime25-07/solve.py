from fractions import Fraction
from math import gcd

def pairings(items):
    if not items:
        yield []
        return
    a = items[0]
    for i in range(1, len(items)):
        b = items[i]
        rest = items[1:i] + items[i+1:]
        for p in pairings(rest):
            yield [(a, b)] + p

def prob_last_contains(n, target):
    letters = list(range(n))
    tot = good = 0
    for p in pairings(letters):
        words = sorted(tuple(sorted(w)) for w in p)
        tot += 1
        if target in words[-1]:
            good += 1
    return Fraction(good, tot)

# Original: 12 letters A..L, target G (index 6)
fo = prob_last_contains(12, 6)
print("original prob", fo, "m+n =", fo.numerator + fo.denominator)
assert fo.numerator + fo.denominator == 821

# Variant: 12 letters A..L, target H (index 7)
fv = prob_last_contains(12, 7)
print("variant prob", fv, "m+n =", fv.numerator + fv.denominator)
