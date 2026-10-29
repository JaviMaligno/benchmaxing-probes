from itertools import permutations
from fractions import Fraction
import random, math

def cross(pos, p, q):
    # chords p=(a,b), q=(c,d) with positions on circle cross iff exactly one of c,d lies strictly between a,b
    a, b = sorted((pos[p[0]], pos[p[1]]))
    c, d = pos[q[0]], pos[q[1]]
    return (a < c < b) != (a < d < b)

def exact(labels, chords):
    # all relative orders of n distinct random points are equally likely
    good = tot = 0
    for perm in permutations(range(len(labels))):
        pos = dict(zip(labels, perm))
        tot += 1
        if all(cross(pos, chords[i], chords[j]) for i in range(len(chords)) for j in range(i+1, len(chords))):
            good += 1
    return Fraction(good, tot)

def monte_carlo(labels, chords, trials=200000, seed=1):
    rng = random.Random(seed); good = 0
    for _ in range(trials):
        pos = {L: rng.random() * 2 * math.pi for L in labels}
        if all(cross(pos, chords[i], chords[j]) for i in range(len(chords)) for j in range(i+1, len(chords))):
            good += 1
    return good / trials

orig = exact("ABCD", [("A","B"), ("C","D")])
print("original exact:", orig, "matches 1/3:", orig == Fraction(1,3))
var = exact("PQRSTU", [("P","Q"), ("R","S"), ("T","U")])
print("variant exact:", var)
print("variant monte carlo:", monte_carlo("PQRSTU", [("P","Q"), ("R","S"), ("T","U")]))
