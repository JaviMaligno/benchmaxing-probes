# Brute force: assign the 5 given distances to 5 vertices (A,B | C,D | E,F of a regular
# octahedron centred at the origin, vertices (+-a,0,0),(0,+-a,0),(0,0,+-a)), sixth = F unknown.
# Opposite pairs must have equal sums of squared distances. For each consistent assignment,
# actually construct P and a and verify all six distances numerically.
from itertools import permutations
import sympy as sp

def solve(ds):
    answers = set()
    for p in permutations(ds):
        A, B, C, D, E = [sp.Integer(v) ** 2 for v in p]
        if A + B != C + D:
            continue
        S = A + B
        F = S - E
        if F <= 0:
            continue
        # x = (B-A)/(4a), y = (D-C)/(4a), z = (F-E)/(4a); a^2 + K/a^2 = S/2
        K = ((B - A) ** 2 + (D - C) ** 2 + (F - E) ** 2) / 16
        t = sp.symbols('t', positive=True)  # t = a^2
        sols = [s for s in sp.solve(sp.Eq(t ** 2 - S / 2 * t + K, 0), t) if s.is_real and s > 0]
        for t0 in sols:
            a = sp.sqrt(t0)
            x, y, z = (B - A) / (4 * a), (D - C) / (4 * a), (F - E) / (4 * a)
            verts = [(a, 0, 0), (-a, 0, 0), (0, a, 0), (0, -a, 0), (0, 0, a), (0, 0, -a)]
            d2 = [sp.nsimplify(sp.simplify((x - u) ** 2 + (y - v) ** 2 + (z - w) ** 2)) for u, v, w in verts]
            target = [A, B, C, D, E, F]
            if all(abs(sp.N(d2[i] - target[i], 30)) < 1e-20 for i in range(6)):
                answers.add(sp.sqrt(F))
    return answers

orig = solve([3, 7, 8, 9, 11])
print("original:", orig)
assert orig == {sp.sqrt(66)}
var = solve([4, 8, 10, 11, 13])
print("variant:", var, [sp.N(v) for v in var])
assert var == {sp.sqrt(85)}
