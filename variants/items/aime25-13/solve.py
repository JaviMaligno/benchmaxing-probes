from fractions import Fraction
from itertools import permutations, product
from math import comb
import random

Q = 4  # quadrants
pairs = [(a, b) for a in range(Q) for b in range(Q) if a != b]

def interleave(pos, c1, c2):
    a, b = sorted((pos[c1[0]], pos[c1[1]]))
    x, y = pos[c2[0]], pos[c2[1]]
    return (a < x < b) != (a < y < b)

def p_chord_chord():
    # exact: assign quadrants, then random order of points within each quadrant
    tot = Fraction(0); cnt = 0
    for p1, p2 in product(pairs, pairs):
        quad = list(p1) + list(p2)  # points 0,1 chord1; 2,3 chord2
        perms = list(permutations(range(4)))
        good = 0; n = 0
        for pr in perms:  # tie-break order within quadrant
            key = sorted(range(4), key=lambda i: (quad[i], pr[i]))
            pos = {pt: r for r, pt in enumerate(key)}
            n += 1; good += interleave(pos, (0, 1), (2, 3))
        tot += Fraction(good, n); cnt += 1
    return tot / cnt

def p_chord_diam_expected():
    # diameters are quadrant boundaries; chord between quadrants a,b crosses
    # 1 diameter if adjacent, 2 if opposite
    s = sum(1 if (b - a) % 4 in (1, 3) else 2 for a, b in pairs)
    return Fraction(s, len(pairs))

def expected_regions(N):
    pcc = p_chord_chord(); ed = p_chord_diam_expected()
    segs = N + 2
    inter = 1 + N * ed + comb(N, 2) * pcc
    return 1 + segs + inter, pcc, ed

def mc(N, trials=20000, seed=1):
    rng = random.Random(seed)
    import math
    def pt():
        return rng.random() * 2 * math.pi
    tot = 0
    for _ in range(trials):
        chords = []
        for _ in range(N):
            while True:
                t1, t2 = pt(), pt()
                if int(t1 // (math.pi/2)) != int(t2 // (math.pi/2)): break
            chords.append(tuple(sorted((t1, t2))))
        I = 1
        for a, b in chords:
            # crossings with diameter through angles d, d+pi: chord crosses it iff exactly one of d, d+pi in (a,b)
            for d in (0.0, math.pi/2):
                # endpoints d / d+pi; treat 0 as 2pi boundary: angle 0 never strictly inside (a,b) since a>=0
                e1, e2 = d, d + math.pi
                ins = (a < e1 < b) + (a < e2 < b)
                if d == 0.0:
                    ins = (a < math.pi < b)  # endpoints 0 and pi: 0 never inside, so crossing iff pi inside
                    I += ins
                else:
                    I += ((a < e1 < b) != (a < e2 < b))
        for i in range(N):
            a, b = chords[i]
            for j in range(i+1, N):
                x, y = chords[j]
                I += ((a < x < b) != (a < y < b))
        tot += 1 + (N + 2) + I
    return tot / trials

orig, pcc, ed = expected_regions(25)
print("P(chord-chord) =", pcc, " E[chord-diameter crossings] =", ed)
print("ORIGINAL N=25:", orig, "(expected 204)", "OK" if orig == 204 else "MISMATCH")
for N in range(15, 36):
    v, _, _ = expected_regions(N)
    if v.denominator == 1: print("integer candidate N=%d -> %s" % (N, v))
NV = 16
var, _, _ = expected_regions(NV)
print("VARIANT N=%d:" % NV, var)
print("MC original N=25:", mc(25, 4000))
print("MC variant N=%d:" % NV, mc(NV, 8000))
