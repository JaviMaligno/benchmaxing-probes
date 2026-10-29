# Brute force: row-major grid sum vs multiplication-table grid sum, difference D.
def grid_sums(a, b):
    row_major = sum(r * b + c + 1 for r in range(a) for c in range(b))
    mult = sum((i + 1) * (j + 1) for i in range(a) for j in range(b))
    return row_major, mult

def solve(D, N=400):
    sols = set()
    for a in range(1, N):
        for b in range(1, N):
            # closed form ab(a-1)(b-1)/4 used only as a pruning bound
            if a * b * (a - 1) * (b - 1) > 4 * D:
                break
            r, m = grid_sums(a, b)
            if abs(r - m) == D:
                sols.add(a + b)
    return sols

orig = solve(1200)
print("original (D=1200) a+b values:", orig)
assert orig == {21}
var = solve(2100)
print("variant (D=2100) a+b values:", var)
assert len(var) == 1
print("variant answer:", var.pop())
