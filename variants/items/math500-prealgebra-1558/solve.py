from fractions import Fraction as F
import math

def dist(legs):
    # legs: list of (dx, dy) exact displacements
    x = sum(l[0] for l in legs); y = sum(l[1] for l in legs)
    sq = x*x + y*y
    return sq, math.sqrt(sq)

# Original: 1/2 S, 3/4 E, 1/2 S
sq, d = dist([(0, -F(1,2)), (F(3,4), 0), (0, -F(1,2))])
print("original squared distance:", sq, "distance:", round(d, 2))
assert round(d, 2) == 1.25

# Variant: 3/4 N, 2 W, 3/4 N
sq, d = dist([(0, F(3,4)), (-2, 0), (0, F(3,4))])
print("variant squared distance:", sq, "distance:", f"{d:.2f}")
assert sq == F(25,4)
