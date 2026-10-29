# k(n,p): max k s.t. exists integer poly P with [x^n]P = 1 and p^k | P(x) for all integers x.
# Write P = sum_j a_j (x)_j (falling factorials, a_j integers). P vanishes mod p^k on Z
# iff p^k | a_j * j! for all j (Newton forward differences). [x^n]P = sum_{j>=n} a_j s(j,n).
# So achievable iff some j>=n has v_p(j!) >= k and p does not divide s(j,n):
#   k(n,p) = max{ v_p(j!) : j >= n, p !| s(j,n) }.
# (x)_j mod p = (x^p-x)^q (x)_r with j=qp+r has min degree >= q, so j < (n+1)p suffices.
from sympy.functions.combinatorial.numbers import stirling
from sympy import factorial, multiplicity
import itertools

def vfact(j, p):
    v, q = 0, p
    while q <= j:
        v += j // q; q *= p
    return v

def k_formula(n, p):
    best = 0
    for j in range(n, (n + 1) * p + p):
        if stirling(j, n, kind=1, signed=True) % p != 0:
            best = max(best, vfact(j, p))
    return best

# Independent check (no falling factorials / Stirling numbers): direct linear algebra over Z/p^k.
# Exists integer P of degree <= D with [x^n]P=1 and p^k | P(x) for all x  <=>  the system
# sum_{d!=n} c_d x^d == -x^n (mod p^k) for x = 0..p^k-1 is solvable (P(x+p^k)==P(x) mod p^k).
def solvable_mod(A, b, p, k):
    m = p ** k
    A = [[a % m for a in row] + [bb % m] for row, bb in zip(A, b)]
    rows, cols = len(A), len(A[0]) - 1
    def val(a):
        if a % m == 0: return k
        v = 0
        while a % p == 0: a //= p; v += 1
        return v
    r = 0
    colset = list(range(cols))
    while r < rows and colset:
        best = None
        for i in range(r, rows):
            for j in colset:
                if A[i][j] % m:
                    vv = val(A[i][j])
                    if best is None or vv < best[0]: best = (vv, i, j)
        if best is None: break
        vv, i, j = best
        A[r], A[i] = A[i], A[r]
        unit = (A[r][j] // p**vv) % m
        inv = pow(unit, -1, m)
        A[r] = [(a * inv) % m for a in A[r]]  # pivot now p^vv
        for i2 in range(rows):
            if i2 != r and A[i2][j] % m:
                f = (A[i2][j] // p**vv) % m  # divisible since min valuation
                A[i2] = [(a - f * c) % m for a, c in zip(A[i2], A[r])]
        colset.remove(j)
        r += 1
    # remaining rows have zero coefficients; also each pivot row needs p^vv | rhs
    for i in range(rows):
        nz = [j for j in range(cols) if A[i][j] % m]
        if not nz:
            if A[i][-1] % m: return False
        else:
            vmin = min(val(A[i][j]) for j in nz)
            if val(A[i][-1]) < vmin: return False
    return True

def k_brute(n, p, D):
    k = 0
    while True:
        m = p ** (k + 1)
        xs = range(m)
        A = [[pow(x, d, m) for d in range(D + 1) if d != n] for x in xs]
        b = [-pow(x, n, m) for x in xs]
        if not solvable_mod(A, b, p, k + 1): return k
        k += 1

for p in (2, 3, 5):
    for n in range(1, 6 if p < 5 else 4):
        kb = k_brute(n, p, D=3 * (n + 1) * p)
        kf = k_formula(n, p)
        assert kf == kb, (n, p, kf, kb)
print("brute-force linear-algebra check agrees with formula on small (n,p)")

orig = sum(k_formula(n, p) for n in range(11, 16) for p in (11, 13))
print("original:", orig)
assert orig == 138
var = sum(k_formula(n, p) for n in range(17, 22) for p in (17, 19))
print("variant:", var)
