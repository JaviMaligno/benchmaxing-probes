# Cave height: stalactites a,b from ceiling (tips at y=H-a, H-b), stalagmites c,d (tips at y=c, d).
# Four tips form a square. Square <=> pick a diagonal pairing; diagonals share midpoint,
# are perpendicular and of equal length. Solve exactly over all 3 pairings with sympy.
import sympy as sp

def solve(a, b, c, d):
    H, x2, x3, x4 = sp.symbols('H x2 x3 x4', real=True)
    P = [(0, H - a), (x2, H - b), (x3, sp.Integer(c)), (x4, sp.Integer(d))]
    sols = set()
    for (i, j), (k, l) in [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]:
        u = (P[j][0] - P[i][0], P[j][1] - P[i][1])
        v = (P[l][0] - P[k][0], P[l][1] - P[k][1])
        eqs = [P[i][0] + P[j][0] - P[k][0] - P[l][0],
               P[i][1] + P[j][1] - P[k][1] - P[l][1],
               u[0]*v[0] + u[1]*v[1],
               u[0]**2 + u[1]**2 - v[0]**2 - v[1]**2]
        for s in sp.solve(eqs, [H, x2, x3, x4], dict=True):
            if H not in s or s[H].free_symbols:
                print("  pairing", (i, j), (k, l), "underdetermined:", s)
                continue
            h = s[H]
            # tips strictly inside the cave, nondegenerate square
            if all(0 < y < h for y in [h - a, h - b, c, d]) and (u[0]**2 + u[1]**2).subs(s) != 0:
                sols.add(h)
    return sols

orig = solve(16, 36, 25, 49)
print("original:", orig)
assert orig == {63}
var = solve(18, 34, 25, 47)
print("variant:", var)
assert len(var) == 1
