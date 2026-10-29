# Brute force over all assignments of the four areas to PAB, PBC, PCD, PDA.
# Square A(0,0) B(s,0) C(s,s) D(0,s), P=(x,y) inside.
# [PAB]=s*y/2, [PBC]=s*(s-x)/2, [PCD]=s*(s-y)/2, [PDA]=s*x/2.
from itertools import permutations
from sympy import sqrt, Rational, nsimplify, simplify, sqrtdenest, radsimp

def solve(areas):
    results = set()
    for a1, a2, a3, a4 in permutations(areas):
        S = sum(areas)
        s = sqrt(S)
        y = 2 * a1 / s
        x_from_bc = s - 2 * a2 / s
        y_from_cd = s - 2 * a3 / s
        x = 2 * a4 / s
        if simplify(x - x_from_bc) != 0 or simplify(y - y_from_cd) != 0:
            continue
        if not (0 < x < s and 0 < y < s):
            continue
        pts = [(0, 0), (s, 0), (s, s), (0, s)]
        prod = 1
        for (u, v) in pts:
            prod *= sqrt((x - u) ** 2 + (y - v) ** 2)
        val = radsimp(sqrtdenest(simplify(prod)))
        results.add(simplify(val))
    return results

orig = solve([1, 2, 3, 4])
print("original:", orig, [float(r) for r in orig])
assert len(orig) == 1 and simplify(list(orig)[0] - 8 * sqrt(10)) == 0
print("original check OK (8*sqrt(10))")

var = solve([3, 4, 6, 7])
print("variant:", var, [float(r) for r in var])
assert len(var) == 1
assert simplify(list(var)[0] - 3 * sqrt(1105)) == 0
# independent numeric check
import math
s = math.sqrt(20); y = 2*3/s; x = 2*4/s
num = 1
for (u, v) in [(0,0),(s,0),(s,s),(0,s)]: num *= math.hypot(x-u, y-v)
print("numeric:", num, "3*sqrt(1105) =", 3*math.sqrt(1105))
