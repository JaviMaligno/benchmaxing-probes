from fractions import Fraction as F
# f(n+1) = (-1)^(n+1) n - 2 f(n), f(1) = f(N+1); find sum f(1..N).
# Direct method: f(n) = a_n + b_n * f(1) linear in x=f(1); solve f(N+1)=f(1) exactly, then sum.
def solve(N):
    a, b = F(0), F(1)
    seq = [(a, b)]
    for n in range(1, N + 1):
        a, b = (-1) ** (n + 1) * n - 2 * a, -2 * b
        seq.append((a, b))
    aN, bN = seq[N]  # f(N+1)
    x = aN / (1 - bN)
    vals = [p + q * x for p, q in seq]
    assert vals[N] == vals[0]
    for n in range(1, N + 1):  # recheck recurrence
        assert vals[n] == (-1) ** (n + 1) * n - 2 * vals[n - 1]
    return sum(vals[:N])
def closed(N):  # telescoping: 3*sum = 1 - 2 + 3 - ... + N
    return F(sum((-1) ** (k + 1) * k for k in range(1, N + 1)), 3)
orig = solve(1985); print("original N=1985:", orig, closed(1985)); assert orig == 331
var = solve(2021); print("variant N=2021:", var, closed(2021)); assert var == closed(2021)
