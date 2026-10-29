# Exact Markov-chain computation for the "merging snakes on a circle" problem.
# State: cyclic tuple of half-gaps h_i (empty arcs between consecutive snakes / 2).
# Gaps start even and change by (m_{i+1}-m_i) in {-2,0,2}, so they stay even; a gap hitting 0 = merge.
# Snake lengths do not affect the gap dynamics. Solve E[T] exactly level by level (number of snakes).
import itertools, random
import numpy as np
from fractions import Fraction

def canon(h):
    k = len(h)
    return min(tuple(h[i:] + h[:i]) for i in range(k)) if k else ()

def step_dist(h):
    k = len(h); out = {}
    p = Fraction(1, 2**k)
    for m in itertools.product((-1, 1), repeat=k):
        nh = [h[i] + (m[(i+1) % k] - m[i])//2 for i in range(k)]
        nh = [x for x in nh if x > 0]
        if len(nh) == 0:   # cannot happen when total > 0 unless k==1
            nh = []
        c = canon(nh) if len(nh) > 1 else ()
        out[c] = out.get(c, 0) + p
    return out

def compositions(total, k):
    for cuts in itertools.combinations(range(1, total), k-1):
        b = (0,) + cuts + (total,)
        yield tuple(b[i+1]-b[i] for i in range(k))

def expected_time(n_snakes, spacing):
    total_half = n_snakes * (spacing - 1) // 2   # sum of half-gaps
    E = {(): Fraction(0)}
    for k in range(2, n_snakes + 1):
        states = sorted({canon(c) for c in compositions(total_half, k)})
        idx = {s: i for i, s in enumerate(states)}
        N = len(states)
        A = np.zeros((N, N)); b = np.zeros(N); rows = []
        for s in states:
            i = idx[s]; A[i, i] += 1; rhs = Fraction(1); row = []
            for t, p in step_dist(list(s)).items():
                if t in idx: A[i, idx[t]] -= float(p); row.append((idx[t], p))
                else: rhs += p * E[t]
            b[i] = float(rhs); rows.append((row, rhs))
        x = np.linalg.solve(A, b)
        xf = [Fraction(v).limit_denominator(10**7) for v in x]
        # exact verification: rationalised solution satisfies every equation exactly
        for i, (row, rhs) in enumerate(rows):
            assert xf[i] - sum(p * xf[j] for j, p in row) == rhs, ("not exact", k, i)
        for s in states: E[s] = xf[idx[s]]
    start = canon([(spacing - 1)//2] * n_snakes)
    return E[start]

def simulate(n_snakes, spacing, trials=20000, seed=1):
    rng = random.Random(seed); tot = 0
    for _ in range(trials):
        h = [(spacing-1)//2]*n_snakes; t = 0
        while len(h) > 1:
            k = len(h); m = [rng.choice((-1, 1)) for _ in range(k)]
            h = [h[i] + (m[(i+1) % k]-m[i])//2 for i in range(k)]
            h = [x for x in h if x > 0]; t += 1
        tot += t
    return tot / trials

import sys
for label, n, sp_ in [("ORIGINAL (45 arcs, 15 snakes, every 3rd)", 15, 3), ("VARIANT (36 arcs, 12 snakes, every 3rd)", 12, 3)]:
    v = expected_time(n, sp_)
    print(label, "exact =", v, "=", float(v), "| MC ~", simulate(n, sp_, 5000))
