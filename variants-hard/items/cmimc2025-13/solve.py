from fractions import Fraction as F
from math import comb
import random

def exact(n, g):
    # P(two specific players ever share a battle); g chosen, 1 stays, g-1 leave
    assert (n - 1) % (g - 1) == 0
    alive, total, k = F(1), F(0), n
    while k > 1:
        c = comb(k, g)
        both = F(comb(k - 2, g - 2), c)
        neither = F(comb(k - 2, g), c)
        one = 1 - both - neither
        total += alive * both
        alive *= neither + one * F(1, g)   # exactly one chosen and that one wins
        k -= g - 1
    return total

def sim(n, g, trials=20000, seed=1):
    rng = random.Random(seed); hit = 0
    for _ in range(trials):
        pl = list(range(n))
        while len(pl) > 1:
            ch = rng.sample(pl, g)
            if 0 in ch and 1 in ch: hit += 1; break
            w = rng.choice(ch)
            pl = [p for p in pl if p not in ch or p == w]
    return hit / trials

orig = exact(34, 4)
print("original (34 players, battles of 4):", orig, "sim", sim(34, 4))
assert orig == F(2, 17)
var = exact(45, 5)
print("variant (45 players, battles of 5):", var, float(var), "sim", sim(45, 5))
