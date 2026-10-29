from fractions import Fraction as F

def brute(x1, K):
    x = F(x1)
    for _ in range(K - 1):
        x = (x + 1/x - 1) / 3
    return x

def fast(x1, K, mod=1000):
    # with x_k = a/b reduced and 3 | a+b, x_{k+1} = ((a^2-ab+b^2)/3)/(ab) is reduced,
    # so s = a+b satisfies s_{k+1} = s_k^2 / 3. Write s = 3t: t_{k+1} = t_k^2 (exact integers).
    x1 = F(x1)
    s = x1.numerator + x1.denominator
    assert s % 3 == 0
    t = (s // 3) % mod
    for _ in range(K - 1):
        t = (t * t) % mod
    return (3 * t) % mod

for x1 in [F(25, 11), F(19, 14)]:
    # independent exact check of the recurrence for the first terms
    for K in range(1, 9):
        x = brute(x1, K)
        assert fast(x1, K, 10**12) == (x.numerator + x.denominator) % 10**12, (x1, K)

orig = fast(F(25, 11), 2025)
print("original x1=25/11 ->", orig)
assert orig == 248
var = fast(F(19, 14), 2025)
print("variant x1=19/14 ->", var)
