from math import factorial
from itertools import product

def by_formula(n):
    tot = 0
    for c in range(1, n+1):
        for v in range(1, n+1):
            s = n - c - v
            if s >= 1 and c > v > s:
                tot += factorial(n)//(factorial(c)*factorial(v)*factorial(s))
    return tot

def brute(n):
    cnt = 0
    for a in product(range(3), repeat=n):
        c, v, s = a.count(0), a.count(1), a.count(2)
        if s >= 1 and c > v > s:
            cnt += 1
    return cnt

for n in (9, 10):
    f, b = by_formula(n), brute(n)
    assert f == b
    print(f"n={n}: N={f}, N mod 1000 = {f % 1000}")
assert by_formula(9) % 1000 == 16
print("original check OK (16)")
print("variant answer:", by_formula(10) % 1000)
