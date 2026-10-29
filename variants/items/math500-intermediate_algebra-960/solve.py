from fractions import Fraction as F
import itertools

def closed(u, v, w):
    # Ravi substitution: s even -> (j+k, i+k, i+j); s odd -> each minus 1
    g = lambda t: t / (1 - t)
    return (1 + 1 / (u * v * w)) * g(v * w) * g(u * w) * g(u * v)

def brute(u, v, w, N=90):
    u, v, w = float(u), float(v), float(w)
    tot = 0.0
    for a in range(1, N):
        for b in range(1, N):
            for c in range(max(1, abs(a - b) + 1), min(N, a + b)):
                tot += u**a * v**b * w**c
    return tot

orig = closed(F(2), F(1, 3), F(1, 5))
print("original closed:", orig, "brute:", brute(2, F(1,3), F(1,5)))
assert orig == F(17, 21)
var = closed(F(3), F(1, 4), F(1, 5))
print("variant closed:", var, "brute:", brute(3, F(1,4), F(1,5), 160), "float:", float(var))
