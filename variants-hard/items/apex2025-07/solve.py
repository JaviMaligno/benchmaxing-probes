"""apex2025-07 variant: n people, k colors; smallest C.
Lower-bound construction: all people identical with masses p_i; the best choice
uses c_i people on colour i and the value is min T with sum floor(T/p_i) >= n.
The adversary maximises T = 1/sum 1/(c_i+1) over sum c_i = n-1 (balanced c_i).
Closed form: n-1 = k*q + s  ->  C = 1/((k-s)/(q+1) + s/(q+2)).
We check (1) closed form == search over two-level identical distributions,
(2) original data reproduces 248/517, (3) small cases: random/local search over
NON-identical people never beats the formula (exact min-max by enumeration)."""
from fractions import Fraction as F
import itertools, random

def closed(n, k):
    q, s = divmod(n - 1, k)
    return 1 / (F(k - s, q + 1) + F(s, q + 2))

def search(n, k):
    best = F(0)
    for j in range(0, k + 1):
        for m in range(0, n):
            rem = n - 1 - j * m
            if rem < 0: break
            if k - j == 0:
                if rem == 0: best = max(best, F(m + 1, j))
                continue
            if rem % (k - j): continue
            l = rem // (k - j)
            best = max(best, 1 / (F(j, m + 1) + F(k - j, l + 1)))
    return best

def exact_minmax(P, k):
    best = float('inf')
    for ch in itertools.product(range(k), repeat=len(P)):
        s = [0.0] * k
        for person, c in zip(P, ch): s[c] += person[c]
        best = min(best, max(s))
    return best

def small_check(n, k, iters=1500, seed=0):
    rng = random.Random(seed); f = float(closed(n, k)); worst = 0.0
    for _ in range(iters):
        P = []
        for _ in range(n):
            w = [rng.random() ** 3 + 1e-9 for _ in range(k)]; t = sum(w)
            P.append([x / t for x in w])
        v = exact_minmax(P, k)
        # local hill-climb
        for _ in range(40):
            Q = [row[:] for row in P]
            i = rng.randrange(n); a, b = rng.sample(range(k), 2)
            d = rng.uniform(0, 0.1) * Q[i][a]; Q[i][a] -= d; Q[i][b] += d
            vq = exact_minmax(Q, k)
            if vq >= v: P, v = Q, vq
        worst = max(worst, v)
    return worst, f

orig = closed(2025, 66)
print("original:", orig, "search:", search(2025, 66), "matches 248/517:", orig == F(248, 517) == search(2025, 66))
var = closed(2025, 56)
print("variant (2025 people, 56 colors):", var, "search:", search(2025, 56), "agree:", var == search(2025, 56), float(var))
for n, k in [(4, 3), (5, 3), (5, 2), (6, 4)]:
    w, f = small_check(n, k, iters=25)
    print(f"small n={n},k={k}: best found {w:.5f} <= formula {f:.5f}: {w <= f + 1e-9}")
