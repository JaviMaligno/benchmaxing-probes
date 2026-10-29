from fractions import Fraction as F
from itertools import product
import random

def closed_form(pa, pb):
    # Alice wins on her k-th turn: ((1-pa)(1-pb))^(k-1) * pa ; geometric series
    return pa / (1 - (1 - pa) * (1 - pb))

def truncated_series(pa, pb, K=200):
    s = F(0); r = (1 - pa) * (1 - pb)
    for k in range(K):
        s += r**k * pa
    return s

def first_step(pa, pb):
    # a = pa + (1-pa)(1-pb) a  -> solve
    return pa / (1 - (1 - pa) * (1 - pb))

def simulate(alice_wins, bob_wins, faces, n=400000, seed=1):
    rng = random.Random(seed); w = 0
    for _ in range(n):
        while True:
            if alice_wins(rng.choice(faces)): w += 1; break
            if bob_wins(rng.choice(faces)): break
    return w / n

# Original: coin; Alice wins on heads (1/2), Bob wins on tails (1/2)
pa, pb = F(1, 2), F(1, 2)
orig = closed_form(pa, pb)
assert orig == first_step(pa, pb)
assert abs(float(truncated_series(pa, pb)) - float(orig)) < 1e-12
print("original:", orig, "sim:", simulate(lambda x: x == 'H', lambda x: x == 'T', ['H', 'T']))
assert orig == F(2, 3)

# Variant: fair six-sided die; Alice wins on 5 or 6, Bob wins on 1 or 2
die = [1, 2, 3, 4, 5, 6]
pa = F(sum(1 for d in die if d >= 5), 6)
pb = F(sum(1 for d in die if d <= 2), 6)
var = closed_form(pa, pb)
assert var == first_step(pa, pb)
assert abs(float(truncated_series(pa, pb)) - float(var)) < 1e-12
print("variant:", var, float(var), "sim:", simulate(lambda x: x >= 5, lambda x: x <= 2, die))
