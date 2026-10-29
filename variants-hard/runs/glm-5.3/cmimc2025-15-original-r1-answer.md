```python
from fractions import Fraction
from functools import lru_cache
from collections import Counter

NV = 3

def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

def A(c):
    n = sum(c)
    return fact(n) // (fact(c[0]) * fact(c[1]) * fact(c[2]))

@lru_cache(None)
def ndp(c, prev):
    if sum(c) == 0:
        return 1
    t = 0
    for u in range(NV):
        if c[u] > 0 and u != prev:
            c2 = list(c); c2[u] -= 1
            t += ndp(tuple(c2), u)
    return t

def nd(c):
    return ndp(tuple(c), -1)

@lru_cache(None)
def D(c, v):
    if sum(c) == 1:
        return 1 if c[v] == 1 else 0
    c2 = list(c); c2[v] -= 1
    c2 = tuple(c2)
    t = 0
    for u in range(NV):
        if c2[u] > 0 and u != v:
            t += D(c2, u)
    return t

def c_p(P):
    t = 0
    for v in range(NV):
        if P[v] >= 2:
            P2 = list(P); P2[v] -= 1
            t += D(tuple(P2), v)
    return t

@lru_cache(None)
def f(c):
    c = tuple(c)
    n = sum(c)
    tot = Fraction(0)
    for a in range(c[0] + 1):
        for b in range(c[1] + 1):
            for d in range(c[2] + 1):
                Mp = (a, b, d)
                if sum(Mp) > n - 2:
                    continue
                rem = (c[0]-a, c[1]-b, c[2]-d)
                cp = c_p(rem)
                if cp == 0:
                    continue
                p = Fraction(A(Mp) * cp, A(c))
                tot += p * (1 + f(Mp))
    return tot

print("sanity f(2,2,0) =", f((2,2,0)), "(esperado 1)")
print("sanity f(4,0,0) =", f((4,0,0)), "(esperado 2)")
print("sanity f(1,1,1) =", f((1,1,1)), "(esperado 0)")
ans = f((4,4,4))
print("DP f(4,4,4) =", ans, "=", float(ans))
print("P(sin dobles) =", Fraction(nd((4,4,4)), A((4,4,4))))

def simulate(seq):
    seq = list(seq)
    cnt = 0
    i = 0
    while True:
        found = None
        for j in range(i, len(seq) - 1):
            if seq[j] == seq[j+1]:
                found = j
                break
        if found is None:
            return cnt
        cnt += 1
        i = found + 2

def gen(c):
    if sum(c) == 0:
        yield ()
        return
    for u in range(NV):
        if c[u] > 0:
            c2 = list(c); c2[u] -= 1
            for rest in gen(tuple(c2)):
                yield (u,) + rest

tot = 0
num = 0
dist = Counter()
for s in gen((4,4,4)):
    v = simulate(s)
    tot += v
    num += 1
    dist[v] += 1

print("brute force: casos =", num, " suma N =", tot)
bf = Fraction(tot, num)
print("brute force E[N] =", bf, "=", float(bf))
print("distribucion:", sorted(dist.items()))
print("COINCIDEN:", ans == bf)
```