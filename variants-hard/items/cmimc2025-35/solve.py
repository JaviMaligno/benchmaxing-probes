from fractions import Fraction
from itertools import product
import random

def exact(n):
    # Linearity over x: enumerate y=f(x); if y==x then f(f(x))=x, else f(y) is uniform and independent.
    total = Fraction(0)
    for x in range(1, n+1):
        for y in range(1, n+1):
            if y == x:
                total += Fraction(1, n) * 0
            else:
                for z in range(1, n+1):
                    total += Fraction(1, n*n) * (z - x)**2
    return total

def brute(n):
    s = 0; cnt = 0
    for f in product(range(1, n+1), repeat=n):
        s += sum((f[f[x-1]-1] - x)**2 for x in range(1, n+1)); cnt += 1
    return Fraction(s, cnt)

def mc(n, trials=200000, seed=1):
    rng = random.Random(seed); s = 0
    for _ in range(trials):
        f = [rng.randint(1, n) for _ in range(n)]
        s += sum((f[f[x-1]-1] - x)**2 for x in range(1, n+1))
    return s / trials

for n in range(1, 7):
    assert exact(n) == brute(n), n
print("exact == full brute force for n=1..6")
orig = exact(25)
print("original n=25:", orig, "(expected 2496)", orig == 2496)
var = exact(23)
print("variant n=23:", var)
print("Monte Carlo n=23:", round(mc(23), 1))
