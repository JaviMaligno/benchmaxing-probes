from fractions import Fraction
import math

def speed_over_pi(radius, revs, secs):
    # circumference = 2*pi*r ; speed = circumference * revs/secs ; return coefficient of pi
    return Fraction(2 * radius) * Fraction(revs, secs)

orig = speed_over_pi(9, 2, 3)
assert orig == 12, orig
print("original:", f"{orig}*pi")

var = speed_over_pi(7, 3, 2)
# independent numeric check: distance over a long time / time
t = 2000
dist = (3 / 2) * t * 2 * math.pi * 7
assert abs(dist / t - float(var) * math.pi) < 1e-9
print("variant:", f"{var}*pi", "=", float(var) * math.pi)
