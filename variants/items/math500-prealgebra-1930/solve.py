from sympy import symbols, Eq, solve, simplify, Integer
n = symbols('n')

def solve_square(g):
    # g: rows top->bottom, each row left->right
    lines = [r for r in g] + [[g[i][j] for i in range(3)] for j in range(3)]
    lines += [[g[i][i] for i in range(3)], [g[i][2-i] for i in range(3)]]
    sums = [sum(l) for l in lines]
    eqs = [Eq(sums[0], s) for s in sums[1:] if simplify(sums[0]-s) != 0]
    sol = solve(eqs, n, dict=True)
    assert len(sol) == 1, sol
    v = sol[0][n]
    vals = [[e.subs(n, v) for e in r] for r in g]
    assert len({sum(l).subs(n, v) for l in lines}) == 1
    return v, vals

orig = [[n+1, Integer(1), n-1], [Integer(3), 2*n-9, n], [n-3, n+2, Integer(2)]]
v, vals = solve_square(orig)
print("original n =", v, vals); assert v == 7

var = [[n+1, Integer(3), n-1], [Integer(5), 2*n-11, n], [n-3, n+2, Integer(4)]]
v2, vals2 = solve_square(var)
print("variant n =", v2, vals2)
# brute-force independent check
bf = [k for k in range(-100, 101) if len({sum(l) for l in (
    [[e.subs(n,k) for e in r] for r in var] +
    [[var[i][j].subs(n,k) for i in range(3)] for j in range(3)] +
    [[var[i][i].subs(n,k) for i in range(3)], [var[i][2-i].subs(n,k) for i in range(3)]])}) == 1]
print("brute force:", bf)
