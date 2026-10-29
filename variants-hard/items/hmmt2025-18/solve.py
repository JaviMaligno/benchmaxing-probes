# Expected number of distinct values on a circle of n iid U[0,1] after t steps of
# a_i <- max(a_{i-1}, a_i, a_{i+1}). Only relative order matters -> use permutations.
from fractions import Fraction
from itertools import permutations
import random

def simulate(vals, t):
    n = len(vals); a = list(vals)
    for _ in range(t):
        a = [max(a[i-1], a[i], a[(i+1) % n]) for i in range(n)]
    return len(set(a))

def exact_bruteforce(n, t):
    tot = 0; cnt = 0
    for p in permutations(range(n)):
        tot += simulate(p, t); cnt += 1
    return Fraction(tot, cnt)

def formula(n, t):
    # each adjacent pair (j, j+1) differs after t steps iff the max of the
    # (2t+2)-window [j-t, j+t+1] sits at one of its two ends: prob 2/(2t+2).
    # Each surviving value occupies one arc, so #distinct = #changes (valid when 2t+1 < n).
    assert 2*t + 1 < n
    return Fraction(n, t + 1)

# Independent exact checks on small cases
for n, t in [(5,1),(6,1),(7,1),(7,2),(8,2),(8,3)]:
    b = exact_bruteforce(n, t); f = formula(n, t)
    print(f"n={n} t={t} brute={b} formula={f} match={b==f}")
    assert b == f

# Monte Carlo on a medium case
random.seed(1)
n, t, R = 61, 7, 20000
mc = sum(simulate([random.random() for _ in range(n)], t) for _ in range(R)) / R
print(f"MC n={n} t={t}: {mc:.4f} vs formula {float(formula(n,t)):.4f}")

orig = formula(2025, 100)
print("original (n=2025, t=100):", orig, "expected 2025/101:", orig == Fraction(2025, 101))
var = formula(1011, 60)
print("variant (n=1011, t=60):", var, float(var))
