# Regular N-gon (N even) = zonogon with m = N/2 edge directions at angles k*pi/m.
# In any parallelogram tiling, every pair of zones (directions) meets in exactly one tile,
# so the tile multiset is fixed: one parallelogram per pair {i,j}. R = # perpendicular pairs.
from fractions import Fraction
import math

def R(N):
    assert N % 2 == 0
    m = N // 2
    # angles k/m (in units of pi), mod 1; perpendicular iff difference == 1/2
    cnt = 0
    for i in range(m):
        for j in range(i + 1, m):
            if 2 * (j - i) == m:
                cnt += 1
    return cnt

def area_check(N):
    # independent numeric check: sum of all pair-parallelogram areas = polygon area
    m = N // 2
    v = [(math.cos(math.pi * k / m), math.sin(math.pi * k / m)) for k in range(m)]
    s = sum(abs(v[i][0]*v[j][1]-v[i][1]*v[j][0]) for i in range(m) for j in range(i+1, m))
    poly = N / (4 * math.tan(math.pi / N))  # side 1
    return abs(s - poly) < 1e-6 * poly

for n in (6, 8, 10, 12, 16):
    assert area_check(n)
orig = R(8960)
print("original R(8960) =", orig, "expected 2240 ->", orig == 2240)
print("variant  R(6720) =", R(6720))
