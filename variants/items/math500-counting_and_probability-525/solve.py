from itertools import permutations
from math import factorial

def brute(n, k=3):
    # people 0..n-1; specials 0..k-1; fix person n-1 at seat 0 to quotient rotations
    count = 0
    others = list(range(n-1))
    for p in permutations(others):
        seat = [n-1] + list(p)
        ok = all(not (seat[i] < k and seat[(i+1) % n] < k) for i in range(n))
        count += ok
    return count

def formula(n, k=3):
    m = n - k
    gaps = 1
    for i in range(k): gaps *= (m - i)
    return factorial(m - 1) * gaps

orig = brute(7); assert orig == formula(7) == 144, orig
print("original (7 people):", orig)
var = brute(8); assert var == formula(8)
print("variant (8 people):", var)
