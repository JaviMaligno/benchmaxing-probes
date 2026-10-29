import sympy as sp, math

def C(M):
    M = sp.Matrix(M)
    k = sp.symbols('k')
    G = M.T * M
    # k feasible iff discriminant of (G00-k)x^2 + 2G01 xy + (G11-k)y^2 >= 0
    disc = sp.expand((2*G[0,1])**2 - 4*(G[0,0]-k)*(G[1,1]-k))
    roots = sp.solve(sp.Eq(disc, 0), k)
    return sp.sqrt(max(roots))

def numeric(M, n=200000):
    best = 0
    for i in range(n):
        t = 2*math.pi*i/n
        x, y = math.cos(t), math.sin(t)
        u = M[0][0]*x + M[0][1]*y; w = M[1][0]*x + M[1][1]*y
        best = max(best, math.hypot(u, w))
    return best

orig = [[2,3],[0,-2]]
var = [[3,8],[0,-3]]
co = C(orig); cv = C(var)
print("original:", co, numeric(orig))
assert co == 4
print("variant:", cv, numeric(var))
print("ANSWER", cv)
