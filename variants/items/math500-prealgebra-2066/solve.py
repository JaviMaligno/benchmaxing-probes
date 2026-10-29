from fractions import Fraction as F
import math

def solve(total, pound_usd, euro_usd):
    half = F(total) / 2
    pounds = half / F(pound_usd)
    euros = half / F(euro_usd)
    diff = euros - pounds
    # round to nearest whole number (half-up); check not ambiguous
    r = math.floor(diff + F(1, 2))
    assert diff - math.floor(diff) != F(1, 2)
    return diff, r

d0, r0 = solve(300, "1.64", "1.32")
print("original diff =", float(d0), "-> rounded", r0)
assert r0 == 22

d1, r1 = solve(400, "1.28", "1.10")
print("variant diff =", float(d1), "-> rounded", r1)
# independent float check
print("float check:", round(200/1.10 - 200/1.28))
