import sys
from functools import lru_cache
sys.setrecursionlimit(100000)

def make_f(m, j0):
    """f(0,j)=(j+1) mod m; f(i,0)=f(i-1,j0); f(i,j)=f(i-1,f(i,j-1))."""
    @lru_cache(maxsize=None)
    def f(i, j):
        if i == 0:
            return (j + 1) % m
        if j == 0:
            return f(i - 1, j0)
        return f(i - 1, f(i, j - 1))
    return f

def evaluate(m, j0, I, J):
    f = make_f(m, j0)
    for i in range(I + 1):  # fill bottom-up to keep recursion shallow
        for j in range(m):
            f(i, j)
    return f(I, J)

def table_method(m, j0, I, J):
    # independent check: iterate rows until a row repeats, then extrapolate
    rows = [[(j + 1) % m for j in range(m)]]
    seen = {tuple(rows[0]): 0}
    while True:
        prev = rows[-1]
        r = [prev[j0]]
        for j in range(1, m):
            r.append(prev[r[j - 1]])
        rows.append(r)
        t = tuple(r)
        if t in seen:
            start = seen[t]; period = len(rows) - 1 - start
            break
        seen[t] = len(rows) - 1
    idx = I if I < len(rows) else start + (I - start) % period
    return rows[idx][J]

orig = evaluate(5, 1, 2015, 2)
assert orig == table_method(5, 1, 2015, 2)
print("original f(2015,2) =", orig, "(expected 1)")
assert orig == 1

var = evaluate(5, 2, 2024, 3)
assert var == table_method(5, 2, 2024, 3)
print("variant f(2024,3) =", var)
